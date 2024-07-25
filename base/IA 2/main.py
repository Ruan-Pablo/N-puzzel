from menus.menu import menu as menu_module 

def main():
    cont = 1
    while(True):
        menu = menu_module()  
        print("(1): Busca em largura")     
        print("(2): Busca em profundidade iterativa")
        print("(3): Busca A* com heurística de quantidade de peças erradas")
        print("(4): Busca A* com heurística de distância de Manhattan")
        print("-------------------------------------------------------------------")
        case = int(input("Escolha um algoritmo: "))
        menu.switch(case)
        
if __name__ == "__main__":
    main()