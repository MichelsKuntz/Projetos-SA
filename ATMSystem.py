# Equipe: William B., Lucas M., Marlon e André
# Sistema de Caixa Eletrônico / ATM's System
# S.A - Prof. Golle - 1º Semeste

import os
import time

userBank = ["Joaquim", "Joao","Admin"]
passBank = [132, 321, 1425]
mnyBank = [2000, 2000, 0]
totCed = 0
totCed50 = 100
totCed20 = 100
totCed10 = 100
totCed1 = 100

os.system("cls")

while True:
    print('=' * 30)
    print("")
    print('{:^30}'.format("Seja Bem Vindo ao Caixa 24h!"))
    print("")
    print('=' * 30)

    user = input("Usuário: ")
    password = int(input("Senha: "))
    os.system("cls")
    i = 0
    for i in range(userBank[i] and passBank[i]):
        if user == userBank[i] and password == passBank[i]:
            totBank = (totCed50*50)+(totCed20*20)+(totCed10*10)+totCed1
    
            print('=' * 30)
            print('{:^30}'.format("Seja Bem Vindo, {}!".format(userBank[i])))
            print("")
            print('{:^30}'.format("Seu saldo atual é de: B${}!".format(mnyBank[i])))
            print('=' * 30)
            print("")
            saque = int(input("Digite o Valor do Saque: "))
            print("")
            os.system("cls")
            if saque <= mnyBank[i] and saque <= totBank and saque <= 1000 and saque > 0:
                mnyBank[i] -= saque
                cedAtual = 50
                while True:
                    if saque >= cedAtual:
                        saque -= cedAtual
                        totCed += 1
                        if cedAtual == 50:
                            totCed50 -= 1
                        else:
                            if cedAtual == 20:
                                totCed20 -= 1
                            else:
                                if cedAtual == 10:
                                    totCed10 -= 1
                                else:
                                    if cedAtual == 1:
                                        totCed1 -= 1
                    else:
                        if totCed > 0:
                            print("{} cédulas de B$ {}".format(totCed, cedAtual))
                        if cedAtual == 50 or totCed50 <= 0:
                            cedAtual = 20
                        else:
                            if cedAtual == 20 or totCed20 <= 0:
                                cedAtual = 10
                            else:
                                if cedAtual == 10 or totCed10 <= 0:
                                    cedAtual = 1
                        totCed = 0
                        if saque == 0:
                            break
                time.sleep(5)
                os.system("cls")
                print("Aguardando retirada das Cédulas...")
                time.sleep(5)
                os.system("cls")
                print('{:^30}'.format("Saque Realizado com Sucesso! Volte Sempre!"))
                time.sleep(5)
                os.system("cls")
            else:
                while True:
                    if saque > mnyBank[i]:
                        os.system("cls")
                        print("Saldo Insuficiente!")
                        time.sleep(5)
                        os.system("cls")
                        saque = int(input("Digite o Valor do Saque: "))
                        os.system("cls")
                    else:
                        if saque > totBank:
                            os.system("cls")
                            print("O Caixa só tem B${}".format(totBank))
                            time.sleep(5)
                            os.system("cls")
                            saque = int(input("Digite o Valor do Saque: "))
                            os.system("cls")
                        else:
                            if saque > 1000:
                                os.system("cls")
                                print("Só se pode sacar B$1.000,00 por vez!")
                                time.sleep(5)
                                os.system("cls")
                                saque = int(input("Digite o Valor do Saque: "))
                                os.system("cls")
                            else:
                                if saque == 0:
                                    print("Caixa encerrado!")
                                    break
            break
        else:
            if user != userBank[i] and password != passBank[i]:
                i+=1
            else:
                print("Usuário ou Senha Incorretos!")
                break
    if saque == 0:
        break