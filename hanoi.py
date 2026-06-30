from datetime import time

class Hanoi(object):
    # print("\u2534")  ┴
    # print("\u2502")  │
        
    def __init__(self, N_DISC=3, N_TOR=3):
        self.N_Disc = N_DISC
        self.N_Tor = N_TOR
        self.tab = [[] for _ in range(N_TOR)]
        self.iniciar_tab()

    def iniciar_tab(self):
        
        for i in range(self.N_Disc):
            self.tab[0].append(i+1)
        
    def __repr__(self):
        
        inv = [torre[:] for torre in self.tab] # invertir el orden de impresion
        for i in inv:
            i.reverse()

        for i in range(self.N_Disc-1, -1, -1): # empezar desde el final
            for t in inv:
                if i < len(t):
                    print(t[i], end="  ")

                else:
                    print("\u2502", end="  ")

            print()
        
        for i in range(self.N_Tor): # imprimir pie de torres
            print("\u2534" ,end="  ")
        
        print()

        for i in range(self.N_Tor): # imprimir letras de torres
            print(chr(65+i) ,end= "  ")
        
        print()

    def movimiento(self, origen, destino):
        ori,des = self.conversion_num(origen, destino)

        if self.mov_valido(ori,des):
            disc_origen = self.tab[ori].pop(0)
            self.tab[des].insert(0,disc_origen)

    def mov_valido(self, ori, des):
        disc_origen = self.tab[ori][0]

        if len(self.tab[des]) >0:
            disc_dest = self.tab[des][0]
            if disc_dest < disc_origen:
                print("Movimiento invalido")
                return False
            
        return True

    def fin_partida(self):
        return len(self.tab[1]) == self.N_Disc or len(self.tab[2]) == self.N_Disc
    
    def conversion_num(self, origen, destino):
        num1 = ord(origen)-65 
        num2 = ord(destino)-65

        return num1, num2
    
def main():
    opciones = [1,2,3]
    
    
    while True:
        op = None

        print("Bienvenido al juego de las Torres de Hanoi")
        print(" 1. Juego manual\n 2. Juego automatico\n 3. Salir")

        while(op not in opciones):
            op = int(input("Seleccione una opción: "))

        if op == 3:
            print("Gracias por jugar")
            break

        if op == 1:
            jugar = True
            otra = None

            while jugar:
                juego = Hanoi()
                while(not juego.fin_partida()):
                    juego.__repr__()

                    try:

                        entrada = input("Movimiento: (Ej: A B) ").strip().upper()
                        origen = entrada.split(" ")[0]
                        destino = entrada.split(" ")[1]
                        juego.movimiento(origen,destino)

                    except Exception as e:
                        print("Error al mover")

                juego.__repr__()   
                print("Fin del juego")
                
                while(otra not in ["S","N"]):
                    otra = input("¿Otra partida? [S/N]: ").strip().upper()

                if otra != "S":
                    jugar = False 

    
if __name__ == '__main__':
    main()