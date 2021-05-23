from Vars import Vars

def doorStatut(statut, args):
    if statut == 0:
        Vars.save("door", True)
        # insérer code pour ouvrir la porte

    elif statut == 1:
        Vars.save("door", False)
        # insérer code pour fermer la porte

    if args[0]:
        from Brain import Brain
        Brain.back()
