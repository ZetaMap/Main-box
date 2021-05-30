from Vars import Vars

def getBilan(statut, args):
    if statut == -1:
        return (Vars.GetSetting("in"), Vars.GetSetting("out"))
