## Main Purposes
This script copy the yaml files and overwrite source texts with the translation texts according to the csv file.


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

### Note
- For each `.py` script, set `root_path` to the folder including the `Configs` folder.
    ```python
    # TODO: Set the path to 'Configs' folder
    root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
    ```


## Support Files

### csv_to_yaml-Text.py
- `Configs/Text`
