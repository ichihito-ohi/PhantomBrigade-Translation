# TODO: Only for 'PhantomBrigade/Configs/DataDecomposed/Overworld/Equipment/Tags'

import sys
import argparse
import pathlib
import yaml


# TODO: Set the path to the folder, not to yaml files
ls = list(pathlib.Path('PATH').glob('*.yaml'))

# TODO: Set output name
dst_path = pathlib.PurePath('Tags-EN.csv')


try:
    # TODO: Set encoding of csv for your language
    with open(dst_path, 'w', encoding='shift_jis', errors='strict') as dst:


        for p in ls:
            src_path = pathlib.PurePath(p)
            print(src_path)

            src_name = src_path.name
            src_stem = src_path.stem


    
            with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
                def constructor_AreaLocation(loader, node):
                    return '!AreaLocation'
                def constructor_UnitGroupEmbedded(loader, node):
                    return '!UnitGroupEmbedded'
                def constructor_UnitPresetLink(loader, node):
                    return '!UnitPresetLink'
                def constructor_UnitPresetEmbedded(loader, node):
                    return '!UnitPresetEmbedded'

                yaml.add_constructor(u'!AreaLocation', constructor_AreaLocation)
                yaml.add_constructor(u'!UnitGroupEmbedded', constructor_UnitGroupEmbedded)
                yaml.add_constructor(u'!UnitPresetLink', constructor_UnitPresetLink)
                yaml.add_constructor(u'!UnitPresetEmbedded', constructor_UnitPresetEmbedded)
        
                data = yaml.load(src,yaml.FullLoader)
                i = 0

                for key_block in data['blocks']:
                    textShort = data['blocks'][key_block]['textShort']
                    textLong = data['blocks'][key_block]['textLong']
                    if textShort != None and textLong != None:
                        i += 1
                        text_str = src_stem + ',' + str(i) + ',' + str(key_block) + ',' + str(textShort) + ',\"' + str(textLong) + '\"\n'
                        print(text_str)
                        dst.write(text_str)


except Exception as e:
    print(e, file=sys.stderr)
