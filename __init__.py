if __name__ == '__main__':
    from Brain import Brain
    
    Brain.init()
    
    print(Brain.back())

    """
    while True:
        try: Brain._print(Brain.keys(keyInput(False), Brain.main_menu))
        except IndexError: ...
    """