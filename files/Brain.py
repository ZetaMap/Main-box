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
        self.later = self.ScanResult
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
        self.later = self.ScanResult
        sleep(2)
        return self.main_menu

    def succes(self):
        print("Paramètre    /")
        print("modifié !  \\/")
        return self.back()

    def name(self, key, index, lines):
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
        self.main(self.ScanResult)

    def keys(self, input):
        if input == "haut": 
            self.index-=1
            self.main(self.ScanResult)

        elif input == "bas": 
            self.index+=1
            self.main(self.ScanResult)

        elif input == "enter":			
            if not self.ScanResult[self.index]["emptyOption"]:
                self.later=self.ScanResult
                if self.ScanResult[self.index]["isASwitch"]: pass
                else: self.ScanResult=self.ScanResult[self.index]["intoOption"]
                
                self.index=0
                self.main(self.ScanResult)

        elif input == "backspace":
            self.index = 0
            self.ScanResult = self.later

            self.main(self.ScanResult)

        elif input == "gauche" and self.isACounter:
            pass

        elif input == "droite" and self.isACounter:
            pass
        
        elif input == "suppr": self.waitStart()
        
        else: return []
    
    def main(self, key, values=()):
        if self.index < 0: self.index=0
        if self.index > len(key)-1: self.index=len(key)-1

        menu=eval("self."+key[self.index]["currently"])

        if not key[self.index]["emptyDesc"]:output, lines=self.desc(menu, key["values"])
        else: output, lines=[], self.lines
        output2, lines, self.index=self.name(menu, self.index, lines)
        output+=output2
        
        print("\n\n")
        for i in output:
            print(i)

Brain=Brain()
