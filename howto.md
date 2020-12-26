Given a search query (e.g., LCSC number) do POST request:

```
curl 'https://easyeda.com/api/components/search' \
  -H 'authority: easyeda.com' \
  -H 'pragma: no-cache' \
  -H 'cache-control: no-cache' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'origin: https://easyeda.com' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://easyeda.com/editor' \
  -H 'accept-language: cs,en;q=0.9,sk;q=0.8,en-GB;q=0.7' \
  -H 'cookie: <PUT your cookies here>' \
  --data-raw 'type=3&doctype%5B%5D=2&uid=0819f05c4eef4c71ace90d822a990e87&returnListStyle=classifyarr&wd=TPSM12T1G&version=6.4.7' \
  --compressed
  ```

It will return json with the list of found components:

```{.json}
{
    "success": true,
    "code": 0,
    "result": {
        "facets": {
            "mine": 0,
            "lcsc": 1,
            "SMT": 0,
            "easyeda": 0,
            "following": 0,
            "user": 0
        },
        "lists": {
            "lcsc": [
                {
                    "uuid": "559ac77b33524d978c56dd5ca7177ef7",
                    "title": "TPSM12T1G",
                    "description": "",
                    "description_cn": "",
                    "tags": [
                        "TVS"
                    ],
                    "type": 3,
                    "docType": 2,
                    "SMT": false,
                    "ownerUuid": "0819f05c4eef4c71ace90d822a990e87",
                    "dataStr": {
                        "head": {
                            "c_para": {
                                "pre": "D?",
                                "BOM_Supplier": "LCSC",
                                "package": "SOT-23-3_L2.9-W1.3-P1.90-LS2.4-BR",
                                "BOM_Manufacturer": "TECH PUBLIC",
                                "BOM_Manufacturer Part": "TPSM12T1G",
                                "Contributor": "LCSC",
                                "BOM_Supplier Part": "C558438",
                                "name": "TPSM12T1G"
                            },
                            "uuid": "559ac77b33524d978c56dd5ca7177ef7",
                            "c_spiceCmd": null,
                            "docType": "2",
                            "importFlag": 0,
                            "puuid": "4f7d32c395fb4911bd2391884cef30c8",
                            "hasIdFlag": true,
                            "utime": 1608703408
                        }
                    },
                    "lcsc": {
                        "min": 20,
                        "url": "https:\/\/lcsc.com\/product-detail\/TVS_TECH-PUBLIC-TPSM12T1G_C558438.html",
                        "price": 0.026554,
                        "number": "C558438",
                        "step": 20,
                        "id": 581845,
                        "stock": 400
                    },
                    "szlcsc": {
                        "url": "http:\/\/www.szlcsc.com\/product\/details_581845.html",
                        "price": 0.166913,
                        "number": "C558438",
                        "step": 20,
                        "min": 20
                    },
                    "subparts": [],
                    "verify": true,
                    "owner": {
                        "username": "LCSC",
                        "nickname": "LCSC",
                        "uuid": "0819f05c4eef4c71ace90d822a990e87",
                        "avatar": "\/\/image.lceda.cn\/avatars\/2018\/6\/kFlrasi7W06gTdBLAqW3fkrqbDhbowynuSzkjqso.png"
                    }
                }
            ],
            "easyeda": [],
            "mine": [],
            "following": [],
            "user": [],
            "SMT": []
        },
        "pageSize": 100,
        "totalPage": 1,
        "wd": "tpsm12t1g",
        "uid": "0819f05c4eef4c71ace90d822a990e87",
        "type": "3",
        "doctype": [
            "2"
        ]
    }
}
```

Find component UUID and make GET request to `https://easyeda.com/api/components/<UUID>?version=6.4.7&uuid=<UUID>&datastrid='; e.g.:

```
curl 'https://easyeda.com/api/components/559ac77b33524d978c56dd5ca7177ef7?version=6.4.7&uuid=559ac77b33524d978c56dd5ca7177ef7&datastrid=' \
  -H 'authority: easyeda.com' \
  -H 'pragma: no-cache' \
  -H 'cache-control: no-cache' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://easyeda.com/editor' \
  -H 'accept-language: cs,en;q=0.9,sk;q=0.8,en-GB;q=0.7' \
  -H 'cookie: <PUT your cookies here>' \
  --compressed
