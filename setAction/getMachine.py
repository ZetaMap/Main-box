from Vars import Vars

def getMachine(statut, args):
    if statut == -1:
        _in = Vars.GetSetting("in")
        _out = Vars.GetSetting("out")
        prod = 't' # insérer code pour voir la production
        conso = 't' # insérer code pour voir la consomation
        bat = 't' # insérer code pour voir la batterie
        
        return ([bat], [prod], [conso], [_in], [_out])
