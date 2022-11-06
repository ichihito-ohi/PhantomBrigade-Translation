import os
import sys
import pathlib
import yaml
import csv
import re
import phantom_brigade as pb

ex = pb.Extractor()

# TODO: Set the translation sheet
csv_path = pathlib.Path('PhantomBrigade-Translation-jp.csv')

# TODO: Set the language name
local_path = pathlib.Path("PB_Translation-jp/Localizations/<lang>")
sectors_path = local_path / 'Sectors'

txtLocalDict = dict()

try:
    with open(csv_path, 'r', newline='', encoding='utf-8', errors='strict') as csvFile:
        csvReader = csv.DictReader(csvFile)

        # Make a text localization dictionary
        for row in csvReader:
            folder = row.get('Folder')
            if folder == 'Configs/TextLibrary/Sectors':

                trans = row.get('Translation')
                if trans != '':
                    id = row.get('Id')
                    key_list = re.split('[:.]', id)

                    if key_list[1] == 'entries':
                        entry_key = key_list[2]
                        entry_field = key_list[3]

                        file = row.get('File')
                        if file not in txtLocalDict:
                            txtLocalDict[file] = {'entries': dict()}

                        entriesDict = txtLocalDict[file]['entries']

                        entriesDict[entry_key] = {entry_field: trans}
                        print(entry_key, ':\t', trans)

                        txtLocalDict[file] = {'entries': entriesDict}
                        
        # Write the dictionary into YAML
        for dst_stem in txtLocalDict:
            dst_path = sectors_path / pathlib.PurePath(dst_stem).with_suffix('.yaml')
            with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
                yaml.dump(txtLocalDict[dst_stem], dst, encoding='utf8', allow_unicode=True, width=sys.maxsize, sort_keys=False)


except Exception as e:
    print(e, file=sys.stderr)
