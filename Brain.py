# -*- coding: utf-8 -*-

from Lib.keyboard import read_hotkey as keyInput, wait
from time import sleep
from Vars import Vars

class Brain:
    def __init__(self):
        fileContent = Vars.LoadFile("settings")
        self.settings = fileContent["custom"]
        if self.settings == {}: self.settings = Vars.CreateSettings()["custom"]
        for i in fileContent["default"]: 
            if not i in self.settings: self.settings.update({i: fileContent["default"][i]})
        Vars.SaveSettingAll(self.settings)
        self.main_menu = Vars.LoadFile("menu")

        self.dir = 0
        self.index = 0
        self.later = self.main_menu
        screen = self.settings["screen"].split("x")
        self.lines = int(screen[0])
        self.letters = int(screen[1])
        self.isACounter = False
        self.isASwitch = False
        self.switchIndex = ()
        self.ScanResult = self.ScanMenu(self.main_menu)

    def ScanMenu(self, key, keyDir=0):
        output=()
        for i in range(len(key)):
            output=output.__add__(({"keyIndex": i},))
            output[i].update({"keyDir": keyDir})
            output[i].update({"later": key})

            if type(key[i]) == dict:
                
                if not key[i].__contains__("name"): raise KeyError("must contain a non-empty 'name' key")
                elif type(key[i]["name"]) != str: raise TypeError("the key 'name' must be a Str")
                elif key[i]["name"] == "": raise ValueError("please don't use an empty Str")

                if not key[i].__contains__("desc"): raise KeyError("must contain a 'desc' key, empty or not")
                elif type(key[i]["desc"]) != list: raise TypeError("the key 'desc' must be a List")
                elif key[i]["desc"] == []: output[i].update({"emptyDesc": True})
                else: 
                    output[i].update({"emptyDesc": False})
                    output[i].update({"intoDesc": self.ScanMenu(key[i]["desc"], keyDir+1)})
                   
                if not key[i].__contains__("option"): raise KeyError("must contain a 'option' key, empty or not")
                elif type(key[i]["option"]) != list: raise TypeError("the key 'option' must be a List")
                elif key[i]["option"] == []: output[i].update({"emptyOption": True})
                else: output[i].update({"emptyOption": False})

                if key[i].__contains__("switch"):
                    if type(key[i]["switch"]) != bool: raise TypeError("the key 'switch' can accept only Bool type")
                    else:
                        if not key[i]["switch"]: output[i].update({"isASwitch": False})
                        else:    
                            output[i].update({"isASwitch": True})
                    
                            if output[i]["emptyOption"]: raise ValueError("if you use the key 'switch', the key 'option' must not be empty")
                            for ii in key[i]["option"]: 
                                if type(ii) != str: raise TypeError("if you use the key 'switch', the list of key 'option' can accept only Str type")
                            if not key[i].__contains__("StartEvent"): KeyError("if you use the key 'switch', you must define a key 'StartEvent', which will launch the function associate with the key. \nThe function will be run with index -1, please use it to return a list of values")
# Disabled for tests
#                            switchValues = self.StartEvent(key[i]["StartEvent"], -1, ())
#                            if not type(switchValues) == list or type(switchValues) == tuple: raise TypeError("the values returned by '{}()' must be of type List or Tuple".format(key[i]["StartEvent"]))
#                            for ii in switchValues:
#                                if type(ii) != list: raise TypeError("please use only List type in the values returned by '{}()'".format(key[i]["StartEvent"]))
#                            output[i].update({"switchValues": switchValues})
                else: 
                    output[i].update({"isASwitch": False})
                    output[i].update({"intoOption": self.ScanMenu(key[i]["option"], keyDir+1)})
                
                output[i].update({"type": dict})

            elif type(key[i]) == str: 
                if key[i] == "": raise ValueError("please don't use an empty Str")
                output[i].update({"type": str})
            
            else: raise TypeError("the key can only accept Str and Dict types")
        return output

    def StartEvent(self, file, position, *args):
        try:
            exec("from {}.{} import {}".format(self.settings["EventsFolder"], file, file))
            exec("return {}({}, {})".format(file, position, args))
        except ModuleNotFoundError: raise FileNotFoundError("the file '"+file+".py' doesn't exist")
        except ImportError: raise ImportError("the main function: '"+file+"()', isn't defined in the file")
        except TypeError: raise Warning("the main function takes 2 positional arguments: (statut: int, args: tuple)")

    def _format(self, key, format):
        output, z=[], ()
        for i in range(len(key)):
            try:
                output.append(key[i].format(format[i][0]))
            except IndexError: 
                try:
                    for ii in range(key[i].count("{}")): z+=(format[i][ii],)
                    output.append(eval("key[i].format"+str(z)))
                except IndexError: 
                    for ii in range(key[i].count("{}")): z+=("<unknown>",)
                    output.append(eval("key[i].format"+str(z)))
        return output

    def back(self):
        self.dir = 0
        self.index = 0
        self.later = self.main_menu
        sleep(2)
        return self.name(self.main_menu, 0)[0]

    def succes(self):
        print("Paramètre    /")
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

    def desc(self, key):
        output, lines=[], self.lines
        for i in range(lines):
            ...

    def waitStart(self):
        for i in range(self.lines): print()   # éteindre tout
        wait("suppr") 
        self.__init__()  # allumer tout
        return self.name(self.main_menu, 0)[0]

    def _print(self, key):
        for i in Brain.name(key, self.index)[0]:
            print(i)

    def keys(self, input, key):
        print(self.index,":",self.dir,":",input)
        
        if input == "haut": 
            if self.index <= 0: self.index = 0
            else: self.index-=1
            return key

        elif input == "bas": 
            if self.index >= len(key)-1-self.lines: self.index = len(key)-1-self.lines
            else: self.index+=1
            return key

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

Brain=Brain()

#print(Brain.ScanMenu(Brain.main_menu))

print(Brain.succes())
"""

while True:
    try: Brain._print(Brain.keys(keyInput(False), Brain.main_menu))
    except IndexError: ...
"""