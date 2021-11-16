import os
import sys
import pathlib
import yaml
import csv
import phantom_brigade as pb

ex = pb.Extractor()

# TODO: Set the translation list
csv_path = pathlib.Path('PhantomBrigade-Translation-jp.csv')
root_path = pathlib.Path('PB_Translation-jp')
edit_path = root_path / 'ConfigEdits'

try:
    with open(csv_path, 'r', newline='', encoding='utf-8', errors='strict') as csvFile:
        csvReader = csv.DictReader(csvFile)
        
        folder_buff = pathlib.Path()
        file_buff = pathlib.Path()
        os.makedirs(edit_path, exist_ok=True)

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


        for row in csvReader:
            folder = row.get('Folder')
            file = row.get('File')
            id = row.get('Id')
            trans = row.get('Translation')

            if folder != folder_buff:
                folder_buff = pathlib.Path(folder)
                os.makedirs(root_path / 'ConfigEdits' / folder_buff.relative_to('Configs'), exist_ok=True)

            if pathlib.Path(file) != file_buff:
                yaml.dump(dst_data, dst, encoding='utf8', allow_unicode=True, width=sys.maxsize, sort_keys=False)
                dst.close()
                file_buff = pathlib.Path(file)
                dst_path = root_path / 'ConfigEdits' / folder_buff.relative_to('Configs') / file_buff.with_suffix('.yaml')
                dst = open(dst_path, 'w', encoding='utf-8', errors='strict')
                dst_data = yaml.load("{'removed': false, 'edits': []}", yaml.FullLoader)

            line = ex.formEditLine(id, trans)
            print(line)
            dst_data['edits'].append(line)


except Exception as e:
    print(e, file=sys.stderr)
