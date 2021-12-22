# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)


target_list = [
    'Configs/DataDecomposed/InfoPages']


try:
    for t in target_list:
        target = pathlib.Path(t)
        src_list = list((root_path/target).glob('*.yaml'))
        dst_stem = str(target).replace(target._flavour.sep, '-') + '-EN'
        dst_path = pathlib.Path(dst_stem).with_suffix('.csv')

        with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
            ver = ex.getVersion()
            print(ex.ver)
            dst.write(ex.ver + '\n')
            
            for p in src_list:
                src_path = pathlib.Path(p)    
                with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
                    data = yaml.load(src,yaml.FullLoader)

                    # TODO: Custom for yaml pattern
                    for key_item in data:
                        if key_item == 'textLeftSubheader' or key_item == 'textName' or key_item == 'textDesc':
                            if data[key_item] != None:
                                line = ex.formCsvLine(src_path, data[key_item], [key_item])
                                print(line)
                                dst.write(line)

                        if key_item == 'sections':
                            if data['sections'] != None:
                                
                                i = -1
                                for key_section in data['sections']:
                                    i += 1

                                    data_section = yaml.safe_load(yaml.safe_dump(key_section))
                                    for key_text in data_section:
                                        if key_text == 'textHeader':
                                            if data_section['textHeader'] != None:
                                                line = ex.formCsvLine(src_path, data_section['textHeader'], ['sections', i, 'textHeader'])
                                                print(line)
                                                dst.write(line)

                                        elif key_text == 'textChanges':
                                            if data_section['textChanges'] != None:
                                                
                                                j = -1
                                                for textChange in data_section['textChanges']:
                                                    j += 1

                                                    if textChange != None:
                                                        line = ex.formCsvLine(src_path, textChange, ['sections', i, 'textChanges', j])

                                                        print(line)
                                                        dst.write(line)


except Exception as e:
    print(e, file=sys.stderr)
