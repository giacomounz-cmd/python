from enemy import arduino,sigmaboy

from player import Player

player1=Player()

def difficulty():
    print("scegli tra le seguenti difficolta(metti il numero)")
    print("1 facile")
    print("2 difficile")
    scelta=input()
    match scelta:
        case "1":
            return 1
        case "2":
            return 1.5
        case _:
            return difficulty()

moltiplicatore=int(difficulty())
arduino1=arduino()
sigmaboy=sigmaboy()
arduino1=(arduino1.hp*moltiplicatore,arduino1.danno*moltiplicatore)
sigmaboy=(sigmaboy.hp*moltiplicatore,sigmaboy.danno*moltiplicatore)


