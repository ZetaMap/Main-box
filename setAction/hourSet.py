from Vars import Vars
from Brain import Brain

def hourSet(statut, args):
    if statut == -1:
        hour = Vars.GetSetting("time").split(":")
        return ([int(hour[0])], [int(hour[1])])

    else:
        Vars.SaveSetting("time", "{}:{}".format(args[0], args[1]))
        Brain.succes()
