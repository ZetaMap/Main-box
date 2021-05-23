from Vars import Vars

def getMachine(statut, args):
    if statut == -1:
        _in = Vars.GetSetting("in")
        _out = Vars.GetSetting("out")
        prod = '' # insérer code pour voir la production
        conso = '' # insérer code pour voir la consomation
        bat = '' # insérer code pour voir la batterie
        
        return ([bat], [prod], [conso], [_in], [_out])
