from Vars import Vars
from Brain import Brain

def openHour(statut, args):
    Vars.save("open", "{}:{}".format(args[0], args[1]))
    Brain.succes()
