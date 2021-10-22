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

    # Make a line to write into csv with the defined format
    def formCsvLine(self, path:pathlib.Path, text:str=None, subkey1:str='', subkey2:str='', subkey3:str=''):
        folder = str(path.relative_to(self.root_path).parent.as_posix())
        file = str(path.stem)
        key = "%s/%s" % (folder, file)
        if subkey1 != '':
            key += ":%s" % subkey1
        if subkey2 != '':
            key += ".%s" % subkey2
        if subkey3 != '':
            key += ".%s" % subkey3
        str_text = str(text).replace('"', '""')
        line = "%s,%s,%s,%s,%s,%s,\"%s\"\n" % (folder, file, subkey1, subkey2, subkey3, key, str_text)
        return line

    # Convert constructor in yaml
    def constructor(self, loader, node):
        return node.tag

    # Add constructors to yaml loader
    def add_constructors(self):
        yaml.add_constructor('!ActionCallArgInt', self.constructor)
        yaml.add_constructor('!ActionCallArgString', self.constructor)
        yaml.add_constructor('!AreaLocation', self.constructor)
        yaml.add_constructor('!AreaLocationFilter', self.constructor)
        yaml.add_constructor('!DataBlockGuidanceInputConstant', self.constructor) # for Equipment/Subsystems
        yaml.add_constructor('!DataBlockGuidanceInputCurve', self.constructor) # for Equipment/Subsystems
        yaml.add_constructor('!EventCallArgInt', self.constructor)
        yaml.add_constructor('!EventCallArgString', self.constructor)
        yaml.add_constructor('!EventCallArgStringList', self.constructor)
        yaml.add_constructor('!UnitFilter', self.constructor)
        yaml.add_constructor('!UnitGroupEmbedded', self.constructor)
        yaml.add_constructor('!UnitGroupFilter', self.constructor)
        yaml.add_constructor('!UnitPresetLink', self.constructor)
        yaml.add_constructor('!UnitPresetEmbedded', self.constructor)
        pass

    # Initiate Extractor
    def __init__(self, root_path:pathlib.Path):
        self.root_path = root_path
        self.ver = self.getVersion()
        self.add_constructors()
        pass
