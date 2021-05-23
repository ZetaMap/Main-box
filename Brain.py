# -*- coding: utf-8 -*-

from Lib.keyboard import read_hotkey as keyInput, wait
from time import sleep
from Vars import Vars

class Brain:
    def __init__(self):
        fileContent = Vars.loadFile("settings")
        self.settings = fileContent["custom"]
        if self.settings == {}: self.settings = Vars.create()["custom"]
        for i in fileContent["default"]: 
            if not i in self.settings: self.settings.update({i: fileContent["default"][i]})
        Vars.saveEach(self.settings)
        self.main_menu = Vars.loadFile("menu")

        self.dir = 0
        self.index = 0
        self.later = self.main_menu
        screen = self.settings["screen"].split("x")
        self.lines = int(screen[0])
        self.letters = int(screen[1])
        self.isACounter = False

    def runAction(self, file, index, *args):
        try:
            exec("from {}.{} import {}".format(self.settings["actionsFolder"], file, file))
            if index < 0: raise ValueError("the value of 'index' must be greater than or equal to 0")
            exec("{}({}, {})".format(file, index, args))
        except ModuleNotFoundError: raise FileNotFoundError("the file '"+file+".py' doesn't exist")
        except ImportError: raise ImportError("the main function: '"+file+"', isn't defined in the file")
        except TypeError: raise Warning("the main function takes 1 positional arguments")
    
    def back(self):
        self.dir = 0
        self.index = 0
        self.later = self.main_menu
        sleep(2)
        return self.name(self.main_menu, 0)[0]

    def succes(self):
        print("Paramètre     /")
        print("modifié !  \\/")
        return self.back()

    def name(self, key, index):
        output, lines=[], self.lines
        for i in range(lines):
            if len(key) != 0:
                if type(key[i]) == str:
                    if i == index: output.append(">"+key[index+i])
                    else: output.append(" "+key[index+i])
                elif type(key[i]) == dict:
                    if i == index: output.append(">"+key[index+i]["name"])
                    else: output.append(" "+key[index+i]["name"])
                else: raise TypeError("only 'str' or 'dict' type is accept in the key")
                lines-=1
        return output, lines

    def waitStart(self):
        for i in range(self.lines): print()   # éteindre l'écran
        wait("suppr")
        for i in self.name(self.main_menu, 0)[0]: print(i) #  allumer l'écran
        self.__init__()

    def keys(self, input, key):
        if input == "haut": 
            if self.index <= 0: self.index = 0
            else: self.index-=1
            return key[self.index]

        elif input == "bas": 
            if self.index >= len(key)-1: self.index = len(key)-1
            else: self.index+=1
            return key[self.index]

        elif input == "enter":
            self.dir+=1
            self.later = key[self.index]["option"]
            try: 
                try: out = key[self.index]["option"]
                except KeyError: out = key[self.index]
            except KeyError: return None
            self.index = 0
            return out

        elif input == "backspace":
            self.dir-=1
            self.index = 0
            return self.later

        elif input == "gauche" and self.isACounter:
            ...

        elif input == "droite" and self.isACounter:
            ...
        
        elif input == "suppr": self.waitStart()

        print(self.index,":",self.dir,":",input)

Brain=Brain()

for i in Brain.name(Brain.main_menu, 0)[0]:
    print(i)