```

Yout get JSON:
```{.json}
{
    "success": true,
    "code": 0,
    "result": {
        "uuid": "559ac77b33524d978c56dd5ca7177ef7",
        "title": "TPSM12T1G",
        "description": "",
        "docType": 2,
        "type": 3,
        "lcsc": {
            "id": 581845,
            "number": "C558438",
            "step": 20,
            "min": 20,
            "price": 0.026554,
            "stock": 400,
            "url": "https:\/\/lcsc.com\/product-detail\/TVS_TECH-PUBLIC-TPSM12T1G_C558438.html"
        },
        "szlcsc": {
            "id": 581845,
            "number": "C558438",
            "step": 20,
            "min": 20,
            "price": 0.166913,
            "stock": 3680,
            "url": "http:\/\/www.szlcsc.com\/product\/details_581845.html"
        },
        "owner": {
            "uuid": "0819f05c4eef4c71ace90d822a990e87",
            "username": "LCSC",
            "nickname": "LCSC",
            "avatar": "\/\/image.lceda.cn\/avatars\/2018\/6\/kFlrasi7W06gTdBLAqW3fkrqbDhbowynuSzkjqso.png"
        },
        "tags": [
            "TVS"
        ],
        "updateTime": 1608703408,
        "updated_at": "2020-12-23 06:05:03",
        "dataStr": {
            "head": {
                "docType": "2",
                "editorVersion": "6.4.10",
                "x": 400,
                "y": 300,
                "c_para": {
                    "pre": "D?",
                    "name": "TPSM12T1G",
                    "package": "SOT-23-3_L2.9-W1.3-P1.90-LS2.4-BR",
                    "BOM_Supplier": "LCSC",
                    "BOM_Supplier Part": "C558438",
                    "BOM_Manufacturer": "TECH PUBLIC",
                    "BOM_Manufacturer Part": "TPSM12T1G",
                    "Contributor": "LCSC"
                },
                "uuid": "559ac77b33524d978c56dd5ca7177ef7",
                "puuid": "4f7d32c395fb4911bd2391884cef30c8",
                "importFlag": 0,
                "c_spiceCmd": null,
                "hasIdFlag": true,
                "utime": 1608703408
            },
            "canvas": "CA~1000~1000~#FFFFFF~yes~#CCCCCC~10~1000~1000~line~10~pixel~5~400~300",
            "shape": [
                "PL~414 301 410 305 410 315 406 319~#880000~1~0~none~gge3~0",
                "PT~M 400 316 L 410 310 L 400 303 Z ~#880000~1~0~none~gge4~0~",
                "PL~414 281 410 285 410 295 406 299~#880000~1~0~none~gge5~0",
                "PT~M 400 296 L 410 290 L 400 283 Z ~#880000~1~0~none~gge6~0~",
                "P~show~0~3~380~300~180~gge7~0^^380~300^^M 380 300 h 10~#8D2323^^0~393~303~0~A~start~~~#8D2323^^0~389~299~0~3~end~~~#8D2323^^0~387~300^^0~M 390 303 L 393 300 L 390 297",
                "PL~400 290 390 290 390 310 400 310 398 310~#880000~1~0~none~gge14~0",
                "P~show~0~1~420~310~0~gge15~0^^420~310^^M 420 310 h -10~#8D2323^^0~407~313~0~C~end~~~#8D2323^^0~411~309~0~1~start~~~#8D2323^^0~413~310^^0~M 410 307 L 407 310 L 410 313",
                "P~show~0~2~420~290~0~gge22~0^^420~290^^M 420 290 h -10~#8D2323^^0~407~293~0~C~end~~~#8D2323^^0~411~289~0~2~start~~~#8D2323^^0~413~290^^0~M 410 287 L 407 290 L 410 293"
            ],
            "BBox": {
                "x": 379,
                "y": 281,
                "width": 42,
                "height": 38
            },
            "colors": []
        },
        "verify": true,
        "writable": false,
        "isFavorite": false,
        "packageDetail": {
            "uuid": "4f7d32c395fb4911bd2391884cef30c8",
            "title": "SOT-23-3_L2.9-W1.3-P1.90-LS2.4-BR",
            "docType": 4,
            "updateTime": 1584090987,
            "writable": false,
            "dataStr": {
                "head": {
                    "docType": "4",
                    "editorVersion": "6.3.27",
                    "c_para": {
                        "pre": "U?",
                        "package": "SOT-23-3_L2.9-W1.3-P1.90-LS2.4-BR",
                        "link": "https:\/\/item.szlcsc.com\/9070.html",
                        "Contributor": "\u7acb\u521bEDA\u5b98\u65b9\u5c01\u88c5\u5e93",
                        "3DModel": "SOT-23-3P_L2.9-W1.3-H1.0-LS2.4-P0.95"
                    },
                    "x": 608,
                    "y": -320,
                    "uuid": "4f7d32c395fb4911bd2391884cef30c8",
                    "utime": 1584090983,
                    "importFlag": 0,
                    "transformList": "",
                    "hasIdFlag": true,
                    "newgId": true
                },
                "canvas": "CA~1000~1000~#000000~yes~~10~1000~1000~line~10~mm~1~45~visible~0.1~608~-320~0~yes",
                "shape": [
                    "TRACK~1~3~~608.65 -314.252 605.441 -314.252 605.441 -316.85~gge17~0",
                    "TRACK~1~3~~605.441 -323.15 605.441 -325.748 605.441 -323.15 605.441 -325.748 608.65 -325.748~gge18~0",
                    "TRACK~0.7874~3~~611.543 -318.819 611.543 -321.181~gge16~0",
                    "PAD~RECT~603.08~-320~2.7559~4.9213~1~~3~0~605.5406 -321.378 605.5406 -318.622 600.6194 -318.622 600.6194 -321.378~270~rep2~0~~Y~0~0~0.4~603.08,-320",
                    "PAD~RECT~612.92~-323.74~2.7559~4.9213~1~~2~0~615.3806 -325.118 615.3806 -322.362 610.4594 -322.362 610.4594 -325.118~270~rep3~0~~Y~0~0~0.4~612.92,-323.74",
                    "PAD~RECT~612.92~-316.26~2.7559~4.9213~1~~1~0~615.3806 -317.638 615.3806 -314.882 610.4594 -314.882 610.4594 -317.638~270~rep4~0~~Y~0~0~0.4~612.92,-316.26",
                    "SVGNODE~{\"gId\":\"g1_outline\",\"nodeName\":\"g\",\"nodeType\":1,\"layerid\":\"19\",\"attrs\":{\"c_width\":\"9.8425\",\"c_height\":\"11.4173\",\"c_rotation\":\"0,0,180\",\"z\":\"0\",\"c_origin\":\"608,-320\",\"uuid\":\"d777607a152f4f3aac9bb0d0c14ed6fd\",\"c_etype\":\"outline3D\",\"id\":\"g1_outline\",\"title\":\"SOT-23-3P_L2.9-W1.3-H1.0-LS2.4-P0.95\",\"layerid\":\"19\",\"transform\":\"scale(1) translate(-0.0012, 0.0006)\"},\"childNodes\":[{\"gId\":\"g1_outline_line0\",\"nodeName\":\"polyline\",\"nodeType\":1,\"attrs\":{\"fill\":\"none\",\"id\":\"g1_outline_line0\",\"c_shapetype\":\"line\",\"points\":\"612.9213 -315.4724 612.9213 -315.5117 612.9213 -316.2598 612.9213 -317.0078 612.9213 -317.0472 612.8819 -317.0472 612.5276 -317.0472 612.4882 -317.0472 612.4488 -317.0472 612.4094 -317.0472 612.3701 -317.0472 612.2913 -317.0472 612.252 -317.0472 612.2126 -317.0472 612.1732 -317.0472 612.1339 -317.0472 612.0945 -317.0472 612.0551 -317.0472 612.0157 -317.0472 611.937 -317.0472 611.8976 -317.0472 611.8583 -317.0472 611.8189 -317.0472 611.7402 -317.0472 611.7008 -317.0472 611.6614 -317.0472 611.622 -317.0472 611.5827 -317.0472 611.5433 -317.0472 611.5039 -317.0472 611.4646 -317.0472 611.3858 -317.0472 611.3465 -317.0472 611.2677 -317.0472 611.2283 -317.0472 611.189 -317.0472 611.1496 -317.0472 611.1102 -317.0472 611.0709 -317.0472 610.9921 -317.0472 610.9528 -317.0472 610.9134 -317.0472 610.874 -317.0472 610.7953 -317.0472 610.5591 -317.0472 610.5591 -322.9527 610.7953 -322.9527 610.874 -322.9527 610.9134 -322.9527 610.9528 -322.9527 610.9921 -322.9527 611.0709 -322.9527 611.1102 -322.9527 611.1496 -322.9527 611.189 -322.9527 611.2283 -322.9527 611.3071 -322.9527 611.3465 -322.9527 611.3858 -322.9527 611.4252 -322.9527 611.4646 -322.9527 611.5039 -322.9527 611.5433 -322.9527 611.5827 -322.9527 611.622 -322.9527 611.6614 -322.9527 611.7008 -322.9527 611.7795 -322.9527 611.8189 -322.9527 611.8583 -322.9527 611.8976 -322.9527 611.937 -322.9527 611.9764 -322.9527 612.0157 -322.9527 612.0551 -322.9527 612.0945 -322.9527 612.1339 -322.9527 612.1732 -322.9527 612.2126 -322.9527 612.252 -322.9527 612.2913 -322.9527 612.3701 -322.9527 612.4094 -322.9527 612.4488 -322.9527 612.4882 -322.9527 612.5669 -322.9527 612.8819 -322.9527 612.9213 -322.9527 612.9213 -322.992 612.9213 -323.7401 612.9213 -324.4881 612.9213 -324.5275 612.8819 -324.5275 612.5276 -324.5275 612.4882 -324.5275 612.4488 -324.5275 612.4094 -324.5275 612.3701 -324.5275 612.3307 -324.5275 612.2913 -324.5275 612.252 -324.5275 612.2126 -324.5275 612.1732 -324.5275 612.1339 -324.5275 612.0945 -324.5275 612.0551 -324.5275 612.0157 -324.5275 611.9764 -324.5275 611.937 -324.5275 611.8976 -324.5275 611.8583 -324.5275 611.8189 -324.5275 611.7402 -324.5275 611.7008 -324.5275 611.6614 -324.5275 611.622 -324.5275 611.5827 -324.5275 611.5433 -324.5275 611.5039 -324.5275 611.4646 -324.5275 611.3858 -324.5275 611.3465 -324.5275 611.2677 -324.5275 611.2283 -324.5275 611.189 -324.5275 611.1496 -324.5275 611.1102 -324.5275 611.0709 -324.5275 610.9921 -324.5275 610.9528 -324.5275 610.9134 -324.5275 610.874 -324.5275 610.7953 -324.5275 610.5591 -324.5275 610.5591 -325.5511 610.5197 -325.5904 610.5197 -325.6298 610.5197 -325.6692 610.4803 -325.6692 610.4409 -325.6692 610.4016 -325.7086 610.3622 -325.7086 605.6378 -325.7086 605.5984 -325.7086 605.5591 -325.6692 605.5197 -325.6692 605.4803 -325.6692 605.4803 -325.6298 605.4803 -325.5904 605.441 -325.5117 605.441 -320.7873 605.2047 -320.7873 605.126 -320.7873 605.0866 -320.7873 605.0473 -320.7873 605.0079 -320.7873 604.9291 -320.7873 604.8898 -320.7873 604.8504 -320.7873 604.811 -320.7873 604.7717 -320.7873 604.6929 -320.7873 604.6536 -320.7873 604.6142 -320.7873 604.5748 -320.7873 604.5354 -320.7873 604.4961 -320.7873 604.4567 -320.7873 604.4173 -320.7873 604.378 -320.7873 604.3386 -320.7873 604.2992 -320.7873 604.2205 -320.7873 604.1811 -320.7873 604.1417 -320.7873 604.1024 -320.7873 604.063 -320.7873 604.0236 -320.7873 603.9843 -320.7873 603.9449 -320.7873 603.9055 -320.7873 603.8662 -320.7873 603.8268 -320.7873 603.7874 -320.7873 603.748 -320.7873 603.7087 -320.7873 603.6299 -320.7873 603.5906 -320.7873 603.5512 -320.7873 603.5118 -320.7873 603.4331 -320.7873 603.1181 -320.7873 603.0788 -320.7873 603.0788 -320.7479 603.0788 -319.9999 603.0788 -319.2519 603.0788 -319.2125 603.1181 -319.2125 603.4725 -319.2125 603.5118 -319.2125 603.5512 -319.2125 603.5906 -319.2125 603.6299 -319.2125 603.6693 -319.2125 603.7087 -319.2125 603.748 -319.2125 603.7874 -319.2125 603.8268 -319.2125 603.8662 -319.2125 603.9055 -319.2125 603.9449 -319.2125 603.9843 -319.2125 604.0236 -319.2125 604.063 -319.2125 604.1024 -319.2125 604.1417 -319.2125 604.1811 -319.2125 604.2599 -319.2125 604.2992 -319.2125 604.3386 -319.2125 604.378 -319.2125 604.4173 -319.2125 604.4567 -319.2125 604.4961 -319.2125 604.5354 -319.2125 604.5748 -319.2125 604.6142 -319.2125 604.6536 -319.2125 604.7323 -319.2125 604.7717 -319.2125 604.811 -319.2125 604.8504 -319.2125 604.8898 -319.2125 604.9291 -319.2125 605.0079 -319.2125 605.0473 -319.2125 605.0866 -319.2125 605.126 -319.2125 605.2047 -319.2125 605.441 -319.2125 605.441 -314.4487 605.4803 -314.4094 605.4803 -314.37 605.4803 -314.3306 605.5197 -314.3306 605.5591 -314.3306 605.5984 -314.2913 605.6378 -314.2913 610.3622 -314.2913 610.4016 -314.2913 610.4409 -314.3306 610.4803 -314.3306 610.5197 -314.3306 610.5197 -314.37 610.5197 -314.4094 610.5591 -314.4881 610.5591 -315.4724 610.7953 -315.4724 610.8346 -315.4724 610.874 -315.4724 610.9134 -315.4724 610.9528 -315.4724 610.9921 -315.4724 611.0709 -315.4724 611.1102 -315.4724 611.1496 -315.4724 611.189 -315.4724 611.2283 -315.4724 611.3071 -315.4724 611.3465 -315.4724 611.3858 -315.4724 611.4252 -315.4724 611.4646 -315.4724 611.5039 -315.4724 611.5433 -315.4724 611.5827 -315.4724 611.622 -315.4724 611.6614 -315.4724 611.7008 -315.4724 611.7795 -315.4724 611.8189 -315.4724 611.8583 -315.4724 611.8976 -315.4724 611.937 -315.4724 611.9764 -315.4724 612.0157 -315.4724 612.0551 -315.4724 612.0945 -315.4724 612.1339 -315.4724 612.1732 -315.4724 612.2126 -315.4724 612.252 -315.4724 612.2913 -315.4724 612.3701 -315.4724 612.4094 -315.4724 612.4488 -315.4724 612.4882 -315.4724 612.5669 -315.4724 612.8819 -315.4724 612.9213 -315.4724 612.9213 -315.4724\"}}]}"
                ],
                "layers": [
                    "1~TopLayer~#FF0000~true~true~true~",
                    "2~BottomLayer~#0000FF~true~false~true~",
                    "3~TopSilkLayer~#FFFF00~true~false~true~",
                    "4~BottomSilkLayer~#808000~true~false~true~",
                    "5~TopPasteMaskLayer~#808080~true~false~true~",
                    "6~BottomPasteMaskLayer~#800000~true~false~true~",
                    "7~TopSolderMaskLayer~#800080~true~false~true~",
                    "8~BottomSolderMaskLayer~#AA00FF~true~false~true~",
                    "9~Ratlines~#6464FF~false~false~true~",
                    "10~BoardOutline~#FF00FF~true~false~true~",
                    "11~Multi-Layer~#C0C0C0~true~false~true~",
                    "12~Document~#FFFFFF~true~false~true~",
                    "13~TopAssembly~#33CC99~false~false~false~",
                    "14~BottomAssembly~#5555FF~false~false~false~",
                    "15~Mechanical~#F022F0~false~false~false~",
                    "19~3DModel~#66CCFF~false~false~false~",
                    "21~Inner1~#800000~false~false~false~~",
                    "22~Inner2~#008000~false~false~false~~",
                    "23~Inner3~#00FF00~false~false~false~~",
                    "24~Inner4~#000080~false~false~false~~",
                    "25~Inner5~#70DBFA~false~false~false~~",
                    "26~Inner6~#00CC66~false~false~false~~",
                    "27~Inner7~#9966FF~false~false~false~~",
                    "28~Inner8~#800080~false~false~false~~",
                    "29~Inner9~#008080~false~false~false~~",
                    "30~Inner10~#15935F~false~false~false~~",
                    "31~Inner11~#000080~false~false~false~~",
                    "32~Inner12~#00B400~false~false~false~~",
                    "33~Inner13~#2E4756~false~false~false~~",
                    "34~Inner14~#99842F~false~false~false~~",
                    "35~Inner15~#FFFFAA~false~false~false~~",
                    "36~Inner16~#99842F~false~false~false~~",
                    "37~Inner17~#2E4756~false~false~false~~",
                    "38~Inner18~#3535FF~false~false~false~~",
                    "39~Inner19~#8000BC~false~false~false~~",
                    "40~Inner20~#43AE5F~false~false~false~~",
                    "41~Inner21~#C3ECCE~false~false~false~~",
                    "42~Inner22~#728978~false~false~false~~",
                    "43~Inner23~#39503F~false~false~false~~",
                    "44~Inner24~#0C715D~false~false~false~~",
                    "45~Inner25~#5A8A80~false~false~false~~",
                    "46~Inner26~#2B937E~false~false~false~~",
                    "47~Inner27~#23999D~false~false~false~~",
                    "48~Inner28~#45B4E3~false~false~false~~",
                    "49~Inner29~#215DA1~false~false~false~~",
                    "50~Inner30~#4564D7~false~false~false~~",
                    "51~Inner31~#6969E9~false~false~false~~",
                    "52~Inner32~#9069E9~false~false~false~~",
                    "99~ComponentShapeLayer~#00CCCC~false~false~false~",
                    "100~LeadShapeLayer~#CC9999~false~false~false~",
                    "Hole~Hole~#000000~~false~true~",
                    "DRCError~DRCError~#FFFFFF~~false~true~"
                ],
                "objects": [
                    "All~true~false",
                    "Component~true~true",
                    "Prefix~true~true",
                    "Name~true~false",
                    "Track~true~true",
                    "Pad~true~true",
                    "Via~true~true",
                    "Hole~true~true",
                    "Copper_Area~true~true",
                    "Circle~true~true",
                    "Arc~true~true",
                    "Solid_Region~true~true",
                    "Text~true~true",
                    "Image~true~true",
                    "Rect~true~true",
                    "Dimension~true~true",
                    "Protractor~true~true"
                ],
                "BBox": {
                    "x": 600.6,
                    "y": -325.7,
                    "width": 14.8,
                    "height": 11.5
                },
                "netColors": []
            }
        }
    }
}
```

Create a fake board; board a JSON dictionary. Use the following header:
```{.json}
"head": {
    "docType": "3",
    "editorVersion": "6.4.7",
    "newgId": true,
    "c_para": {},
    "hasIdFlag": true
}
```
Then copy `BBox`, `objects`, `layers` from `packageDetail.dataStr` from the JSON
you requested before. We also have to create a key `shape`; this will be created
by the following procedure (see
[Documentation](https://docs.easyeda.com/en/DocumentFormat/3-EasyEDA-PCB-File-Format/index.html#Footprint)
for details):

- take template ``LIB~<x>~<y>~package`<package_name>`~0~~~1`` and replace `<x>` with `dataStr.head.x` from the previous JSON. Similarly for `<y>`. Also replace `<package_name>` with the package name.
- append to the template all the lines from `shape` from the footprint JSON a
  join them with `#@$`.

