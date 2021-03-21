# TODO: Only for 'PhantomBrigade/Configs/DataDecomposed/Cutscenes'

import sys
import argparse
import pathlib
import yaml


# TODO: Set each yaml file name manually
# UNDONE: Scan all yaml files in the folder automatically
src_path = pathlib.PurePath('unique_tutorial_intro.yaml')

src_name = src_path.name
src_stem = src_path.stem
dst_path = pathlib.PurePath(src_stem + '-EN.csv')


try:
    with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
        def constructor_AreaLocation(loader, node):
            return '!AreaLocation'
        def constructor_UnitGroupEmbedded(loader, node):
            return '!UnitGroupEmbedded'
        def constructor_UnitPresetLink(loader, node):
            return '!UnitPresetLink'

        yaml.add_constructor(u'!AreaLocation', constructor_AreaLocation)
        yaml.add_constructor(u'!UnitGroupEmbedded', constructor_UnitGroupEmbedded)
        yaml.add_constructor(u'!UnitPresetLink', constructor_UnitPresetLink)
        
        data = yaml.load(src,yaml.FullLoader)


        # TODO: Set encoding of csv for your language
        with open(dst_path, 'w', encoding='shift_jis', errors='strict') as dst:
            i = 0

            for key_states in data['states']:
                state = key_states

                for key_act in data['states'][key_states]:

                    if key_act == 'textName':
                        textName = data['states'][key_states]['textName']

                    if key_act == 'textDesc':
                        textDesc = data['states'][key_states]['textDesc']

                        if textDesc != None:
                            i += 1
                            text_str = src_stem + ',' + str(i) + ',states,' + str(state) + ',' + str(textName) + ',\"' + str(textDesc) + '\"\n'
                            print(text_str)
                            dst.write(text_str)


            for key_step in data['steps']:
                step = key_step

                for key_turn in data['steps'][key_step]:

                    if key_turn == 'textCurrentPrimary':
                        textCurrentPrimary = data['steps'][key_step]['textCurrentPrimary']
                        textCurrentSecondary = data['steps'][key_step]['textCurrentSecondary']
                        if textCurrentPrimary != None and textCurrentSecondary != None:
                            i += 1
                            text_str = src_stem + ',' + str(i) + ',steps_textCurrent,' + str(step) + ',' + str(textCurrentPrimary) + ',\"' + str(textCurrentSecondary) + '\"\n'
                            print(text_str)
                            dst.write(text_str)


                    elif key_turn == 'intermissions':
                        if data['steps'][key_step]['intermissions'] != None:
                            for key_intermission in data['steps'][key_step]['intermissions']:
                                if key_intermission == 'pages':
                                    if data['steps'][key_step]['intermissions']['pages'] != None:
                                        for key_page in data['steps'][key_step]['intermissions']['pages']:
                                            data_page = yaml.safe_load(yaml.safe_dump(key_page))
                                            header = data_page['header']
                                            content = data_page['content']
                                            if header != None and content != None:
                                                i += 1
                                                text_str = src_stem + ',' + str(i) + ',steps_intermissions,' + str(step) + ',' + str(header) + ',\"' + str(content) + '\"\n'
                                                print(text_str)
                                                dst.write(text_str)


                    elif key_turn == 'hintsConditional':
                        if data['steps'][key_step]['hintsConditional'] != None:
                            for key_hint in data['steps'][key_step]['hintsConditional']:
                                data_hint = yaml.safe_load(yaml.safe_dump(key_hint))
                                text_hint = data_hint['text']
                                if text_hint != None:
                                    i += 1
                                    text_str = src_stem + ',' + str(i) + ',steps_hints,' + str(step) + ',' + '' + ',\"' + str(text_hint) + '\"\n'
                                    print(text_str)
                                    dst.write(text_str)


                    elif key_turn == 'commsOnStart':
                        if data['steps'][key_step]['commsOnStart'] != None:
                            for key_time in data['steps'][key_step]['commsOnStart']:
                                data_time = yaml.safe_load(yaml.safe_dump(key_time))
                                key = data_time['key']
                                textHeader = data_time['custom']['textHeader']
                                
                                for item in data_time['custom']['textContent']:
                                    if item != None:
                                        i += 1
                                        text_str = src_stem + ',' + str(i) + ',steps_comm,' + str(key) + ',' + str(textHeader) + ',\"' + str(item) + '\"\n'
                                        print(text_str)
                                        dst.write(text_str)


except Exception as e:
    print(e, file=sys.stderr)
