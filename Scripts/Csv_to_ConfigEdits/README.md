## Main Purpose
This script makes the config edit files for the official modding system according to the csv file of translation list.


## How to Use
*Read the general manual in advance*

### Input Format
*The csv file has to have the label at the first row.*

Folder|File|Id|Source|Translation
---|---|---|---|---
`Configs/***`|`filename`|`Configs/***/filename:key.to.the.text`|"String"|"String"

- **Folder**
    - This column shows the path to the folder including the file where the data was extracted from.

- **File**
    - This column shows the file name (without `.yaml` extension) where the data was extracted from.

- **Id**
    - This column shows the ID of the source text.
    - The ID is used to the several purposes: management of translation task, targeting of the game data overwriting.
    - The ID is a combination of `Folder/File` and `key.to.the.text`, joined by `:`.
    - `key.to.the.text` shows the yaml structure below. The key format is referring to the config edits of the official mod system. [Modding System | BYG Wiki](https://wiki.braceyourselfgames.com/en/PhantomBrigade/Modding/ModSystem#config-edits)
        ```yaml
        key:
            to:
                the:
                    text: "String"
        ```

- **Source**
    - This column shows the source text to translate.

- **Translation**
    - This column shows the translation text.

### Enable Mod
*Read the detail [here](https://wiki.braceyourselfgames.com/en/PhantomBrigade/Modding/ModSystem).*

1. Copy `PB_Translation-jp` (default name) folder, which was made by the script, including `ConfigEdits` folder and `metadata.yaml` file into `Documents/My Games/Phantom Brigade/Mods` folder in the user folder.

1. Boot the game.

1. On the "Mods" tab in the main menu, move the mod to the right list and enable its checkbox, then press "SAVE CONFIG".

1. Reboot the game.

### Note
- Set `csv_path` to the csv file of translation list.
    ```python
    # TODO: Set the translation list
    csv_path = pathlib.Path('PhantomBrigade-Translation-jp.csv')
    ```

- Set metadata as needed. Don't change `includesConfigEdits: true`.
    ```python
    # TODO: Don't forget ', ' at every end of lines
    dst = open(root_path / 'metadata.yaml', 'w', encoding='utf-8', errors='strict')
    dst_data = yaml.load("{"
                         "id: PB_Translation-jp, "
                         "ver: , "
                         "includesConfigOverrides: true, "
                         "includesConfigEdits: true, "
                         "includesLibraries: false, "
                         "includesTextures: false, "
                         "includesLocalizations: false, "
                         "gameVersionMin: , "
                         "gameVersionMax: , "
                         "name: PB_Translation-jp, "
                         "desc: Phantom Brigade Translation Mod for Japanese"
                         "}", yaml.FullLoader)
    ```


## Support Files

### csv_to_config-edit.py
- `Configs/Data`
- `Configs/DataDecomposed`
