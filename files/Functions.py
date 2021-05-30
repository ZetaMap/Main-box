from Vars import Vars

def StartEvent(file, position, *args):
    try:
        exec("from {}.{} import {}".format(Vars.GetSetting("EventsFolder"), file, file))
        return eval("{}({}, {})".format(file, position, args))
    except ModuleNotFoundError: raise FileNotFoundError("the file '"+file+".py' doesn't exist")
    except ImportError: raise ImportError("the main function: '"+file+"()', isn't defined in the file")
    except TypeError: raise Warning("the main function takes 2 positional arguments: (statut: int, args: tuple)")

def ScanSettings(key):
    if type(key) != dict: raise TypeError("type must be Dict only")

    try: default=key["default"]
    except KeyError: raise KeyError("must have a 'default' key in which default settings will be stored")
    try: custom=key["custom"]
    except KeyError: raise KeyError("must have a 'custom' key in which user settings will be stored")
    if type(key["default"]) != dict: raise TypeError("'default' must only be of type Dict")
    if type(key["custom"]) != dict: raise TypeError("'custom' must only be of type Dict")

    if not "screen" in key["default"]: raise KeyError("a 'screen' key must be created in key 'default' and must respect this form: '<lines>x<letters>'")
    if not "EventsFolder" in key["default"]: raise KeyError("a 'EventsFolder' key must be created in key 'default' and must contain the name of the folder where the 'Events' files are located")

    if custom == {}: custom = Vars.CreateSettings()["custom"]
    else:
        for i in default: 
            if not i in custom: custom.update({i: default[i]})
        Vars.SaveSettingAll(custom)
    return custom

def ScanMenu(key, keyDir=0, keyLater="main_menu"):
    output=()

    for i in range(len(key)):
        output=output.__add__(({"index": i},))
        output[i].update({"later": keyLater})

        if type(key[i]) == dict:
            if not key[i].__contains__("name"): raise KeyError("must contain a non-empty 'name' key")
            elif type(key[i]["name"]) != str: raise TypeError("the key 'name' must be a Str")
            elif key[i]["name"] == "": raise ValueError("please don't use an empty Str")

            if not key[i].__contains__("desc"): raise KeyError("must contain a 'desc' key, empty or not")
            elif type(key[i]["desc"]) != list: raise TypeError("the key 'desc' must be a List")
            elif key[i]["desc"] == []: output[i].update({"emptyDesc": True})
            else: 
                for ii in key[i]["desc"]: 
                    if type(ii) != str: raise TypeError("the list of key 'desc' can accept only Str type")
                output[i].update({"emptyDesc": False})
                output[i].update({"intoDesc": ScanMenu(key[i]["desc"], keyDir+1, "{}[{}]['desc']".format(keyLater, i))})
                for ii in key[i]["desc"]:
                    try: ii.format()
                    except IndexError:
                        switchValues = StartEvent(key[i]["StartEvent"], -1, ())
                        if not type(switchValues) == tuple: raise TypeError("the values returned by '{}()' must be of type Tuple".format(key[i]["StartEvent"]))
                        output[i]["intoDesc"]+=({"switchValues": switchValues},)
                        break
                   
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
                            
                        if key[i].__contains__("StartEvent"): # The function will be run with index -1, you can use it to return a list of values. Ex: ([0], [1])"
                            switchValues = StartEvent(key[i]["StartEvent"], -1, ())
                            if not type(switchValues) == tuple: raise TypeError("the values returned by '{}()' must be of type Tuple".format(key[i]["StartEvent"]))
                        else: switchValues = ()
                        
                        output[i].update({"switchValues": switchValues})
            else: 
                output[i].update({"isASwitch": False})
                output[i].update({"intoOption": ScanMenu(key[i]["option"], keyDir+1, "{}[{}]['option']".format(keyLater, i))})

        elif type(key[i]) == str: 
            if key[i] == "": raise ValueError("please don't use an empty Str")
            
        else: raise TypeError("the key can only accept Str and Dict types")
    return output
