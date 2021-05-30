from Vars import Vars
from Brain import Brain

def chickenNumber(statut, args):
    if statut == -1:
        return (Vars.GetSetting("chickens"),)

    else:
        Vars.SaveSetting("chickens", args[0])
        Brain.succes()
