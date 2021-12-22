# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)

# This script extract from single yaml file
target = pathlib.Path('Configs/Data/Settings/simulation.yaml')
src_path = root_path/target
dst_stem = str(target).replace(target._flavour.sep, '-') + '-EN'
dst_path = pathlib.Path(dst_stem).with_suffix('.csv')


try:
    with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
        ver = ex.getVersion()
        print(ex.ver)
        dst.write(ex.ver + '\n')

        with open(src_path, 'r', encoding='utf-8', errors='strict') as src:

            data = yaml.load(src,yaml.FullLoader)

            # TODO: Custom for yaml pattern
            i = -1
            for key_item in data['weightClasses']:
                i += 1

                data_item = yaml.safe_load(yaml.safe_dump(key_item))
                for key_text in data_item:
                    if key_text == 'textName' or key_text == 'textDesc':
                        if data_item[key_text] != None:
                            line = ex.formCsvLine(src_path, data_item[key_text], ['weightClasses', i, key_text])
                            print(line)
                            dst.write(line)


except Exception as e:
    print(e, file = sys.stderr)
