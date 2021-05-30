if __name__ == '__main__':
    from Brain import Brain
    from lib.keyboard import read_hotkey as keyInput

    Brain.init()
    
    print(Brain.back())

    while True:
        try: Brain.keys(keyInput(False), Brain.main_menu)
        except IndexError: ...
