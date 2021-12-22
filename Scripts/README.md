# Python Scripts of Translation Toolkit

Copyright (c) 2021 Ichihito Ohi

## Main Purposes
### Yaml_to_csv
These scripts extract the source texts for translation and output them with the metadata of folder path, file name, and ID into a csv file.

### Csv_to_yaml
This script copy the yaml files and overwrite source texts with the translation texts according to the csv file.

### Csv_to_ConfigEdits
This script makes the config edit files for the official modding system according to the csv file of translation list.


## Requirements
- Python 3.7 (Not verified with other versions.)
- Editor
    - *(Official recommended)* Notepad++
- *(Recommended)* A virtual environment manager for Python;
    - Visual Studio 2019 Community
- *(Recommended)* CSV viewer;
    - Microsoft Office Excel

## How to Use

### Preparation
1. Install Python 3.7 .

1. Install modules in `requirements.txt` to your environment.

1. Clone this repository or download the scripts in your workspace.

1. Copy `.yaml` files from the game folder to your workspace.
    - The game folder (Windows, as default): `C:\Program Files\Epic Games\PhantomBrigade\Configs`
    - You don't need to copy all of those folders. For translation, part of the folders `Data`, `DataDecomposed`, and `Text` will be used.
    - Do not change the structure in the original folder.
    - *(Recommended)* Keep folder structures of copied files as same as origin. You have to overwrite the original files with the translated files later.


### Run
1. Open a `.py` script for each `.yaml` files which you want to extract the text elements with text editor.

1. Using editor, open a `.py` script for each `.yaml` files which you want to extract the text elements from.
    - `.yaml` files have several structures and different tags, so you need use the right script properly depending on the `.yaml` files.

1. Check *# TODO:* tag in the `.py` file and change the path of input file.
    - Be careful where you run python and where the `.yaml` file is.
        - *(Recommended)* Set as absolute path.
        - You can set as relative path, but it could be changed depending on environment.

1.  Run the script.
    - Run it at the same directory to  `phantom_brigade.py`.
    - When not successed; python will show error message, read it before you exit.

### Common Error
- You may set wrong path.
- Some original files have special characters which system in some locations can't deal, so *you need to replace to other available character* using editor before you run.
