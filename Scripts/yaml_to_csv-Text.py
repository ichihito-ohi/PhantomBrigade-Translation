# TODO: Only for 'PhantomBrigade/Configs/Text'

import sys
import argparse
import pathlib
import yaml


# TODO: Set each yaml file name manually
# UNDONE: Scan all yaml files in the folder automatically
src_path = pathlib.PurePath('overworld_events.yaml')

src_name = src_path.name
src_stem = src_path.stem
dst_path = pathlib.PurePath(src_stem + '-EN.csv')


try:
    # TODO: Windows can't en/decode some characters like '\xab' and '\xbb'. Replace them before.
    with open(src_path, 'r', encoding='utf-8', errors='strict') as src:

        # TODO: Set encoding of csv for your language
        with open(dst_path, 'w', encoding='shift_jis', errors='strict') as dst:
            data = yaml.safe_load(src)
            
            i = 0
            for entry in data['entries']:
                i+=1

                text_str = str(data['entries'][entry]['text']).replace('\n', '\n\n')

                entry_str = src_stem + ',' + str(i) + ',' + entry + ',\"' + text_str + '\"\n'
                print(entry_str)
                dst.write(entry_str)

except Exception as e:
    print(e, file=sys.stderr)
