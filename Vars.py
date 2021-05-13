# -*- coding: utf-8 -*-

from os import read, open, write, close
from json import loads, dumps

class Vars():
    def __init__(self):
        self.dirr = "D:/propriétaire/Python Projects/poulailler/"
        self.file = open(self.dirr+"settings.json", 2)
        self.settings = loads(read(self.file, 9999999))
        close(self.file)

    def load(self): 
        def loader(key):
            out = ()
            for i in key:
                out = out.__add__((key[i],))
            return out

        self.__init__()
        out = loader(self.settings["custom"])
        if out == (): return loader(self.Create())
        else: return out

    def Create(self): 
        self.settings["custom"] = self.settings["default"]
        self.file = open(self.dirr+"settings.json",2)

        write(self.file,dumps(
            loads("""{}"default": {}, "custom": {}{}""".format(
                "{", 
                dumps(self.settings["default"]), 
                dumps(self.settings["custom"]), 
                "}"
            ))
        , indent=2).encode("utf-8"))
        close(self.file)
        
        self.__init__()
        return self.settings

    def save(self, item, value):
        try: self.settings["custom"][item] = value
        except KeyError: self.settings["custom"] += {str(item): value}

    def get(self, item):
        try: return self.settings["custom"][item]
        except KeyError: raise KeyError("the key '{}' doesn't exist".format(item))

Vars=Vars()
