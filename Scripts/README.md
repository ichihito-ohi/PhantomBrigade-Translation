# yaml_to_csv Scripts

Copyright (c) 2020-2021 Ichihito Ohi

## Requirements
- Python 3.7 (Not verified with other versions.)
- Editor
    - *(Official recommended)* Notepad++
- *(Recommended)* CSV viewer;
    - Microsoft Office Excel
- *(Recommended)* A virtual environment manager for Python;
    - Visual Studio 2019 Community

---
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
    - Successed; you will get a csv file in same folder as the script.
    - Not successed; python will show error message, read it before you exit.

### Common Error
- You may set wrong path.
- Some original files have special characters which system in some locations can't deal, so *you need to replace to other available character* using editor before you run.

---
## Support Files

_(Common)_
### yaml_to_csv-Text.py
- `PhantomBrigade/Configs/Text`
### yaml_to_csv-firstLevelKey.py
- `PhantomBrigade/Configs/DataDecomposed/Overworld/Blueprints`
- `PhantomBrigade/Configs/DataDecomposed/Overworld/EventStats`
- `PhantomBrigade/Configs/DataDecomposed/Overworld/FactionBranches`
- `PhantomBrigade/Configs/DataDecomposed/Overworld/Provinces`
- `PhantomBrigade/Configs/DataDecomposed/PilotChecks`
- `PhantomBrigade/Configs/DataDecomposed/UnitBlueprints`
- `PhantomBrigade/Configs/DataDecomposed/UnitChecks`
- `PhantomBrigade/Configs/DataDecomposed/UnitPresets`
- `PhantomBrigade/Configs/DataDecomposed/UnitStats`
### yaml_to_csv-Combat.py (WIP)
- `PhantomBrigade/Configs/DataDecomposed/Combat/Stats`
- `PhantomBrigade/Configs/DataDecomposed/Combat/UnitGroups`

_(Unique)_
### yaml_to_csv-Cutscenes.py
- `PhantomBrigade/Configs/DataDecomposed/Cutscenes`
### yaml_to_csv-InfoPages.py
- `PhantomBrigade/Configs/DataDecomposed/InfoPages`
### yaml_to_csv-simulation.py
- `PhantomBrigade/Configs/Data/Settings/simulation.yaml`
### yaml_to_csv-ui.py (WIP)
- `PhantomBrigade/Configs/Data/Settings/ui.yaml`

_(Not required but remain)_
### yaml_to_csv-Tutorials.py
- `PhantomBrigade/Configs/DataDecomposed/Tutorials`