from Vars import Vars
from Brain import Brain

def openHour(statut, args):
    if statut == -1:
        open = Vars.GetSetting("open").split(":")
        return ([open[0]], [open[1]])
        
    else:
        Vars.SaveSetting("open", "{}:{}".format(args[0], args[1]))
        Brain.succes()
