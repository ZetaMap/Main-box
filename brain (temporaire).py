from Vars import *
from time import sleep

def runAction(file, index=-1):
    try:
        exec("from {}.{} import {}".format(Vars.get("actionsFolder"), file, file))
        if index == -1: exec("{}()".format(file))
        else: 
            if index < 0: raise ValueError("the value of 'index' must be greater than or equal to 0")
            exec("{}({})".format(file, index))
    except ModuleNotFoundError: raise FileNotFoundError("the file '"+file+".py' doesn't exist")
    except ImportError: raise ImportError("the main function: '"+file+"', isn't defined in the file")
    except TypeError: raise Warning("the main function takes 1 positional arguments")


def printer(key, screen, input, index=0, format=[]):
    def name(lines, key, index=0):
        output=[]
        if type(key) == list :
            for i in range(lines):
                try: output.append(key[index+i]["name"])
                except IndexError: break
            lines+=-i-1
        elif type(key) == dict:
            output.append(key["name"])
            lines-=1
        return output, lines

    def desc(lines, key, index, format):
        output=[]
        for i in range(lines):
            try: 
                try: output.append(key["desc"][index+i].format(format[i]))
                except IndexError: output.append(key["desc"][index+i])
            except IndexError: break
        return output, lines-i-1

    def option(lines, key, index, format):
        output, b=[], False
        for i in range(lines):
            if type(key) == list: 
                if type(key[i]) == str:
                    if i == index: output.append(">"+key[i])
                    else: output.append(" "+key[i])
                elif type(key[i]) == dict:
                    if i == index: output.append(">"+key[i]["name"])
                    else: output.append(" "+key[i]["name"])
                else: raise TypeError("only 'str' or 'dict' type can accept in the list")

            elif type(key) == str:
                output.append(key.format(format[0]))
                b=True

            else: raise TypeError("only 'list' or 'str' type can accept in the key 'option'")
        if Vars.get("actionsFolder") in __temp__: runAction(__temp__[Vars.get("actionsFolder")],index)
        return output, lines-i-1, index, b
    
    def __main__(lines, key, index, format, isIn=False):
        output=[]
        if isIn:
            desc(lines, key, index, format)
            option(lines, key, index, format)
        else: 
            output,lines=name(lines, key, index)
            return output


    lines, letters= int(screen.split("x")[0]), int(screen.split("x")[1])

    print(option(lines, key["option"], input, index, format))


def keys(key,main_menu):
    if key == "haut": 
        printer(main_menu[4],Vars.get("screen"),"",0,["|"])
        sleep(0.2)

    if key == "bas": 
        printer(main_menu[4],Vars.get("screen"),"",1,["|"])
        sleep(0.2)

    if key == "gauche":
        ...

    if key == "droite":
        ...

    if key == "enter":
        ...

    if key == "backspace":
        ...

    if key == "del": return True