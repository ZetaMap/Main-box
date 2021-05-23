from Vars import Vars
from Brain import Brain

def closeHour(statut, args):
    if statut == -1:
        close = Vars.GetSetting("close").split(":")
        return ([close[0]], [close[1]])
    
    else:
        Vars.SaveSetting("close", "{}:{}".format(args[0], args[1]))
        Brain.succes()
