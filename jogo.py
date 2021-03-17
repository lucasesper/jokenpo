import random



print("Bem vindo ao torneio de pedra, papel e tesoura!\n")
print("FASE 1")

def partida():
    vitoria = 0
    derrota = 0
    while (vitoria < 2 and derrota < 2):
        jogador = int(input("Digite\n 1- pedra\n 2- papel\n 3- tesoura \n"))
        dado = random.randint(1,3)
        if dado == 1 and jogador == 1:
            print("Empate \n")
        if dado == 1 and jogador == 2:
            print("Você venceu!")
            vitoria += 1
            
        if dado == 1 and jogador == 3:
            print("Você perdeu!")
            derrota += 1
            
        if dado == 2 and jogador == 1:
            print("Você perdeu!")
            derrota += 1
            
        if dado == 2 and jogador == 2:
            print("Empate!")
        if dado == 2 and jogador == 3:
            print("Você venceu!")
            
            vitoria += 1
        if dado == 3 and jogador == 1:
            print("Você venceu!")
            
            vitoria += 1
        if dado == 3 and jogador == 2:
            print("Você perdeu!")
            
            derrota += 1
        if dado == 3 and jogador == 3:
            print("Empate!")

    if vitoria == 2:
        print("Você passou de fase!\n Jogador: ", vitoria, "Computador: ", derrota)
        
    if derrota == 2 :
        print("Você foi eliminado!\n Jogador: ", vitoria, "Computador: ", derrota)
        jogar = int(input("Deseja jogar novamente? \n 1- SIM\n 2- NAO\n "))
        if jogar == 1:
            partida()
        if jogar == 2:
            print("Até a próxima!")
            return False
    return True
       
x = partida()
fase = 1
if x == True:
    fase += 1
    print("FASE 2")
    partida()
if fase == 2:
    print("Parabéns, você foi campeão do torneio!")

