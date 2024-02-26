from blackjackPOO import *

class Juego:
    def __init__(self):
        self.mazo = Mazo()
        self.casa = Mazo(True)
        self.jugador = Mazo(True)
    
    def iniciar_juego(self):
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.casa.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        self.jugador.agregar_carta(self.mazo.dar_carta())
        
        print("¡Bienbenido a Blackjack!")
    
    def mostrar_juego(self):
        
        print("jugador:")
        self.jugador.mostrar_cartas()
        print("casa:")
        self.casa.mostrar_cartas()
        
    def dentro_juego_jugador(self):

            p1 = input("¿Quieres pedir una carta? y/n").lower()
            if p1 == 'y':
                self.jugador.agregar_carta(self.mazo.dar_carta())
                self.mostrar_juego()

                if self.jugador.dar_valor() > 21:
                    print("¡Has perdido!, la casa gana")
                    pf = input("¿Quieres intentarlo de nuevo? y/n").lower()
                    if pf == 'y':
                        self.iniciar_juego()
                    else:
                        print("!Hasta la próxima!")
                else:
                    self.dentro_juego_jugador()
            else:
                print("Te has plantado")
    

    def dentro_juego_casa(self):
        while self.casa.dar_valor()<17:
            self.casa.agregar_carta(self.mazo.dar_carta())
        self.mostrar_juego()


    def ganador(self):
        valorf_jugador = self.jugador.dar_valor()
        valorf_casa = self.casa.dar_valor()
        if valorf_jugador > 21:
            print("Ha ganado la casa")
        elif valorf_casa > 21:
            print("ha ganado el jugador")
        elif valorf_casa > valorf_jugador:
            print("ha ganado la casa")
        elif valorf_jugador > valorf_casa:
            print("ha ganado el jugador")
        else:
            print("ha ganado la casa (la casa gana si hay empate)")