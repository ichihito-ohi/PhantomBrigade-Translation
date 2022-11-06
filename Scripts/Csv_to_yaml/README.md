# CSV to YAML

These scripts make the mod files for the official system according to the CSV translation sheet.


## How to Use
*Read the general manual in advance*

### 1. Make CSV translation sheet

### 2. Set values in code
- **csv_to_yaml-TextSectors.py**
    - Set `csv_path` to the CSV translation sheet.
        ```python
        # TODO: Set the translation sheet
        csv_path = pathlib.Path('PhantomBrigade-Translation-jp.csv')
        ```
    - Set language name `<lang>` in `local_path`
        ```python
        # TODO: Set the language name
        local_path = pathlib.Path("PB_Translation-jp/Localizations/<lang>")
        ```
- **csv_to_yaml-ConfigEdits.py**
    - Set `csv_path` to the CSV translation sheet.
        ```python
        # TODO: Set the translation sheet
        csv_path = pathlib.Path('PhantomBrigade-Translation-jp.csv')
        ```
    - Set metadata as needed. Don't change `includesConfigEdits: true` and `includesLocalizations: true`.
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
                            "includesLocalizations: true, "
                            "gameVersionMin: , "
                            "gameVersionMax: , "
                            "name: PB_Translation-jp, "
                            "desc: Phantom Brigade Translation Mod for Japanese"
                            "}", yaml.FullLoader)
        ```

### 3. Run the script
YAML files will be generated in the current directory.


## Input Format
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


## Support Files
- **csv_to_yaml-TextSectors.py**
    - `Configs/TextLibrary/Sectors/`
- **csv_to_yaml-ConfigEdits**
    - `Configs/Data/`
    - `Configs/DataDecomposed/`
