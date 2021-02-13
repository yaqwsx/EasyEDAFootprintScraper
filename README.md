# EasyEDA Footprint Scraper for KiCAD

**The whole project is work-in-progress. There is no solid documentation and
everything might not work.**

## Prerequisites

- KiCAD
- [easyeda2kicad](https://github.com/wokwi/easyeda2kicad)
- [ctmconv](http://openctm.sourceforge.net/)
- Please read build instructions for the required LC2KiCad module in `./LC2KiCad/README.md`

## Trying it out

Just run:
```
./fetchComponent.py fetchlcsc --kicadLib test.pretty --force C558438
```

It will create a KiCAD library `test.pretty` and `test.3dshapes` in the working
directory. There will be a footprint for component C558438and a corresponding 3D
model. To actually view the 3D models in KiCAD, you have to configure a KiCAD
variable `EASY_EDA_3D` pointing to a directory with `test.3dshapes`.

## Known issues

- The script segfaults on exit - this is a bug in KiCAD (see
  [issue](https://gitlab.com/kicad/code/kicad/-/issues/6850))
- Materials of 3D models are not preserved
- Some LCSC code are not found
    - this is issue on the EasyEDA website
    - they seem to be working on direct search among LCSC codes, however, their
      page says it is under construction

## What needs to be done

- prepare a script for batch downloading (we can use data from [JLC
  Parts](https://yaqwsx.github.io/jlcparts/))
    - create a component table
    - cache existing entries
- possibly shorten the long EasyEDA footprint names
