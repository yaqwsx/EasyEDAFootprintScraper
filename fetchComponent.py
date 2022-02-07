#!/usr/bin/env python3

import requests
import json
import re
import pcbnew
import os
import subprocess
import click
from tempfile import TemporaryDirectory
from pathlib import Path

class FormatError(RuntimeError):
    pass

def easyEdaHeaders(token):
    return {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-csrf-token': token,
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'isajax': 'true',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://easyeda.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://easyeda.com',
        'accept-language': 'cs,en;q=0.9,sk;q=0.8,en-GB;q=0.7',
    }

def extractCsrfToken(pageText):
    m = re.search(r"'X-CSRF-TOKEN':\s*'(.*)'", pageText)
    if not m:
        return None
    return m.group(1)

def obtainCsrfTokenAndCookies():
    homePage = requests.get("https://easyeda.com/")
    return extractCsrfToken(homePage.text), homePage.cookies

def searchComponents(text, token=None, cookies=None):
    """
    Perform fulltext search, return list of components
    """
    if token is None or cookies is None:
        token, cookies = obtainCsrfTokenAndCookies()
    res = requests.post("https://easyeda.com/api/components/search",
        headers=easyEdaHeaders(token), cookies=cookies,
        data={
            "wd": text
        })
    components = []
    lists = res.json()["result"]["lists"]
    if isinstance(lists, list):
        for component in lists:
            components.append(component)
    else:
        for componentList in res.json()["result"]["lists"].values():
            for component in componentList:
                components.append(component)
    return components

def getComponentInfo(lcscCode, token=None, cookies=None):
    for component in searchComponents(lcscCode, token, cookies):
        if component["dataStr"]["head"]["c_para"]["BOM_Supplier Part"] == lcscCode:
            return component

def fetchCompnentDetails(componetUuid, token=None, cookies=None):
    if token is None or cookies is None:
        token, cookies = obtainCsrfTokenAndCookies()
    res = requests.get(f"https://easyeda.com/api/components/{componetUuid}",
        headers=easyEdaHeaders(token), cookies=cookies,
        data={})
    return res.json()["result"]

def getComponentSymbol(componentDetail):
    sch = {
        "editorVersion": "6.4.14",
        "docType": "5",
        "title": "TempSch",
        "description": "",
        "colors": {},
        "schematics": [
        {
            "docType": "1",
            "title": "Sheet_1",
            "description": "",
            "dataStr": {
            "head": {
                "docType": "1",
                "editorVersion": "6.4.14",
                "newgId": True,
                "c_para": {
                "Prefix Start": "1"
                },
                "c_spiceCmd": None
            },
            "colors": {}
            }
        }
        ]
    }
    
    for text in ["canvas", "BBox"]:
        sch["schematics"][0]["dataStr"][text] = componentDetail["dataStr"][text]
    
    shape = "LIB~-5~5~package`" + componentDetail["packageDetail"]["title"] + "`BOM_Supplier`LCSC`BOM_Supplier Part`" + componentDetail["lcsc"]["number"] + "`BOM_Manufacturer`" + componentDetail["dataStr"]["head"]["c_para"]["BOM_Manufacturer"] + "`BOM_Manufacturer Part`" + componentDetail["dataStr"]["head"]["c_para"]["BOM_Manufacturer Part"] + "`Contributor`" + componentDetail["dataStr"]["head"]["c_para"]["Contributor"] + "`spicePre`" + componentDetail["dataStr"]["head"]["c_para"]["pre"][:-1] + "`spiceSymbolName`" + componentDetail["dataStr"]["head"]["c_para"]["name"] + "`~~0~gge03d9a0f3a4a33646~" + componentDetail["uuid"] + "~052918e6192f4a27891c8ca5941aa6aa~0~~yes~yes"
    for line in componentDetail["dataStr"]["shape"]:
        shape += "#@$"
        shape += line
    sch["schematics"][0]["dataStr"]["shape"] = [shape]
    
    return sch

def getComponentPackageName(componentInfo):
    return componentInfo["dataStr"]["head"]["c_para"]["package"]

def getComponentPackage(componentDetail):
    return componentDetail["packageDetail"]

def buildPackageBoard(packageInfo):
    """
    Builds EasyEDA board with a single footprint for footprint extraction
    """
    board = {}
    board["head"] = {
        "docType": "3",
        "editorVersion": "6.4.7",
        "newgId": True,
        "c_para": {},
        "hasIdFlag": True
    }
    for field in ["BBox", "objects", "layers"]:
        board[field] = packageInfo["dataStr"][field]
    x = packageInfo["dataStr"]["head"]["x"]
    y = packageInfo["dataStr"]["head"]["y"]
    shape = f"LIB~{x}~{y}~package`{getComponentPackageName(packageInfo)}`~0~~~1#@$"
    shape += "#@$".join(packageInfo["dataStr"]["shape"])
    board["shape"] = [shape]
    return board

def easyEdaToKicad(symbolJson, boardJson):
    """
    Convert board JSON, return pcbnew.BOARD
    """
    with TemporaryDirectory() as tmpDir:
        symbolFilename = os.path.join(tmpDir, "symbol.json")
        boardFilename = os.path.join(tmpDir, "board.json")
        kicadFilename = os.path.join(tmpDir, "board.kicad_pcb")
        with open(symbolFilename, "w") as schFile:
            schFile.write(json.dumps(symbolJson, indent=2))
        with open(boardFilename, "w") as easyFile:
            easyFile.write(json.dumps(boardJson, indent=4))
        subprocess.check_call(["easyeda2kicad", boardFilename, kicadFilename])
        os.system("./LC2KiCad/build/lc2kicad -v " + symbolFilename + " -a ENL:1")
        return pcbnew.LoadBoard(kicadFilename)

