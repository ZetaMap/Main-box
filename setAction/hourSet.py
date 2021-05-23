from Vars import Vars
from Brain import Brain

def hourSet(statut, args):
    Vars.save("time", "{}:{}".format(args[0], args[1]))
    Brain.succes()
