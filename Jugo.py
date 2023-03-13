class Jugador01():
    def __init__(self, jugador1, luchador1, poder1):
        self.jugador1=jugador1
        self.luchador1=luchador1
        self.poder1=poder1

    def Juego(self):
        return 'El jugador {} tiene un {} con el {} 100%'.format(self.jugador1, self.luchador1, self.poder1)
    
boxeo= Jugador01('Enoc', 'Pedro', '100')
print(boxeo.Juego)

