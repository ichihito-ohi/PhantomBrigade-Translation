# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)


target_list = [
    'Configs/DataDecomposed/Overworld/Events']


try:
    for t in target_list:
        target = pathlib.Path(t)
        src_list = list((root_path/target).glob('*.yaml'))
        dst_stem = str(target).replace(target._flavour.sep, '-') + '-EN'
        dst_path = pathlib.Path(dst_stem).with_suffix('.csv')

        with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
            for p in src_list:
                src_path = pathlib.Path(p)    
                with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
                    data = yaml.load(src,yaml.FullLoader)

                    # TODO: Custom for yaml pattern
                    if data['steps'] != None:
                        for key_step in data['steps']:
                            for key_item in data['steps'][key_step]:
                                if key_item == 'textName' or key_item == 'textDesc':
                                    if data['steps'][key_step][key_item] != None:
                                        line = ex.formCsvLine(src_path, data['steps'][key_step][key_item], key_step, key_item)
                                        print(line) 
                                        dst.write(line)

                    if data['options'] != None:
                        for key_option in data['options']:
                            for key_item in data['options'][key_option]:
                                if key_item == 'textHeader' or key_item == 'textContent':
                                    if data['options'][key_option][key_item] != None:
                                        line = ex.formCsvLine(src_path, data['options'][key_option][key_item], key_option, key_item)
                                        print(line) 
                                        dst.write(line)


except Exception as e:
    print(e, file=sys.stderr)
    # sys.exit(1)
