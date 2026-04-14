# LabPBR to MERS Converter
[EN] | [[中文]](README_CN.md)  

A command-line tool for converting LabPBR material format to MERS format.

## Features

- Pixel-level conversion from LabPBR to MERS format
- Support for PNG/TGA output formats
- Automatic creation of output directories
- Batch processing support (via scripting)

## Build

```bash
#Install dependencies
pip install Pillow
#Build
python -m PyInstaller --onefile --name Lab2MERS --icon Lab2MERS.ico Lab2MERS.py
#The build result in the dist directory