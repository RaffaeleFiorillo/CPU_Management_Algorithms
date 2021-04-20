from random import choice as r_choice
from os import system


class Process:
    estado = False
    estado2 = False
    type = r_choice(["CPU-Bound", "I/O-Bound"])
    waiting_time = 0
    ordem = 0
    tempo_espera = []
    tempo_interrompido = 0

    def __init__(self, num, tc, te, prio=5):
        self.nome = "P" + str(num)
        self.arrival_time = int(tc)
        self.tempo_exec = int(te)
        self.prioridade=int(prio)


# asks for user input. Terminates the program, or sends user back to Main Menu
def exit_menu():
    choice = input("Do you wish to return to the Main Menu?\n"
                   "  Yes............1\n"
                   "  No............2 ")
    if choice == "1":
        system("python Menu.py")
    else:
        system("cls")
        print("See you soon, Bye!!!")


def display_algorithm_name(name):
    system("cls")
    spaces = (24-len(name))//2*" "
    print("##########################################################################\n"
          f"#########################{spaces}{name}{spaces}#########################\n"
          "##########################################################################\n")


def get_waiting_time_1(current_time, arrival_time):
    if arrival_time>=current_time:
        return 0
    return current_time-arrival_time


def get_waiting_time_3(processes):
    tempos=[]
    for p in processes:
        tem=[]
        for i in p.tempo_espera:
            if p.tempo_espera.index(i)==0:
                tem.append(i)
            else:
                if i !=0:
                    tem.append(i)

        tempos.append(sum(tem)/len(tem))
    return sum(tempos)/len(tempos)


def get_waiting_time_5(times):
    tempo_de_espera=[]
    for t in times:
        if len(t)!=0:
            tempo_de_espera.append(sum(t)/len(t))
    return sum(tempo_de_espera)/len(tempo_de_espera)
