# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)


target_list = [
    'Configs/DataDecomposed/Overworld/BaseParts']


try:
    for t in target_list:
        target = pathlib.Path(t)
        src_list = list((root_path/target).glob('*.yaml'))
        dst_stem = str(target).replace(target._flavour.sep, '-') + '-EN'
        dst_path = pathlib.Path(dst_stem).with_suffix('.csv')

        with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
            ver = ex.getVersion()
            print(ex.ver)
            dst.write(ex.ver + '\n')
            
            for p in src_list:
                src_path = pathlib.Path(p)    
                with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
                    data = yaml.load(src,yaml.FullLoader)

                    # TODO: Custom for yaml pattern
                    for key_item in data:
                        if key_item == 'ui':
                            if data['ui'] != None:
                                for key_ui in data['ui']:
                                    if key_ui == 'textName' or key_ui == 'textDesc':
                                        if data['ui'][key_ui] != None:
                                            line = ex.formCsvLine(src_path, data['ui'][key_ui], ['ui', key_ui])
                                            print(line)
                                            dst.write(line)


except Exception as e:
    print(e, file=sys.stderr)
