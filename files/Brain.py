# -*- coding: utf-8 -*-

from lib.keyboard import read_hotkey as keyInput, wait
from time import sleep
from Vars import Vars
from Functions import *

class Brain:
    def init(self, debugScan=False):
        Vars.init()
        try: 
            self.settings = ScanSettings(Vars.LoadFile("settings"))
            self.main_menu = Vars.LoadFile("menu")
            self.ScanResult = ScanMenu(self.main_menu)
            if debugScan: Vars.SaveFile("ScanMenu", self.ScanResult)
        except FileNotFoundError as e: FileNotFoundError(str(e))

        self.index = 0
        self.later = self.main_menu
        screen = self.settings["screen"].split("x")
        self.lines = int(screen[0])
        self.letters = int(screen[1])
        self.isACounter = False

    def _format(self, key, format):
        output, dump=[], ()
        for i in range(len(key)):
            try:
                output.append(key[i].format(format[i]))
            except IndexError: 
                try:
                    for ii in range(key[i].count("{}")): dump+=(format[i][ii],)
                    output.append(eval("key[i].format"+str(dump)))
                except: 
                    for ii in range(key[i].count("{}")): dump+=("<unknown>",)
                    output.append(eval("key[i].format"+str(dump)))
        return output

    def back(self):
        self.index = 0
        self.later = self.main_menu
        sleep(2)
        return self.name(self.main_menu, 0)[0]

    def succes(self):
        print("Paramètre    /")
        print("modifié !  \\/")
        return self.back()

    def name(self, key, index):
        __temp__, output=[], []
        if index < 0: index=0
        if index > len(key)-1: index=len(key)-1
        select=index
        if index+self.lines > len(key): index=len(key)-self.lines
        if index < 0: index=0

        for i in key:
            if type(i) == str: 
                if i == key[select]: __temp__.append(">"+i)
                else: __temp__.append(" "+i)
            elif type(i) == dict: 
                if i == key[select]: __temp__.append(">"+i["name"])
                else: __temp__.append(" "+i["name"])   
        for i in range(self.lines):
            try: output.append(__temp__[index+i])
            except IndexError: break
        return output, self.lines-len(output), select

    def desc(self, key, format=()):
        output, lines=self._format(key["desc"], format), self.lines
        lines=len(output)-lines
        for i in range(lines): output.pop()
        return output, lines


    def waitStart(self):
        for i in range(self.lines): print()   # éteindre tout
        Vars.SaveSettingAll(self.settings)
        wait("suppr") 
        sleep(0.2)
        self.init()  # allumer tout
        return self.main_menu

    def keys(self, input, key):
        print(self.index,":",input)
        
        if input == "haut": 
            self.index-=1
            self.main(key)

        elif input == "bas": 
            self.index+=1
            self.main(key)

        elif input == "enter":
            self.later = key[self.index]["option"]
            try: 
                try: out = key[self.index]["option"]
                except KeyError: out = key[self.index]
            except KeyError: return None
            self.index = 0
            return out

        elif input == "backspace":
            self.index = 0
            return self.later

        elif input == "gauche" and self.isACounter:
            pass

        elif input == "droite" and self.isACounter:
            pass
        
        elif input == "suppr": return self.waitStart()
        
        else: return []
    
    def main(self, key):
        output, lines, self.index=self.name(key, self.index)
        for i in output:
            print(i)

Brain=Brain()