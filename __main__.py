from menu import *

lines=5
letters=20
screen="2x20"

def printer(key, input, screen, index=0, format=[]):
    def name(lines, key, index):
        output=[]
        for i in range(lines):
            try: output.append(key[index+i]["name"])
            except IndexError: break
        return output, lines-i-1
    
    def desc(lines, key, index, format):
        output=[]
        for i in range(lines):
            try: 
                try:
                    output.append(key["desc"][index+i].format(format[i]))
                except IndexError: output.append(key["desc"][index+i])
            except IndexError: break
        return output, lines-i-1

    def option(lines, key, index, format, isIn=False):
        ...


    print(desc(2, key, index, format))

printer(main_menu[5],"","",0,["|"])


def printing(key,object_=main_menu,index=0):
    for i in range(lines):
        try:
            menu=object_[i]
            """
            if type(menu[object_]) == list: 
                if type(menu[object_][i]) == dict: print(menu[object_][i]["name"])
            
            else: 
            """
            print(menu[key])
        except IndexError: break

