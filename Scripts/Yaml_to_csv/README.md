## Main Purposes
These scripts extract the source texts for translation and output them with the metadata of folder path, file name, and ID into a csv file.


## How to Use
*Read the general manual in advance*

### Output Format

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

### Note
- For each `.py` script, set `root_path` to the folder including the `Configs` folder.
    ```python
    # TODO: Set the path to 'Configs' folder
    root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
    ```


## Support Files

_(Common)_
### yaml_to_csv-Text.py
- `Configs/Text`
### yaml_to_csv-firstLevelKey.py
- `Configs/DataDecomposed/Overworld/BaseActions`
- `Configs/DataDecomposed/Overworld/BaseStats`
- `Configs/DataDecomposed/Overworld/BaseStatGroups`
- `Configs/DataDecomposed/Overworld/EventStats`
- `Configs/DataDecomposed/Overworld/FactionBranches`
- `Configs/DataDecomposed/Overworld/Provinces`
- `Configs/DataDecomposed/PilotChecks`
- `Configs/DataDecomposed/UnitBlueprints`
- `Configs/DataDecomposed/UnitChecks`
- `Configs/DataDecomposed/UnitPresets`
- `Configs/DataDecomposed/UnitStats`
### yaml_to_csv-Combat.py
- `Configs/DataDecomposed/Combat/Comms`
- `Configs/DataDecomposed/Combat/Stats`
- `Configs/DataDecomposed/Combat/UnitGroups`

_(Unique)_
### yaml_to_csv-BaseParts.py
- `Configs/DataDecomposed/Overworld/BaseParts`
### yaml_to_csv-Cutscenes.py
- `Configs/DataDecomposed/Cutscenes`
### yaml_to_csv-InfoPages.py
- `Configs/DataDecomposed/InfoPages`
### yaml_to_csv-simulation.py
- `Configs/Data/Settings/simulation.yaml`
### yaml_to_csv-ui.py (WIP)
- `Configs/Data/Settings/ui.yaml`

_(Not required but remain)_
### yaml_to_csv-Tutorials.py
- `Configs/DataDecomposed/Tutorials`