You should get the following JSON:

```{.json}
{
"head": {
    "docType": "3",
    "editorVersion": "6.4.7",
    "newgId": true,
    "c_para": {},
    "hasIdFlag": true
},
"canvas": "CA~1000~1000~#000000~yes~~10~1000~1000~line~10~mm~1~45~visible~0.1~608~-320~0~yes",
"shape": [
    "LIB~608~-320~package`CK17-B`~0~~gge15~1#@$TRACK~1~3~~608.65 -314.252 605.441 -314.252 605.441 -316.85~gge17~0#@$TRACK~1~3~~605.441 -323.15 605.441 -325.748 605.441 -323.15 605.441 -325.748 608.65 -325.748~gge18~0#@$TRACK~0.7874~3~~611.543 -318.819 611.543 -321.181~gge16~0#@$PAD~RECT~603.08~-320~2.7559~4.9213~1~~3~0~605.5406 -321.378 605.5406 -318.622 600.6194 -318.622 600.6194 -321.378~270~rep2~0~~Y~0~0~0.4~603.08,-320#@$PAD~RECT~612.92~-323.74~2.7559~4.9213~1~~2~0~615.3806 -325.118 615.3806 -322.362 610.4594 -322.362 610.4594 -325.118~270~rep3~0~~Y~0~0~0.4~612.92,-323.74#@$PAD~RECT~612.92~-316.26~2.7559~4.9213~1~~1~0~615.3806 -317.638 615.3806 -314.882 610.4594 -314.882 610.4594 -317.638~270~rep4~0~~Y~0~0~0.4~612.92,-316.26#@$SVGNODE~{\"gId\":\"g1_outline\",\"nodeName\":\"g\",\"nodeType\":1,\"layerid\":\"19\",\"attrs\":{\"c_width\":\"9.8425\",\"c_height\":\"11.4173\",\"c_rotation\":\"0,0,180\",\"z\":\"0\",\"c_origin\":\"608,-320\",\"uuid\":\"d777607a152f4f3aac9bb0d0c14ed6fd\",\"c_etype\":\"outline3D\",\"id\":\"g1_outline\",\"title\":\"SOT-23-3P_L2.9-W1.3-H1.0-LS2.4-P0.95\",\"layerid\":\"19\",\"transform\":\"scale(1) translate(-0.0012, 0.0006)\"},\"childNodes\":[{\"gId\":\"g1_outline_line0\",\"nodeName\":\"polyline\",\"nodeType\":1,\"attrs\":{\"fill\":\"none\",\"id\":\"g1_outline_line0\",\"c_shapetype\":\"line\",\"points\":\"612.9213 -315.4724 612.9213 -315.5117 612.9213 -316.2598 612.9213 -317.0078 612.9213 -317.0472 612.8819 -317.0472 612.5276 -317.0472 612.4882 -317.0472 612.4488 -317.0472 612.4094 -317.0472 612.3701 -317.0472 612.2913 -317.0472 612.252 -317.0472 612.2126 -317.0472 612.1732 -317.0472 612.1339 -317.0472 612.0945 -317.0472 612.0551 -317.0472 612.0157 -317.0472 611.937 -317.0472 611.8976 -317.0472 611.8583 -317.0472 611.8189 -317.0472 611.7402 -317.0472 611.7008 -317.0472 611.6614 -317.0472 611.622 -317.0472 611.5827 -317.0472 611.5433 -317.0472 611.5039 -317.0472 611.4646 -317.0472 611.3858 -317.0472 611.3465 -317.0472 611.2677 -317.0472 611.2283 -317.0472 611.189 -317.0472 611.1496 -317.0472 611.1102 -317.0472 611.0709 -317.0472 610.9921 -317.0472 610.9528 -317.0472 610.9134 -317.0472 610.874 -317.0472 610.7953 -317.0472 610.5591 -317.0472 610.5591 -322.9527 610.7953 -322.9527 610.874 -322.9527 610.9134 -322.9527 610.9528 -322.9527 610.9921 -322.9527 611.0709 -322.9527 611.1102 -322.9527 611.1496 -322.9527 611.189 -322.9527 611.2283 -322.9527 611.3071 -322.9527 611.3465 -322.9527 611.3858 -322.9527 611.4252 -322.9527 611.4646 -322.9527 611.5039 -322.9527 611.5433 -322.9527 611.5827 -322.9527 611.622 -322.9527 611.6614 -322.9527 611.7008 -322.9527 611.7795 -322.9527 611.8189 -322.9527 611.8583 -322.9527 611.8976 -322.9527 611.937 -322.9527 611.9764 -322.9527 612.0157 -322.9527 612.0551 -322.9527 612.0945 -322.9527 612.1339 -322.9527 612.1732 -322.9527 612.2126 -322.9527 612.252 -322.9527 612.2913 -322.9527 612.3701 -322.9527 612.4094 -322.9527 612.4488 -322.9527 612.4882 -322.9527 612.5669 -322.9527 612.8819 -322.9527 612.9213 -322.9527 612.9213 -322.992 612.9213 -323.7401 612.9213 -324.4881 612.9213 -324.5275 612.8819 -324.5275 612.5276 -324.5275 612.4882 -324.5275 612.4488 -324.5275 612.4094 -324.5275 612.3701 -324.5275 612.3307 -324.5275 612.2913 -324.5275 612.252 -324.5275 612.2126 -324.5275 612.1732 -324.5275 612.1339 -324.5275 612.0945 -324.5275 612.0551 -324.5275 612.0157 -324.5275 611.9764 -324.5275 611.937 -324.5275 611.8976 -324.5275 611.8583 -324.5275 611.8189 -324.5275 611.7402 -324.5275 611.7008 -324.5275 611.6614 -324.5275 611.622 -324.5275 611.5827 -324.5275 611.5433 -324.5275 611.5039 -324.5275 611.4646 -324.5275 611.3858 -324.5275 611.3465 -324.5275 611.2677 -324.5275 611.2283 -324.5275 611.189 -324.5275 611.1496 -324.5275 611.1102 -324.5275 611.0709 -324.5275 610.9921 -324.5275 610.9528 -324.5275 610.9134 -324.5275 610.874 -324.5275 610.7953 -324.5275 610.5591 -324.5275 610.5591 -325.5511 610.5197 -325.5904 610.5197 -325.6298 610.5197 -325.6692 610.4803 -325.6692 610.4409 -325.6692 610.4016 -325.7086 610.3622 -325.7086 605.6378 -325.7086 605.5984 -325.7086 605.5591 -325.6692 605.5197 -325.6692 605.4803 -325.6692 605.4803 -325.6298 605.4803 -325.5904 605.441 -325.5117 605.441 -320.7873 605.2047 -320.7873 605.126 -320.7873 605.0866 -320.7873 605.0473 -320.7873 605.0079 -320.7873 604.9291 -320.7873 604.8898 -320.7873 604.8504 -320.7873 604.811 -320.7873 604.7717 -320.7873 604.6929 -320.7873 604.6536 -320.7873 604.6142 -320.7873 604.5748 -320.7873 604.5354 -320.7873 604.4961 -320.7873 604.4567 -320.7873 604.4173 -320.7873 604.378 -320.7873 604.3386 -320.7873 604.2992 -320.7873 604.2205 -320.7873 604.1811 -320.7873 604.1417 -320.7873 604.1024 -320.7873 604.063 -320.7873 604.0236 -320.7873 603.9843 -320.7873 603.9449 -320.7873 603.9055 -320.7873 603.8662 -320.7873 603.8268 -320.7873 603.7874 -320.7873 603.748 -320.7873 603.7087 -320.7873 603.6299 -320.7873 603.5906 -320.7873 603.5512 -320.7873 603.5118 -320.7873 603.4331 -320.7873 603.1181 -320.7873 603.0788 -320.7873 603.0788 -320.7479 603.0788 -319.9999 603.0788 -319.2519 603.0788 -319.2125 603.1181 -319.2125 603.4725 -319.2125 603.5118 -319.2125 603.5512 -319.2125 603.5906 -319.2125 603.6299 -319.2125 603.6693 -319.2125 603.7087 -319.2125 603.748 -319.2125 603.7874 -319.2125 603.8268 -319.2125 603.8662 -319.2125 603.9055 -319.2125 603.9449 -319.2125 603.9843 -319.2125 604.0236 -319.2125 604.063 -319.2125 604.1024 -319.2125 604.1417 -319.2125 604.1811 -319.2125 604.2599 -319.2125 604.2992 -319.2125 604.3386 -319.2125 604.378 -319.2125 604.4173 -319.2125 604.4567 -319.2125 604.4961 -319.2125 604.5354 -319.2125 604.5748 -319.2125 604.6142 -319.2125 604.6536 -319.2125 604.7323 -319.2125 604.7717 -319.2125 604.811 -319.2125 604.8504 -319.2125 604.8898 -319.2125 604.9291 -319.2125 605.0079 -319.2125 605.0473 -319.2125 605.0866 -319.2125 605.126 -319.2125 605.2047 -319.2125 605.441 -319.2125 605.441 -314.4487 605.4803 -314.4094 605.4803 -314.37 605.4803 -314.3306 605.5197 -314.3306 605.5591 -314.3306 605.5984 -314.2913 605.6378 -314.2913 610.3622 -314.2913 610.4016 -314.2913 610.4409 -314.3306 610.4803 -314.3306 610.5197 -314.3306 610.5197 -314.37 610.5197 -314.4094 610.5591 -314.4881 610.5591 -315.4724 610.7953 -315.4724 610.8346 -315.4724 610.874 -315.4724 610.9134 -315.4724 610.9528 -315.4724 610.9921 -315.4724 611.0709 -315.4724 611.1102 -315.4724 611.1496 -315.4724 611.189 -315.4724 611.2283 -315.4724 611.3071 -315.4724 611.3465 -315.4724 611.3858 -315.4724 611.4252 -315.4724 611.4646 -315.4724 611.5039 -315.4724 611.5433 -315.4724 611.5827 -315.4724 611.622 -315.4724 611.6614 -315.4724 611.7008 -315.4724 611.7795 -315.4724 611.8189 -315.4724 611.8583 -315.4724 611.8976 -315.4724 611.937 -315.4724 611.9764 -315.4724 612.0157 -315.4724 612.0551 -315.4724 612.0945 -315.4724 612.1339 -315.4724 612.1732 -315.4724 612.2126 -315.4724 612.252 -315.4724 612.2913 -315.4724 612.3701 -315.4724 612.4094 -315.4724 612.4488 -315.4724 612.4882 -315.4724 612.5669 -315.4724 612.8819 -315.4724 612.9213 -315.4724 612.9213 -315.4724\"}}]}"
],
"layers": [
    "1~TopLayer~#FF0000~true~true~true~",
    "2~BottomLayer~#0000FF~true~false~true~",
    "3~TopSilkLayer~#FFFF00~true~false~true~",
    "4~BottomSilkLayer~#808000~true~false~true~",
    "5~TopPasteMaskLayer~#808080~true~false~true~",
    "6~BottomPasteMaskLayer~#800000~true~false~true~",
    "7~TopSolderMaskLayer~#800080~true~false~true~",
    "8~BottomSolderMaskLayer~#AA00FF~true~false~true~",
    "9~Ratlines~#6464FF~false~false~true~",
    "10~BoardOutline~#FF00FF~true~false~true~",
    "11~Multi-Layer~#C0C0C0~true~false~true~",
    "12~Document~#FFFFFF~true~false~true~",
    "13~TopAssembly~#33CC99~false~false~false~",
    "14~BottomAssembly~#5555FF~false~false~false~",
    "15~Mechanical~#F022F0~false~false~false~",
    "19~3DModel~#66CCFF~false~false~false~",
    "21~Inner1~#800000~false~false~false~~",
    "22~Inner2~#008000~false~false~false~~",
    "23~Inner3~#00FF00~false~false~false~~",
    "24~Inner4~#000080~false~false~false~~",
    "25~Inner5~#70DBFA~false~false~false~~",
    "26~Inner6~#00CC66~false~false~false~~",
    "27~Inner7~#9966FF~false~false~false~~",
    "28~Inner8~#800080~false~false~false~~",
    "29~Inner9~#008080~false~false~false~~",
    "30~Inner10~#15935F~false~false~false~~",
    "31~Inner11~#000080~false~false~false~~",
    "32~Inner12~#00B400~false~false~false~~",
    "33~Inner13~#2E4756~false~false~false~~",
    "34~Inner14~#99842F~false~false~false~~",
    "35~Inner15~#FFFFAA~false~false~false~~",
    "36~Inner16~#99842F~false~false~false~~",
    "37~Inner17~#2E4756~false~false~false~~",
    "38~Inner18~#3535FF~false~false~false~~",
    "39~Inner19~#8000BC~false~false~false~~",
    "40~Inner20~#43AE5F~false~false~false~~",
    "41~Inner21~#C3ECCE~false~false~false~~",
    "42~Inner22~#728978~false~false~false~~",
    "43~Inner23~#39503F~false~false~false~~",
    "44~Inner24~#0C715D~false~false~false~~",
    "45~Inner25~#5A8A80~false~false~false~~",
    "46~Inner26~#2B937E~false~false~false~~",
    "47~Inner27~#23999D~false~false~false~~",
    "48~Inner28~#45B4E3~false~false~false~~",
    "49~Inner29~#215DA1~false~false~false~~",
    "50~Inner30~#4564D7~false~false~false~~",
    "51~Inner31~#6969E9~false~false~false~~",
    "52~Inner32~#9069E9~false~false~false~~",
    "99~ComponentShapeLayer~#00CCCC~false~false~false~",
    "100~LeadShapeLayer~#CC9999~false~false~false~",
    "Hole~Hole~#000000~~false~true~",
    "DRCError~DRCError~#FFFFFF~~false~true~"
],
"objects": [
    "All~true~false",
    "Component~true~true",
    "Prefix~true~true",
    "Name~true~false",
    "Track~true~true",
    "Pad~true~true",
    "Via~true~true",
    "Hole~true~true",
    "Copper_Area~true~true",
    "Circle~true~true",
    "Arc~true~true",
    "Solid_Region~true~true",
    "Text~true~true",
    "Image~true~true",
    "Rect~true~true",
    "Dimension~true~true",
    "Protractor~true~true"
],
"BBox": {
    "x": 600.6,
    "y": -325.7,
    "width": 14.8,
    "height": 11.5
},
"netColors": []
}
```

Run [`easyeda2kicad`](https://github.com/wokwi/easyeda2kicad) to get KiCAD
board. Use KiCAD Python API to extract the footprint into a footprint library.

Finito.

The 3D models are fetched by the following requests:

```
curl 'https://easyeda.com/analyzer/api/3dmodel/d777607a152f4f3aac9bb0d0c14ed6fd' \
  -H 'authority: easyeda.com' \
  -H 'pragma: no-cache' \
  -H 'cache-control: no-cache' \
  -H 'accept: text/plain, */*; q=0.01' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://easyeda.com/editor/6.4.7/htm/editorpage15.html' \
  -H 'accept-language: cs,en;q=0.9,sk;q=0.8,en-GB;q=0.7' \
  -H 'cookie: <PUT your cookies here>' \
  --compressed
```

Where `d777607a152f4f3aac9bb0d0c14ed6fd` is UUID hidden inside the `SVGNODE` shape of the footprint. The GET request returns the `.obj` 3D model.