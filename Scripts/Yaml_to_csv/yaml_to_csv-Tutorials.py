# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)


target_list = [
    'Configs/DataDecomposed/Tutorials']


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
                    if data['pages'] != None:

                        i = -1
                        for key_page in data['pages']:
                            i += 1
                            
                            data_page = yaml.safe_load(yaml.safe_dump(key_page))
                            for key_item in data_page:
                                if key_item == 'header' or key_item == 'content':
                                    if data_page[key_item] != None:
                                        line = ex.formCsvLine(src_path, data_page[key_item], ['pages', i, key_item])
                                        print(line)
                                        dst.write(line)


except Exception as e:
    print(e, file = sys.stderr)
