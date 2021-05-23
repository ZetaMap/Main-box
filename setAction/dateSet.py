from Vars import Vars
from Brain import Brain

def dateSet(statut, args):
    Vars.save("date", "{}/{}/{}".format(args[0], args[1], args[2]))
    Brain.succes()
