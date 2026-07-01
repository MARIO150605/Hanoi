from time import sleep

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
        
        self.movs=0
        
    def __repr__(self):

        #print(self.puntuar_movimientos(self.tab))
        inv = self.copia_tab(self.tab) # invertir el orden de impresion
        for i in inv:
            i.reverse()

        print(f"MOVIMIENTO #{self.movs}")
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

        if self.mov_valido(ori,des,self.tab):
            disc_origen = self.tab[ori].pop(0)
            self.tab[des].insert(0,disc_origen)
            self.movs+=1
        else:
            print("Movimiento invalido")

    def mov_valido(self, ori, des, tab):
        disc_origen = tab[ori][0]

        if len(tab[des]) >0:
            disc_dest = tab[des][0]
            if disc_dest < disc_origen:
                return False
            
        return True

    def fin_partida(self):
        for i in range(1,self.N_Tor):
            if len(self.tab[i]) == self.N_Disc:
                return True
            
        return False
    
    def conversion_num(self, origen, destino):
        num1 = ord(origen)-65 
        num2 = ord(destino)-65

        return num1, num2
    
    def copia_tab(self, tab):
        nuevo = [torre[:] for torre in tab]
        return nuevo
    
    def movimientos_posibles(self, tab):
        posibles = []

        for ori in range(self.N_Tor):
            if tab[ori]:
                
                for des in range(self.N_Tor):
                    if ori != des and self.mov_valido(ori,des,tab):
                        posibles.append((chr(65+ori),chr(65+des)))

        return posibles
    
    def puntuaciones(self, tab):

        # 🏆 victoria real
        for i in range(1, self.N_Tor):
            if tab[i] == list(range(1, self.N_Disc + 1)):
                return 3

        # 🟡 progreso real: torre parcialmente correcta
        for i in range(1, self.N_Tor):
            if tab[i] == list(range(1, len(tab[i]) + 1)):
                return 2

        # 🔴 cualquier otro caso
        return 1
    
    def puntuar_movimientos(self,tab):
        movimientos = self.movimientos_posibles(tab)
        punt={}
        
        for ori, des in movimientos:
            nuevo = self.simular_mov(tab,ord(ori)-65,ord(des)-65)
            puntuacion = self.puntuaciones(nuevo)
            punt[(ori,des)] = puntuacion

        return punt
    
    def simular_mov(self, tab, ori, des):

        nuevo = self.copia_tab(tab)

        d = nuevo[ori].pop(0)
        nuevo[des].insert(0,d)

        return nuevo

    def ordenar_puntuaciones(self, punt):
        puntuaciones = list(punt.items())

        for i in range(len(puntuaciones)): # ordenamiento por burbuja
            for j in range(0, len(puntuaciones)-i-1):

                if puntuaciones[j][1] < puntuaciones[j+1][1]:
                    puntuaciones[j], puntuaciones[j+1] = puntuaciones[j+1], puntuaciones[j]

        ordenado = {}

        for m, p in puntuaciones:
            ordenado[m] = p

        return ordenado
    
    def mejor_jugada(self):
        puntuaciones = self.puntuar_movimientos(self.tab)
        puntuaciones = self.ordenar_puntuaciones(puntuaciones)

        for ori, des in puntuaciones:

            nuevo = self.simular_mov(self.tab, ord(ori)-65,ord(des)-65)
            estado = self.estado(nuevo)

            if estado not in self.visitados:
                return (ori, des)

        return None
    
    def estado(self, tab):
        return tuple(tuple(torre) for torre in tab)
    
    def juego_auto(self):

        self.__repr__()

        self.visitados = set()
        while(not self.fin_partida()):
            
            jugada = self.mejor_jugada()
            ori = jugada[0]
            des = jugada[1]
            print(f"Movimiento: {ori} {des}")
            self.movimiento(ori,des)

            estado_actual = self.estado(self.tab)

            self.visitados.add(estado_actual)
            self.__repr__()

            sleep(1)


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
        
        if op == 2:
            juego = Hanoi()
            juego.juego_auto()

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