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
