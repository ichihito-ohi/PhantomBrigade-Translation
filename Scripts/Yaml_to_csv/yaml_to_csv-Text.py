# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

with open('Yaml_to_csv/config.yaml', 'r', encoding='utf-8', errors='strict') as cfg:
    config = yaml.load(cfg, yaml.FullLoader)
    for key in config:
        if key == 'rootPath':
            root_path = pathlib.Path(config['rootPath'])

ex = pb.Extractor(root_path)


target_list = [
    'Configs/Text/English/Sectors']


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
                    if data['description'] != None:
                        line = ex.formCsvLine(src_path, data['description'], ['description'])
                        print(line)
                        dst.write(line)
                        
                    if data['entries'] != None:
                        for key_entry in data['entries']:
                            if data['entries'][key_entry] != None:
                                if data['entries'][key_entry]['text'] != None:
                                    line = ex.formCsvLine(src_path, data['entries'][key_entry]['text'], ['entries', key_entry, 'text'])
                                    print(line)
                                    dst.write(line)


except Exception as e:
    print(e, file=sys.stderr)
