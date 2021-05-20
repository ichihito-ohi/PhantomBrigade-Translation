# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)


target_list = [
    'Configs/DataDecomposed/Equipment/Part_Sockets',
    'Configs/DataDecomposed/Equipment/Features',
    'Configs/DataDecomposed/Overworld/Blueprints',
    'Configs/DataDecomposed/Overworld/EventOptions',
    'Configs/DataDecomposed/Overworld/EventStats',
    'Configs/DataDecomposed/Overworld/FactionBranches',
    'Configs/DataDecomposed/Overworld/Provinces',
    'Configs/DataDecomposed/PilotChecks',
    'Configs/DataDecomposed/UnitBlueprints',
    'Configs/DataDecomposed/UnitChecks',
    'Configs/DataDecomposed/UnitPresets',
    'Configs/DataDecomposed/UnitStats']


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

                    data = yaml.load(src, yaml.FullLoader)

                    for key0 in data:
                        if key0 == 'textHeader' or key0 == 'textContent' or key0 == 'textName' or key0 == 'textDesc' or key0 == 'description':
                            if data[key0] != None:
                                line = ex.formCsvLine(src_path, data[key0], key0)
                                print(line)
                                dst.write(line)


except Exception as e:
    print(e, file=sys.stderr)
