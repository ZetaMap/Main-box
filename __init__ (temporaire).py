from os import open, read
from Lib.json import loads
from Lib.keyboard import read_key
from Vars import Vars

if __name__ == '__main__':
    from brain import *

    Vars.load()
    main_menu=loads(read(open(Vars.dirr+"menu.json", 2), 9999999))

    for i in range(int(Vars.get("screen").split("x")[0])):
    	printer(main_menu[1],Vars.get("screen"),"",0,["|"])

    while True: 
    	keys(read_key(),main_menu)
