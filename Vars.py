from os import getcwd
from Lib.json import loads, dumps

class Vars:
    def __init__(self):
        self.dirr = getcwd()+"\\"
        self.settings = self.loadFile("settings")

    def SavePatern(self, paternIndex):
        paterns=[
            # Settings patern
            loads("""{}"default": {}, "custom": {} {}""".format(
            "{", 
            dumps(self.settings["default"]), 
            dumps(self.settings["custom"]), 
            "}"
            ))
        ]
        return paterns[paternIndex]

    def SaveFile(self, fileName, content):
        fileID = open(self.dirr+fileName+".json","wt")
        fileID.write(dumps(content, indent=2))
        fileID.close()
        return self.loadFile(fileName)

    def loadFile(self, fileName): 
        fileID = open(self.dirr+fileName+".json", "rt")
        content = loads(fileID.read())
        fileID.close()
        return content

    def create(self): 
        self.settings["custom"] = self.settings["default"]
        self.settings = self.SaveFile("settings", self.SavePatern(0))
        return self.settings
 
    def save(self, item, value):
        try: self.settings["custom"][item] = value
        except KeyError: self.settings["custom"].update({str(item): value})
        self.SaveFile("settings", self.SavePatern(0))
        return self.settings["custom"][item]

    def saveEach(self, args):
        self.settings["custom"].update(args)
        self.SaveFile("settings", self.SavePatern(0))

Vars=Vars()