from Vars import Vars
from Brain import Brain

def dateSet(statut, args):
    if statut == -1:
        date = Vars.GetSetting("date").split("/")
        return ([date[0]], [date[1]], [date[2]])

    else:
        Vars.SaveSetting("date", "{}/{}/{}".format(args[0], args[1], args[2]))
        Brain.succes()
