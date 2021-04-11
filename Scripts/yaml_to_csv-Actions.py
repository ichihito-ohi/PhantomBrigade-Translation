# TODO: Only for 'PhantomBrigade/Configs/DataDecomposed/Overworld/Actions'

import sys
import argparse
import pathlib
import yaml


# TODO: Set the path to the folder, not to yaml files
ls = list(pathlib.Path('PATH').glob('*.yaml'))

# TODO: Set output name
dst_path = pathlib.PurePath('Actions-EN.csv')


try:
    # TODO: Set encoding of csv for your language
    # TODO: Windows can't en/decode some characters like '\u2014'. Replace them before
    with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:

        i = 0
        for p in ls:
            src_path = pathlib.PurePath(p)
            print(src_path)

            src_name = src_path.name
            src_stem = src_path.stem

    
            with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
                def constructor_ActionCallArgInt(loader, node):
                    return '!ActionCallArgInt'
                def constructor_ActionCallArgString(loader, node):
                    return '!ActionCallArgString'
                def constructor_AreaLocation(loader, node):
                    return '!AreaLocation'
                def constructor_UnitGroupEmbedded(loader, node):
                    return '!UnitGroupEmbedded'
                def constructor_UnitPresetLink(loader, node):
                    return '!UnitPresetLink'
                def constructor_UnitPresetEmbedded(loader, node):
                    return '!UnitPresetEmbedded'
                def constructor_EventCallArgInt(loader, node):
                    return '!EventCallArgInt'
                def constructor_EventCallArgString(loader, node):
                    return '!EventCallArgString'
                def constructor_EventCallArgStringList(loader, node):
                    return '!EventCallArgStringList'

                yaml.add_constructor(u'!ActionCallArgInt', constructor_ActionCallArgInt)
                yaml.add_constructor(u'!ActionCallArgString', constructor_ActionCallArgString)
                yaml.add_constructor(u'!AreaLocation', constructor_AreaLocation)
                yaml.add_constructor(u'!UnitGroupEmbedded', constructor_UnitGroupEmbedded)
                yaml.add_constructor(u'!UnitPresetLink', constructor_UnitPresetLink)
                yaml.add_constructor(u'!UnitPresetEmbedded', constructor_UnitPresetEmbedded)
                yaml.add_constructor(u'!EventCallArgInt', constructor_EventCallArgInt)
                yaml.add_constructor(u'!EventCallArgString', constructor_EventCallArgString)
                yaml.add_constructor(u'!EventCallArgStringList', constructor_EventCallArgStringList)
        
                data = yaml.load(src,yaml.FullLoader)

                if data['ui'] != None:
                    for key_item in data['ui']:
                        if key_item == 'textName' or key_item == 'textContext' or key_item == 'textStart' or key_item == 'textCancel' or key_item == 'textEnd' or key_item == 'textDesc':
                            if data['ui'][key_item] != None:
                                textVal = str(data['ui'][key_item]).replace('"', '""')
                                i += 1
                                text_str = src_stem + ',' + str(i) + ',' + str(key_item) + ',\"' + textVal + '\"\n'
                                print(text_str)
                                dst.write(text_str)


except Exception as e:
    print(e, file=sys.stderr)
