# TODO: Check target_list, this script extract from only them.

import sys
import pathlib
import yaml
import phantom_brigade as pb

# TODO: Set the path to 'Configs' folder
root_path = pathlib.Path('C:/Program Files/Epic Games/PhantomBrigade')
ex = pb.Extractor(root_path)

def constructor_map(loader, node):
    node.tag = 'tag:yaml.org,2002:map'
    string = yaml.serialize(node)
    return string

yaml.add_constructor('!SubsystemResolverHardpoint', constructor_map)
yaml.add_constructor('!SubsystemResolverKeys', constructor_map)
yaml.add_constructor('!SubsystemResolverTags', constructor_map)

target_list = [
    'Configs/DataDecomposed/Equipment/Part_Presets']


try:
    for t in target_list:
        target = pathlib.Path(t)
        src_list = list((root_path/target).glob('*.yaml'))
        dst_stem = str(target).replace(target._flavour.sep, '-')
        dst_path = pathlib.Path(dst_stem).with_suffix('.csv')

        with open(dst_path, 'w', encoding='utf-8', errors='strict') as dst:
            ver = ex.getVersion()
            print(ex.ver)
            dst.write(ex.ver + '\n')

            dst.write("<yaml>,<parents>,<systems>\n")
            
            for p in src_list:
                src_path = pathlib.Path(p)    
                with open(src_path, 'r', encoding='utf-8', errors='strict') as src:
        
                    data = yaml.load(src,yaml.FullLoader)

                    # TODO: Custom for yaml pattern
                    parents = list()
                    systems = list()

                    if data['parents'] != None:
                        for key_parent in data['parents']:
                            data_parent = yaml.safe_load(yaml.safe_dump(key_parent))
                            if data_parent['key'] != None:
                                parents.append(data_parent['key'])

                    if data['systems'] != None:
                        for key_system in data['systems']:
                            if data['systems'][key_system]['resolver'] != None:
                                data_resolver = yaml.safe_load(data['systems'][key_system]['resolver'])
                                for key_resolver in data_resolver:
                                    if key_resolver == 'keys':
                                        systems = data_resolver['keys']

                    str_parents = str(parents).replace('[','').replace(']','').replace("'", '').replace(',', ';')
                    str_systems = str(systems).replace('[','').replace(']','').replace("'", '').replace(',', ';')
                    line = "%s,%s,%s\n" % (src_path.stem,str_parents, str_systems)
                    print(line)
                    dst.write(line)


except Exception as e:
    print(e, file = sys.stderr)
