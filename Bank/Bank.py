# -*- coding: Windows-1250 -*-
# -*- coding: ISO-8859-2 -*-
import os


clients = [
    {
        "ID": 1,
        "IMIE": "Jan",
        "NAZWISKO": "Nowak",
        "NR_KONTA": "001",
        "SALDO": 1457.23
    },
    {
        "ID": 2,
        "IMIE": "Angnieszka",
        "NAZWISKO": "Kowalska",
        "NR_KONTA": "002",
        "SALDO": 3600.18
    },
    {
        "ID": 3,
        "IMIE": "Robert",
        "NAZWISKO": "Lewandowski",
        "NR_KONTA": "003",
        "SALDO": 2745.03
    },
    {
        "ID": 4,
        "IMIE": "Zofia",
        "NAZWISKO": "Plucińska",
        "NR_KONTA": "004",
        "SALDO": 7344.00
    },
    {
        "ID": 5,
        "IMIE": "Grzegorz",
        "NAZWISKO": "Braun",
        "NR_KONTA": "005",
        "SALDO": 455.38
    }
]

def Welcome():
    print("1 => LISTA WSZYSTKICH KLIENTÓW BANKU")
    print("2 => LOGOWANIE")
    print("3 => ZAKOŃCZ PROGRAM")

    choice = eval(input("WYBIERZ 1,2 LUB 3:"))

    if choice >=4 or choice <= 0:
        print("NIE MA TAKIEGO NUMERU NA LISCIE")
        Welcome()

    if choice == 1:
        os.system('cls')
        AllClients()

    if choice == 2:
        Transfers()

    if choice == 3:
        END()
    

def AllClients():
    print("ID | IMIĘ I NAZWISKO | NR KONTA | SALDO")
    for i in range(len(clients)):
        #print(list(map(itemgetter(1),clients[i].items()))[0], " | ", list(map(itemgetter(1),clients[i].items()))[1], list(map(itemgetter(1),clients[i].items()))[2], " | ", list(map(itemgetter(1),clients[i].items()))[3], " | ", list(map(itemgetter(1),clients[i].items()))[4])
        print(clients[i]['ID'], "|", clients[i]['IMIE'], clients[i]['NAZWISKO'], "|", clients[i]['NR_KONTA'], "|", clients[i]['SALDO'])

def Transfers():
    os.system('cls')
    choiceID = eval(input("ZALOGUJ SIĘ PODAJĄC ID KLIENTA:"))
    for i in range(len(clients)):
        if (clients[i]['ID'] == choiceID):
            os.system('cls')
            print("                  ZALOGOWANY KLIENT:")
            print()
            print("ID:              ", clients[i]['ID'])
            print()
            print("IMIĘ I NAZWISKO: ", clients[i]['IMIE'], clients[i]['NAZWISKO'])
            print()
            print("NUMER KONTA:     ", clients[i]['NR_KONTA'])
            print()
            print("SALDO:           ", clients[i]['SALDO'])
            print()
            choiceAccount = input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAĆ PRZELEW:")
            os,os.system('cls')
            for j in range(len(clients)):
                if(clients[j]['NR_KONTA'] == choiceAccount):
                    if(clients[j]['NR_KONTA'] == clients[i]['NR_KONTA']):
                        print("NIE MOŻESZ ZROBIĆ PRZELEWU NA WŁASNE KONTO")
                    else:
                        amount = eval(input("PODAJ KWOTE PRZELEWU:"))
                        os.system('cls')
                        if(amount > clients[i]['SALDO']):
                            print("NIEWYSTARCZAJĄCE ŚRODKI NA RACHUNKU")
                        else:
                            clients[j]['SALDO']=clients[j]['SALDO']+amount
                            clients[i]['SALDO']=clients[i]['SALDO']-amount
                            print("PRZELEW ZOSTAŁ ZLECONY")
                            AllClients()
                    break
                elif (j == len(clients)-1):
                    print("NIEPRAWIDŁOWY NUMER KONTA")
            break
        elif (choiceID > len(clients)):
            print("LOGOWANIE NIEUDANE")
            break
    


def END():
    os.system('cls')
    print("Dziękujemy za skorzystanie z naszego systemu bankowego")

Welcome()
