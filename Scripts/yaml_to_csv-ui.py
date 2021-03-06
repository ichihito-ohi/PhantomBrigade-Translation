# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)

# This script extract from single yaml file
target = pathlib.Path('Configs/Data/Settings/ui.yaml')
src_path = root_path/target
dst_stem = str(target).replace(target._flavour.sep, '-') + '-EN'
dst_path = pathlib.Path(dst_stem).with_suffix('.csv')


try:
    with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
        
        with open(src_path, 'r', encoding='utf-8', errors='strict') as src:

            data = yaml.load(src,yaml.FullLoader)

            # TODO: Custom for yaml pattern
            for key_ui in data:
                if key_ui == 'modeConfigs':
                    for key_modeConfig in data['modeConfigs']:
                        for key_item in data['modeConfigs'][key_modeConfig]:
                            if key_item == 'header' or key_item == 'tooltip':
                                if data['modeConfigs'][key_modeConfig][key_item] != None:
                                    line = ex.formCsvLine(src_path, data['modeConfigs'][key_modeConfig][key_item], 'modeConfigs', key_modeConfig, key_item)
                                    print(line)
                                    dst.write(line)

                else:
                    if type(data[key_ui]) == dict:
                        for key_item in data[key_ui]:
                            if key_item == 'custom':
                                for key_text in data[key_ui]['custom']:
                                    if key_text == 'textHeader':
                                        if data[key_ui]['custom']['textHeader'] != None:
                                            line = ex.formCsvLine(src_path, data[key_ui]['custom']['textHeader'], key_ui, 'custom', 'textHeader')
                                            print(line)
                                            dst.write(line)

                                    if key_text == 'textContent':
                                        if data[key_ui]['custom']['textContent'] != None:
                                            for textContent in data[key_ui]['custom']['textContent']:
                                                line = ex.formCsvLine(src_path, textContent, key_ui, 'custom', 'textContent')
                                                print(line)
                                                dst.write(line)


except Exception as e:
    print(e, file = sys.stderr)
