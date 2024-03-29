# YAML to CSV

These scripts extract the source texts for translation and output them with the metadata of folder path, file name, and ID into a csv file.


## How to Use
*Read the general manual in advance*

### 1. Set value in code
In `config.yaml`, set `rootPath` to the folder just above `Configs` folder: `PhantomBrigade` or `PhantomAlpha`
- **config.yaml**
    ```yaml
    rootPath: C:\Program Files\Epic Games\PhantomBrigade
    ```

### 2. Run the scripts
CSV files will be generated in the current directory.


## Output Format

build info<br>Folder|<br>File|<br>Id|<br>Source
---|---|---|---
`Configs/***`|`filename`|`Configs/***/filename:key.to.the.text`|"String"

- **build info**
    - The first row of the csv shows which version the data was extracted from.
        ```
        <YYYY>-<MM>-<DD>-<hhmm>-<version>-<buildNumber>-<hash>
        ```

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


## Support Files

- **yaml_to_csv-TextSectors.py**
    - `Configs/TextLibrary/Sectors`
- **yaml_to_csv-TextCollections.py**
    - `Configs/TextLibrary/Collections`
- **yaml_to_csv-firstLevelKey.py**
    - `Configs/DataDecomposed/Overworld/EventStats`
    - `Configs/DataDecomposed/UnitPresets`
    - `Configs/DataDecomposed/UnitStats`
- **yaml_to_csv-Combat.py**
    - `Configs/DataDecomposed/Combat/Comms`
    - `Configs/DataDecomposed/Combat/UnitGroups`
    - `Configs/Saves/save_internal_newgame/Pilots`      (No mod system support)
    - `Configs/Saves/save_internal_quickstart/Pilots`   (No mod system support)
- **yaml_to_csv-Cutscenes.py**
    - `Configs/DataDecomposed/Cutscenes`
    - `Configs/DataDecomposed/CutscenesVideo`
- **yaml_to_csv-InfoPages.py**
    - `Configs/DataDecomposed/InfoPages`
- **yaml_to_csv-roadmap.py**
    - `Configs/Data/roadmap.yaml`
- **yaml_to_csv-simulation.py**
    - `Configs/Data/Settings/simulation.yaml`
- **yaml_to_csv-ui.py**
    - `Configs/Data/Settings/ui.yaml`