def validateLibName(lib):
    if not lib.endswith(".pretty"):
        raise FormatError(f"'{lib} is not valid library path, it has to end with '.pretty'")

def ensureKicadLib(lib):
    """
    Ensure the given KiCAD library exists, if not, create it
    """
    if os.path.exists(lib):
        return
    pcbnew.PCB_IO().FootprintLibCreate(lib)

def ensure3DLib(lib):
    Path(lib).mkdir(exist_ok=True, parents=True)

def extractFirstFootprint(board):
    for f in board.GetFootprints():
        return f

def topMiddle(rect):
    return pcbnew.wxPoint(rect.GetX() + rect.GetWidth() // 2, rect.GetY())

def bottomMiddle(rect):
    return pcbnew.wxPoint(rect.GetX() + rect.GetWidth() // 2, rect.GetY() + rect.GetHeight())

def postProcessFootprint(footprint):
    footprint.Reference().SetVisible(False)
    footprint.Value().SetVisible(False)

    bbox = footprint.GetBoundingBox(False, False)
    refPos = topMiddle(bbox) + pcbnew.wxPoint(0, -footprint.Reference().GetTextHeight())
    valuePos = bottomMiddle(bbox) + pcbnew.wxPoint(0, +footprint.Reference().GetTextHeight())

    footprint.Reference().SetPosition(refPos)
    footprint.Value().SetPosition(valuePos)

    footprint.Reference().SetVisible(True)
    footprint.Value().SetVisible(True)

def footprintExists(lib, name):
    # PCB_IO().FootprintExists behaves strangely, thus, we implement it ourselves
    return os.path.exists(os.path.join(lib, name + ".kicad_mod"))

def fetchAndConvert(componentInfo, token, cookies):
    uuid = componentInfo["dataStr"]["head"]["uuid"]
    details = fetchCompnentDetails(uuid, token, cookies)
    schSymbol = getComponentSymbol(details)
    package = getComponentPackage(details)
    packageBoard = buildPackageBoard(package)
    kicadBoard = easyEdaToKicad(schSymbol, packageBoard)
    footprint = extractFirstFootprint(kicadBoard)
    postProcessFootprint(footprint)

    return details, footprint

def fetchAndConvert3D(componentDetail, kicadlib, pathvar, token, cookies):
    lib3D = kicadlib.replace(".pretty", ".3dshapes")
    ensure3DLib(lib3D)

    models = []
    submodels = 0
    for shape in componentDetail["packageDetail"]["dataStr"]["shape"]:
        if not shape.startswith("SVGNODE"):
            continue
        m = re.search(r'"uuid":"([0-9a-f]*)"', shape)
        if not m:
            continue
        shapeUuid = m.group(1)
        res = requests.get(f"https://easyeda.com/analyzer/api/3dmodel/{shapeUuid}",
            headers=easyEdaHeaders(token), cookies=cookies,
            data={})
        packageName = getComponentPackageName(componentDetail)
        if submodels != 0:
            packageName += f"_model_{submodels}"
        objFile = os.path.join(lib3D, packageName + ".obj")
        wrlFile = os.path.join(lib3D, packageName + ".wrl")
        with open(objFile, "w") as f:
            f.write(res.text)
        subprocess.check_call(["ctmconv", objFile, wrlFile])

        desc = pcbnew.FP_3DMODEL()
        desc.m_Filename = "${" + pathvar + "}/" + wrlFile
        desc.m_Scale.x = desc.m_Scale.y = desc.m_Scale.z = 1 / 2.54
        desc.m_Rotation.z = 180
        models.append(desc)

        submodels += 1
    return models


@click.command()
@click.argument("LCSC")
@click.option("--kicadLib", type=click.Path(dir_okay=True, file_okay=False), required=True,
    help="Path to KiCAD library where to store the footprint")
@click.option("--force", is_flag=True,
    help="Overwrite footprint if it already exists in the library")
@click.option("--pathVar", type=str, default="EASY_EDA_3D",
    help="Name of variable, that will be used for prefixing 3D models paths")
def fetchLcsc(kicadlib, force, lcsc, pathvar):
    """
    Fetch a footprint based on LCSC code
    """
    token, cookies = obtainCsrfTokenAndCookies()

    validateLibName(kicadlib)
    ensureKicadLib(kicadlib)

    cinfo = getComponentInfo(lcsc, token, cookies)
    if cinfo is None:
        raise RuntimeError(f"No component was found for the code {lcsc}")
    packageName = getComponentPackageName(cinfo)

    if footprintExists(kicadlib, packageName) and not force:
        print(f"Component {lcsc} uses package {packageName} which already exists in {kicadlib}.")
        print(f"Nothing has been done. If you want to overwrite the package, run this command again with '--force'.")
        return

    componentDetail, footprint = fetchAndConvert(cinfo, token, cookies)
    models = fetchAndConvert3D(componentDetail, kicadlib, pathvar, token, cookies)
    for model in models:
        footprint.Add3DModel(model)

    pcbnew.FootprintSave(kicadlib, footprint)

@click.command()
@click.argument("name")
@click.option("--kicadLib", type=click.Path(dir_okay=True, file_okay=False), required=True,
    help="Path to KiCAD library where to store the footprint")
@click.option("--force",
    help="Overwrite footprint if it already exists in the library")
def fetchName(kicadlib, force, name):
    """
    Fetch a footprint based on full text search.
    """
    pass

@click.group()
def cli():
    """
    Tool for downloading KiCAD footprints from EasyEDA
    """
    pass

cli.add_command(fetchLcsc)
cli.add_command(fetchName)

if __name__ == "__main__":
    cli()
