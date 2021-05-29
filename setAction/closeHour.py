from Vars import Vars
from Brain import Brain

def closeHour(statut, args):
    if statut == -1:
        close = Vars.GetSetting("close").split(":")
        return ([int(close[0])], [int(close[1])])
    
    else:
        Vars.SaveSetting("close", "{}:{}".format(args[0], args[1]))
        Brain.succes()
