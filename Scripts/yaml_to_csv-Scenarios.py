# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)


target_list = [
    'Configs/DataDecomposed/Combat/Scenarios']


try:
    for t in target_list:
        target = pathlib.Path(t)
        src_list = list((root_path/target).glob('*.yaml'))
        dst_stem = str(target).replace(target._flavour.sep, '-') + '-EN'
        dst_path = pathlib.Path(dst_stem).with_suffix('.csv')

        with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
            for p in src_list:
                src_path = pathlib.Path(p)    
                with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
                    data = yaml.load(src,yaml.FullLoader)

                    # TODO: Custom for yaml pattern
                    if data['states'] != None:
                        for key_state in data['states']:
                            if data['states'][key_state] != None:
                                for key_item in data['states'][key_state]:
                                    if key_item == 'textName' or key_item == 'textDesc':
                                        if data['states'][key_state][key_item] != None:
                                            line = ex.formCsvLine(src_path, data['states'][key_state][key_item], 'states', key_state, key_item)
                                            print(line)
                                            dst.write(line)

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
                                                                                                    line = ex.formCsvLine(src_path, data_commsOnStart['custom'][key_custom], 'states', key_step, 'textHeader')
                                                                                                    print(line)
                                                                                                    dst.write(line)

                                                                                            elif key_custom == 'textContent':
                                                                                                for textContent in data_commsOnStart['custom']['textContent']:
                                                                                                    line = ex.formCsvLine(src_path, textContent, 'states', key_step, 'textContent')
                                                                                                    print(line)
                                                                                                    dst.write(line)

                    if data['steps'] != None:
                        for key_step in data['steps']:
                            if data['steps'][key_step] != None:
                                for key_item in data['steps'][key_step]:
                                    if key_item == 'textCurrentPrimary' or key_item == 'textCurrentSecondary':
                                        if data['steps'][key_step][key_item] != None:
                                            line = ex.formCsvLine(src_path, data['steps'][key_step][key_item], 'steps', key_step, key_item)
                                            print(line)
                                            dst.write(line)

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
                                                                        line = ex.formCsvLine(src_path, data_page[key_hint], 'steps', key_step, key_hint)
                                                                        print(line)
                                                                        dst.write(line)
                                
                                    elif key_item == 'hintsConditional':
                                        if data['steps'][key_step]['hintsConditional'] != None:
                                            i = 0
                                            for key_hintsConditional in data['steps'][key_step][key_item]:
                                                data_hintsConditional = yaml.safe_load(yaml.safe_dump(key_hintsConditional))
                                                for key_hint in data_hintsConditional:
                                                    if key_hint == 'text':
                                                        if data_hintsConditional[key_hint] != None:
                                                            i += 1
                                                            line = ex.formCsvLine(src_path, data_hintsConditional[key_hint], 'steps', key_step, 'text-' + str(i))
                                                            print(line)
                                                            dst.write(line)

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
                                                                        line = ex.formCsvLine(src_path, data_commsOnStart[key_comm][key_custom], 'steps', key_step, key_custom)
                                                                        print(line)
                                                                        dst.write(line)

                                                                elif key_custom == 'textContent':
                                                                    for textContent in data_commsOnStart[key_comm][key_custom]:
                                                                        line = ex.formCsvLine(src_path, textContent, 'steps', key_step, key_custom)
                                                                        print(line)
                                                                        dst.write(line)


except Exception as e:
    print(e, file=sys.stderr)
