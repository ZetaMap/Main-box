from Vars import Vars
from Brain import Brain

def closeHour(statut, args):
    Vars.save("close", "{}:{}".format(args[0], args[1]))
    Brain.succes()
