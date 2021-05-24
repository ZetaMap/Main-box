# -*- coding: utf-8 -*-

from Lib.keyboard import read_hotkey as keyInput, wait
from time import sleep
from Vars import Vars
from Functions import *

class Brain:
    def init(self):
        Vars.init()
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
        self.ScanResult = ScanMenu(self.main_menu)

    def _format(self, key, format):
        output, dump=[], ()
        for i in range(len(key)):
            try:
                output.append(key[i].format(format[i][0]))
            except IndexError: 
                try:
                    for ii in range(key[i].count("{}")): dump+=(format[i][ii],)
                    output.append(eval("key[i].format"+str(dump)))
                except IndexError: 
                    for ii in range(key[i].count("{}")): dump+=("<unknown>",)
                    output.append(eval("key[i].format"+str(dump)))
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
        Vars.SaveSettingAll(self.settings)
        wait("suppr") 
        self.init()  # allumer tout
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

"""

while True:
    try: Brain._print(Brain.keys(keyInput(False), Brain.main_menu))
    except IndexError: ...
"""
