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

# This script extract from single yaml file
target = pathlib.Path('Configs/Data/Settings/ui.yaml')
src_path = root_path/target
dst_stem = pathlib.Path(str(target).replace(target._flavour.sep, '-')).stem + '-EN'
dst_path = pathlib.Path(dst_stem).with_suffix('.csv')


try:
    with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
        ver = ex.getVersion()
        print(ex.ver)
        dst.write(ex.ver + '\n')
        
        with open(src_path, 'r', encoding='utf-8', errors='strict') as src:

            data = yaml.load(src,yaml.FullLoader)

            # TODO: Custom for yaml pattern
            for key_ui in data:
                if key_ui == 'modeConfigs' or key_ui == 'commSources':
                    for key_item in data[key_ui]:
                        for key_source in data[key_ui][key_item]:
                            if key_source == 'header' or key_source == 'tooltip' or key_source == 'text':
                                if data[key_ui][key_item][key_source] != None:
                                    line = ex.formCsvLine(src_path, data[key_ui][key_item][key_source], [key_ui, key_item, key_source])
                                    print(line)
                                    dst.write(line)


except Exception as e:
    print(e, file = sys.stderr)
