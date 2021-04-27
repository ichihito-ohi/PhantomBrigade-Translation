# TODO: Only for 'PhantomBrigade/Configs/Data/Settings/simulation.yaml'

import sys
import argparse
import pathlib
import yaml


# TODO: Set the path to the yaml file, not to the folder
src_path = pathlib.Path('PATH')

src_name = src_path.name
src_stem = src_path.stem
dst_path = pathlib.PurePath(src_stem + '-EN.csv')


try:
    with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:

        i = 0

        print(src_path)
        with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
            def constructor_ActionCallArgInt(loader, node):
                return '!ActionCallArgInt'
            def constructor_ActionCallArgString(loader, node):
                return '!ActionCallArgString'
            def constructor_AreaLocation(loader, node):
                return '!AreaLocation'
            def constructor_AreaLocationFilter(loader, node):
                return '!AreaLocationFilter'
            def constructor_UnitFilter(loader, node):
                return '!UnitFilter'
            def constructor_UnitGroupEmbedded(loader, node):
                return '!UnitGroupEmbedded'
            def constructor_UnitGroupFilter(loader, node):
                return '!UnitGroupFilter'
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
            yaml.add_constructor(u'!AreaLocationFilter', constructor_AreaLocationFilter)
            yaml.add_constructor(u'!UnitFilter', constructor_UnitFilter)
            yaml.add_constructor(u'!UnitGroupEmbedded', constructor_UnitGroupEmbedded)
            yaml.add_constructor(u'!UnitGroupFilter', constructor_UnitGroupFilter)
            yaml.add_constructor(u'!UnitPresetLink', constructor_UnitPresetLink)
            yaml.add_constructor(u'!UnitPresetEmbedded', constructor_UnitPresetEmbedded)
            yaml.add_constructor(u'!EventCallArgInt', constructor_EventCallArgInt)
            yaml.add_constructor(u'!EventCallArgString', constructor_EventCallArgString)
            yaml.add_constructor(u'!EventCallArgStringList', constructor_EventCallArgStringList)
        
            data = yaml.load(src,yaml.FullLoader)


            for key_item in data['weightClasses']:
                data_item = yaml.safe_load(yaml.safe_dump(key_item))
                for key_text in data_item:
                    if key_text == 'textName' or key_text == 'textDesc':
                        if data_item[key_text] != None:
                            textVal = str(data_item[key_text]).replace('"', '""')
                            i += 1
                            text_str = src_stem + ',' + str(i) + ',' + str(data_item['textName']) + ',' + str(key_text) + ',\"' + textVal + '\"\n'
                            print(text_str)
                            dst.write(text_str)


except Exception as e:
    print(e, file = sys.stderr)
