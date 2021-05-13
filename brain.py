from Vars import *
from Lib.keyboard import is_pressed as keydown

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

    def option(lines, key, input, index, format):
        output,__temp__,key=[],key,key["option"]
        for i in range(lines):
            if type(key) == list: 
                if i == index: output.append(">"+key[i])
                else: output.append(" "+key[i])



        if Vars.get("actionsFolder") in __temp__: runAction(__temp__[Vars.get("actionsFolder")],index)
        return output, lines-i-1, index
    
    def __main__(lines, key, index, format, isIn=False):
        output=[]
        if isIn:
            desc(lines, key, index, format)
        else: 
            output,lines=name(lines, key, index)
            return output

    print(key)
    print(option(2, key, input, index, format))

def __main__(main_menu):
    printer(main_menu[0],"","",0,["|"])
