from Brain import Brain

def USBExport(statut, args):
    if statut == -1:
        return ([], [])

    elif statut == 1:
        print("Veuillez brancher")
        print("une clé USB ...")

        try:
            # inséser code pour l'exportation
        except:
            print("Erreur : fichier")
            print("non exporter !")
        finally:
            print("Fichier exporter")
            print("avec succès !")

        Brain.back()

    else: Brain.back()
    
