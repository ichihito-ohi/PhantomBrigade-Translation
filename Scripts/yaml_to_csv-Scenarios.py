# TODO: Only for 'PhantomBrigade/Configs/DataDecomposed/Combat/Scenarios'

import sys
import argparse
import pathlib
import yaml


# TODO: Set the path to the folder, not to yaml files
ls = list(pathlib.Path('PATH').glob('*.yaml'))

# TODO: Set output name
dst_path = pathlib.PurePath('Scenarios-EN.csv')


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

                if data['states'] != None:
                    for key_state in data['states']:
                        if data['states'][key_state] != None:
                            for key_item in data['states'][key_state]:
                                if key_item == 'textName' or key_item == 'textDesc':
                                    if data['states'][key_state][key_item] != None:
                                        textVal = str(data['states'][key_state][key_item]).replace('"', '""')
                                        i += 1
                                        text_str = src_stem + ',' + str(i) + ',' + str('states') + ',' + str(key_state) + ',' + str(key_item) + ',\"' + textVal + '\"\n'
                                        print(text_str)
                                        dst.write(text_str)

                                elif key_item == 'reactions':
                                    if data['states'][key_state]['reactions'] != None:
                                        for key_reaction in data['states'][key_state]['reactions']:
                                            if key_reaction == 'effectsPerIncrement':
                                                if data['states'][key_state]['reactions']['effectsPerIncrement'] != None:
                                                    for key_increment in data['states'][key_state]['reactions']['effectsPerIncrement']:
                                                        for key_effect in data['states'][key_state]['reactions']['effectsPerIncrement'][key_increment]:
                                                            if key_effect == 'commsOnStart':
                                                                if data['states'][key_state]['reactions']['effectsPerIncrement'][key_increment]['commsOnStart'] != None:
                                                            for key_commsOnStart in data['states'][key_state]['reactions']['effectsPerIncrement'][key_increment]['commsOnStart']:
                                                                data_commsOnStart = yaml.safe_load(yaml.safe_dump(key_commsOnStart))
                                                                for key_comm in data_commsOnStart:
                                                                    if key_comm == 'custom':
                                                                        if data_commsOnStart['custom'] != None:
                                                                            for key_custom in data_commsOnStart['custom']:
                                                                                if key_custom == 'textHeader':
                                                                                    if data_commsOnStart['custom'][key_custom] != None:
                                                                                        textVal = str(data_commsOnStart['custom'][key_custom]).replace('"', '""')
                                                                                        i += 1
                                                                                                text_str = src_stem + ',' + str(i) + ',' + str('states') + ',' + str(key_step) + ',' + str('textHeader') + ',\"' + textVal + '\"\n'
                                                                                        print(text_str)
                                                                                        dst.write(text_str)
                                                                                elif key_custom == 'textContent':
                                                                                    for textContent in data_commsOnStart['custom']['textContent']:
                                                                                        textVal = str(textContent).replace('"', '""')
                                                                                        i += 1
                                                                                                text_str = src_stem + ',' + str(i) + ',' + str('states') + ',' + str(key_step) + ',' + str('textContent') + ',\"' + textVal + '\"\n'
                                                                                        print(text_str)
                                                                                        dst.write(text_str)

                if data['steps'] != None:
                    for key_step in data['steps']:
                        if data['steps'][key_step] != None:
                            for key_item in data['steps'][key_step]:
                                if key_item == 'textCurrentPrimary' or key_item == 'textCurrentSecondary':
                                    if data['steps'][key_step][key_item] != None:
                                        textVal = str(data['steps'][key_step][key_item]).replace('"', '""')
                                        i += 1
                                        text_str = src_stem + ',' + str(i) + ',' + str('steps') + ',' + str(key_step) + ',' + str(key_item) + ',\"' + textVal + '\"\n'
                                        print(text_str)
                                        dst.write(text_str)

                                elif key_item == 'intermissions':
                                    if data['steps'][key_step][key_item] != None:
                                        for key_intermission in data['steps'][key_step][key_item]:
                                            if key_intermission == 'pages':
                                                if data['steps'][key_step]['intermissions']['pages'] != None:
                                                    for key_page in data['steps'][key_step]['intermissions']['pages']:
                                                        data_page = yaml.safe_load(yaml.safe_dump(key_page))
                                                        for key_hint in data_page:
                                                            if key_hint == 'header' or key_hint == 'content':
                                                                if data_page[key_hint] != None:
                                                                    textVal = str(data_page[key_hint]).replace('"', '""')
                                                                    i += 1
                                                                    text_str = src_stem + ',' + str(i) + ',' + str('steps') + ',' + str(key_step) + ',' + str(key_hint) + ',\"' + textVal + '\"\n'
                                                                    print(text_str)
                                                                    dst.write(text_str)
                                
                                elif key_item == 'hintsConditional':
                                    if data['steps'][key_step][key_item] != None:
                                        for key_hintsConditional in data['steps'][key_step][key_item]:
                                            data_hintsConditional = yaml.safe_load(yaml.safe_dump(key_hintsConditional))
                                            for key_hint in data_hintsConditional:
                                                if key_hint == 'text':
                                                    if data_hintsConditional[key_hint] != None:
                                                        textVal = str(data_hintsConditional[key_hint]).replace('"', '""')
                                                        i += 1
                                                        text_str = src_stem + ',' + str(i) + ',' + str('steps') + ',' + str(key_step) + ',' + str(key_hint) + ',\"' + textVal + '\"\n'
                                                        print(text_str)
                                                        dst.write(text_str)

                                elif key_item == 'commsOnStart':
                                    if data['steps'][key_step]['commsOnStart'] != None:
                                        for key_commsOnStart in data['steps'][key_step]['commsOnStart']:
                                            data_commsOnStart = yaml.safe_load(yaml.safe_dump(key_commsOnStart))
                                            for key_comm in data_commsOnStart:
                                                if key_comm == 'custom':
                                                    if data_commsOnStart[key_comm] != None:
                                                        for key_custom in data_commsOnStart[key_comm]:
                                                            if key_custom == 'textHeader':
                                                                if data_commsOnStart[key_comm][key_custom] != None:
                                                                    textVal = str(data_commsOnStart[key_comm][key_custom]).replace('"', '""')
                                                                    i += 1
                                                                    text_str = src_stem + ',' + str(i) + ',' + str('steps') + ',' + str(key_step) + ',' + str(key_custom) + ',\"' + textVal + '\"\n'
                                                                    print(text_str)
                                                                    dst.write(text_str)
                                                            elif key_custom == 'textContent':
                                                                for textContent in data_commsOnStart[key_comm][key_custom]:
                                                                    textVal = str(textContent).replace('"', '""')
                                                                    i += 1
                                                                    text_str = src_stem + ',' + str(i) + ',' + str('steps') + ',' + str(key_step) + ',' + str(key_custom) + ',\"' + textVal + '\"\n'
                                                                    print(text_str)
                                                                    dst.write(text_str)



except Exception as e:
    print(e, file=sys.stderr)
