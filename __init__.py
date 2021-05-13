from os import open, read
from json import loads


if __name__ == '__main__':
    from brain import __main__ as run
    
    dirr = "D:/propriétaire/Python Projects/poulailler/"
    run(loads(read(open(dirr+"menu.json", 2), 9999999)))
    

    