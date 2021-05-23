from Vars import Vars
from Brain import Brain

def chickenNumber(statut, args):
    Vars.save("chickens", args[0])
    Brain.succes()
