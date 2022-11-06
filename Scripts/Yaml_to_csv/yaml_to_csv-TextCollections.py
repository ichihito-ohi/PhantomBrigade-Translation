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
    'Configs/TextLibrary/Collections']


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
                    if data['entries'] != None:

                        i = -1
                        for key_sub in data['entries']:
                            i += 1
                            
                            line = ex.formCsvLine(src_path, key_sub, ['entries', i])
                            print(line)
                            dst.write(line)


except Exception as e:
    print(e, file=sys.stderr)
    # sys.exit(1)
