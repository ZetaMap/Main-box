if __name__ == '__main__':
    from Brain import Brain
    from lib.keyboard import read_hotkey as keyInput

    Brain.init()
    
    for i in Brain.name(Brain.back(), 0, Brain.lines)[0]:
    	print(i)

    while True:
        try: Brain.keys(keyInput(False))
        except IndexError: pass
	
