# TODO: Only for 'PhantomBrigade/Configs/DataDecomposed/Cutscenes'

import sys
import argparse
import pathlib
import yaml


# TODO: Set each yaml file name manually
# UNDONE: Scan all yaml files in the folder automatically
src_path = pathlib.PurePath('ending.yaml')

src_name = src_path.name
src_stem = src_path.stem
dst_path = pathlib.PurePath(src_stem + '-EN.csv')


try:
    with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
        def constructor_ActionCallArgInt(loader, node):
                    return '!ActionCallArgInt'
                def constructor_ActionCallArgString(loader, node):
                    return '!ActionCallArgString'
                def constructor_AreaLocation(loader, node):
                    return '!AreaLocation'
                def constructor_AreaLocationFilter(loader, node):
                    return '!AreaLocationFilter'
                def constructor_EventCallArgInt(loader, node):
                    return '!EventCallArgInt'
                def constructor_EventCallArgString(loader, node):
                    return '!EventCallArgString'
                def constructor_EventCallArgStringList(loader, node):
                    return '!EventCallArgStringList'
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

                yaml.add_constructor(u'!ActionCallArgInt', constructor_ActionCallArgInt)
                yaml.add_constructor(u'!ActionCallArgString', constructor_ActionCallArgString)
                yaml.add_constructor(u'!AreaLocation', constructor_AreaLocation)
                yaml.add_constructor(u'!AreaLocationFilter', constructor_AreaLocationFilter)
                yaml.add_constructor(u'!EventCallArgInt', constructor_EventCallArgInt)
                yaml.add_constructor(u'!EventCallArgString', constructor_EventCallArgString)
                yaml.add_constructor(u'!EventCallArgStringList', constructor_EventCallArgStringList)
                yaml.add_constructor(u'!UnitFilter', constructor_UnitFilter)
                yaml.add_constructor(u'!UnitGroupEmbedded', constructor_UnitGroupEmbedded)
                yaml.add_constructor(u'!UnitGroupFilter', constructor_UnitGroupFilter)
                yaml.add_constructor(u'!UnitPresetLink', constructor_UnitPresetLink)
                yaml.add_constructor(u'!UnitPresetEmbedded', constructor_UnitPresetEmbedded)
        
        data = yaml.load(src,yaml.FullLoader)


        # TODO: Set encoding of csv for your language
        with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
            i = 0

            if data['subtitles'] != None:
                for key_sub in data['subtitles']:
                    data_sub = yaml.safe_load(yaml.safe_dump(key_sub))
                    time = data_sub['time']
                    textContent = data_sub['textContent']
                    if time != None and textContent != None:
                        i += 1
                        text_str = src_stem + ',' + str(i) + ',' + str(time) + ',\"' + str(textContent) + '\"\n'
                        print(text_str)
                        dst.write(text_str)


except Exception as e:
    print(e, file=sys.stderr)
