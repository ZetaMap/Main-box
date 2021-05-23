from Vars import Vars
from Brain import Brain

def hoursType(statut, args):
    if statut == 0:
        Vars.save("opening", True)
        Brain.succes()

    elif statut == 1:
        Vars.save("opening", False)
