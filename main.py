from random import randint
from time import sleep
import emoji
#Placar computador e jogador
comp_cont = 0
j_cont = 0
 
itens = ('Pedra', 'Papel', 'Tesoura')
#Computador escolhe primeira jogada
computador = randint(0,2)
print('''\033[33mDigite 4 para sair.
[0] Pedra
[1] Papel 
[2] Tesoura
''' )
jogador = int(input('Escoha uma das opções acima: '))
print('JO...')
sleep(1.5)
print('KEN...')
sleep(1.5)
print('PO!!!')
 
#Funções de escolha de Emoji
def jog_comp(computador):
    if computador == 0:
        print (emoji.emojize(':right-facing_fist:', language='en'))
    elif computador == 1:
        computador = (emoji.emojize(':raised_back_of_hand:', language='en'))
    elif computador == 2:
        computador = (emoji.emojize(':victory_hand:', language='en'))
 
def jog_jogador(jogador):
    if jogador == 0:
        print (emoji.emojize(':left-facing_fist:', language='en'))
    elif jogador == 1:
        print (emoji.emojize(':raised_back_of_hand:', language='en'))
    elif jogador == 2:
        print(emoji.emojize(':victory_hand:', language='en'))
 
#Enquanto jogador escolher de 0 a 2, o jogo segue.
while jogador == 0 or jogador == 1 or jogador == 2:
    #Jogadas possíveis
    if computador == 0 and jogador == 1:
        print('-='*15)
        #resultado da jogada ###EMOJI entra aqui####
        print('Você venceu! Escolhi {}.'.format(itens[computador], jog_jogador(jogador),(jog_comp(computador))))
        #computa resultado
        j_cont += 1
        #computador grava próxima jogada
        computador = randint(0,2)
        #placar
        print('jogador {} X {} Computador'.format(j_cont, comp_cont))
        #jogador joga novamente
        jogador = int(input('Jogue novamente: '))
        # Se jogador escolher maior que 2, loop termina
        if jogador > 2:
            break
        print('JO...')
        sleep(1.5)
        print('KEN...')
        sleep(1.5)
        print('PO!!!')
        print('-='*15)
    elif computador == 0 and jogador == 2:
        print('-='*15)
        print('Venci! Escolhi {}.'.format(itens[computador], jog_jogador(jogador), (jog_comp(computador))))
        comp_cont += 1
        computador = randint(0,2)
        print(f'jogador {j_cont} X {comp_cont} Computador')
        jogador = int(input('Jogue novamente: '))
        # Se jogador escolher maior que 2, loop termina
        if jogador > 2:
            break
        print('JO...')
        sleep(1.5)
        print('KEN...')
        sleep(1.5)
        print('PO!!!')
        print('-='*15)
    elif computador == 1 and jogador == 0:
        print('-='*15)
        print('Venci! Escolhi {}.'.format(itens[computador], jog_jogador(jogador), jog_comp(computador)))
        comp_cont += 1
        computador = randint(0,2)
        print('jogador {} X {} Computador'.format(j_cont, comp_cont))
        jogador = int(input('Jogue novamente: '))
        # Se jogador escolher maior que 2, loop termina
        if jogador > 2:
            break
        print('JO...')
        sleep(1.5)
        print('KEN...')
        sleep(1.5)
        print('PO!!!')
        print('-='*15)
    elif computador == 1 and jogador == 2:
        print('-='*15)
        print('Você venceu! Escolhi {}'.format(itens[computador], jog_jogador(jogador), jog_comp(computador)))
        j_cont += 1
        computador = randint(0,2)
        print('jogador {} X {} Computador'.format(j_cont, comp_cont))
        jogador = int(input('Jogue novamente: '))
        # Se jogador escolher maior que 2, loop termina
        if jogador > 2:
            break
        print('JO...')
        sleep(1.5)
        print('KEN...')
        sleep(1.5)
        print('PO!!!')
        print('-='*15)
    elif computador == 2 and jogador == 0:
        print('-='*15)
        print('Você venceu! Esoclhi {}.'.format(itens[computador], jog_jogador(jogador), jog_comp(computador)))
        j_cont += 1
        computador = randint(0,2)
        print('jogador {} X {} Computador'.format(j_cont, comp_cont))
        jogador = int(input('Jogue novamente: '))
        # Se jogador escolher maior que 2, loop termina
        if jogador > 2:
            break
        print('JO...')
        sleep(1.5)
        print('KEN...')
        sleep(1.5)
        print('PO!!!')
        print('-='*15)
    elif computador == 2 and jogador == 1:
        print('-='*15)
        print('Venci! Escolhi {}'.format(itens[computador], jog_jogador(jogador), jog_comp(computador)))
        comp_cont += 1
        computador = randint(0,2)
        print('jogador {} X {} Computador'.format(j_cont, comp_cont))
        jogador = int(input('Jogue novamente: '))
        # Se jogador escolher maior que 2, loop termina
        if jogador > 2:
            break
        print('JO...')
        sleep(1.5)
        print('KEN...')
        sleep(1.5)
        print('PO!!!')
        print('-='*15)
 
    #Empate
    elif computador == jogador:
        print('-='*15)
        print('Empate!!! Jogamos {}'.format(itens[computador], jog_jogador(jogador), jog_comp(computador)))
        print('jogador {} X {} Computador'.format(j_cont, comp_cont))
        computador = randint(0,2)
        jogador = int(input('Jogue novamente: '))
        # Se jogador escolher maior que 2, loop termina
        if jogador > 2:
            break
        print('JO...')
        sleep(1.5)
        print('KEN...')
        sleep(1.5)
        print('PO!!!')
        print('-='*15)
 
 
#Mostra placar final
if comp_cont < j_cont:
    print('Jogador Venceu!!! Você foi genial.')
if comp_cont == j_cont:
    print('Empatamos. Vamos de novo?')
if comp_cont > j_cont:
    print('Computador venceu!!!\nMais sorte da próxima vez!')
print('jogador {} X {} Computador\nPLACAR FINAL!!!'.format(j_cont, comp_cont))
