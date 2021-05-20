# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)


target_list = [
    'Configs/DataDecomposed/Equipment/Tags/']


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
                    for key_block in data['blocks']:
                        if data['blocks'][key_block] != None:
                            if data['blocks'][key_block]['textShort'] != None and data['blocks'][key_block]['textLong'] != None:
                                line = ex.formCsvLine(src_path, data['blocks'][key_block]['textLong'], key_block, data['blocks'][key_block]['textShort'])
                                print(line)
                                dst.write(line)


except Exception as e:
    print(e, file=sys.stderr)
