from datetime import time

class Hanoi(object):
    # print("\u2534")  ┴
    # print("\u2502")  │
        
    def __init__(self, N_Disc=5, N_TOR=3):
        self.N_Disc = N_Disc
        self.N_Tor = N_TOR
        self.tab = [[],[],[]]
        self.iniciar_tab()
    def iniciar_tab(self):
        
        for i in range(self.N_Disc):
            self.tab[0].append(i+1)
        
    def __repr__(self):
        
        print(self.tab)

    def movimiento(self, ori, des):
        if self.mov_valido(ori,des):
            disc_origen = self.tab[ori-1].pop(0)
            self.tab[des-1].insert(0,disc_origen)

    def mov_valido(self, ori, des):
        disc_origen = self.tab[ori-1][0]

        if len(self.tab[des-1]) >0:
            disc_dest = self.tab[des-1][0]
            if disc_dest < disc_origen:
                print("Movimiento invalido")
                return False
            
        return True

    def fin_partida(self):
        if len(self.tab[1]) == self.N_Disc or len(self.tab[2]) == self.N_Disc:
            return True
        
        return False
    
def main():
    opciones = [1,2,3]
    op = None
    print("Bienvenido al juego de las Torres de Hanoi")
    print(" 1. Juego manual\n 2. Juego automatico\n 3. Salir")

    while(op not in opciones):
        op = int(input("Seleccione una opción: "))

    juego = Hanoi()
    while(not juego.fin_partida()):
        juego.__repr__()
        entrada = input("Movimiento: ")
        origen = int(entrada.split(" ")[0])
        destino = int(entrada.split(" ")[1])
        juego.movimiento(origen,destino)

    juego.__repr__()    
    print("Fin del juego")
    
if __name__ == '__main__':
    main()