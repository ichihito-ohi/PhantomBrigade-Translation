from typing import List, Union
import pathlib
import yaml


class Extractor:
    # Get version of Phantom Brigade
    def getVersion(self):
        info_path = self.root_path / 'Configs/buildinfo.yaml'
        try:
            with open(info_path, 'r', encoding='utf-8', errors='strict') as info:
                data = yaml.load(info, yaml.FullLoader)
                if data['data'] != None:
                    data_info = str(data['data'])
                    return data_info
                else:
                    return 'N/A'

        except Exception as e:
            print(e, file=sys.stderr)


    def formId(self, path:pathlib.Path, subkey_list:List[Union[int, str]]=None):
        folder = str(path.relative_to(self.root_path).parent.as_posix())
        file = str(path.stem)
        key = "%s/%s" % (folder, file)

        i = 0
        for subkey in subkey_list:
            if i == 0:
                key += ":%s" % subkey
            else:
                key += ".%s" % subkey
            i += 1
        return key

    # Make a line to write into csv with the defined format
    def formCsvLine(self, path:pathlib.Path, text:str=None, subkey_list:List[Union[int, str]]=None):
        folder = str(path.relative_to(self.root_path).parent.as_posix())
        file = str(path.stem)
        key = "%s/%s" % (folder, file)

        i = 0
        for subkey in subkey_list:
            if i == 0:
                key += ":%s" % subkey
            else:
                key += ".%s" % subkey
            i += 1

        str_text = str(text).replace('"', '""')
        line = "%s,%s,%s,\"%s\"\n" % (folder, file, key, str_text)
        return line


    def formEditLine(self, id:str=None, text:str=None):
        key = id.split(':')[1]
        line = key + ': ' + text
        return line

    # Convert construction in yaml
    def construct(self, loader, node):
        return node.tag

    # Add constructors to yaml loader
    def add_multi_constructors(self):
        yaml.add_constructor('!ActionCallArgInt', self.construct)
        yaml.add_constructor('!ActionCallArgString', self.construct)
        yaml.add_constructor('!AreaLocation', self.construct)
        yaml.add_constructor('!AreaLocationFilter', self.construct)
        yaml.add_constructor('!EventCallArgInt', self.construct)
        yaml.add_constructor('!EventCallArgString', self.construct)
        yaml.add_constructor('!EventCallArgStringList', self.construct)
        yaml.add_constructor('!PartResolverClear', self.construct)
        yaml.add_constructor('!PartResolverKeys', self.construct)
        yaml.add_constructor('!PartResolverTags', self.construct)
        yaml.add_constructor('!SubsystemResolverKeys', self.construct)
        yaml.add_constructor('!UnitFilter', self.construct)
        yaml.add_constructor('!UnitGroupEmbedded', self.construct)
        yaml.add_constructor('!UnitGroupFilter', self.construct)
        yaml.add_constructor('!UnitPresetLink', self.construct)
        yaml.add_constructor('!UnitPresetEmbedded', self.construct)
        pass

    # Represent null
    def represent_null(self, dumper, data):
        return dumper.represent_scalar(u'tag:yaml.org,2002:null', '')
    
    # Add representers to yaml dumper
    def add_multi_representors(self):
        yaml.add_representer(type(None), self.represent_null)
        pass

    # Initiate Extractor
    def __init__(self, root_path:pathlib.Path=None):
        if root_path != None:
            self.root_path = root_path
            self.ver = self.getVersion()
            self.add_multi_constructors()
            self.add_multi_representors()
        pass
