import sys
import pathlib
import yaml
import csv
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)

dir_list = [
    'Configs/Text/English/Sectors']

# TODO: Set the translation csv file
csv_path = pathlib.Path('PhantomBrigade-Translation-jp.csv')

try:
    with open(csv_path, 'r', newline='', encoding='utf-8', errors='strict') as csvFile:
        csvReader = csv.DictReader(csvFile)
        id = list()
        text = list()
        for row in csvReader:
            # TODO: Csv file should have 'Id' and 'Translation' label in the first row
            id.append(row.get('Id'))
            text.append(row.get('Translation'))
        csvDict = dict(zip(id, text))


    for dir in dir_list:
        dir_path = pathlib.Path(dir)
        src_list = list((root_path/dir_path).glob('*.yaml'))     

        for p in src_list:
            src_path = pathlib.Path(p)
            with open(src_path, 'r', encoding='utf-8', errors='strict') as src:

                dst_path = src_path.name
                with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
                    data = yaml.load(src,yaml.FullLoader)

                    # TODO: Custom for yaml pattern
                    if data['description'] != None:
                        key = ex.formId(src_path, ['description'])
                        if key in csvDict:
                            if csvDict.get(key) != '':
                                data['description'] = csvDict.get(key)

                    if data['entries'] != None:
                        for key_entry in data['entries']:
                            if data['entries'][key_entry] != None:
                                if data['entries'][key_entry]['text'] != None:
                                    key = ex.formId(src_path, ['entries', key_entry, 'text'])
                                    if key in csvDict:
                                        if csvDict.get(key) != '':
                                            print(csvDict.get(key))
                                            data['entries'][key_entry]['text'] = csvDict.get(key)


                    yaml.dump(data, dst, encoding='utf8', allow_unicode=True, width=sys.maxsize, sort_keys=False)


except Exception as e:
    print(e, file=sys.stderr)
