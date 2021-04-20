from os import system
from random import choice
import resources as r

algorithm_name = "SJF(nao-preemptivo)"


def sair():
    escolha = input("Deseja voltar ao Menu?\n  Sim............1\n  Nao............2 ")
    if escolha == "1":
        system("python Menu.py")
    else:
        system("cls")
        print("Obrigado,ate a proxima!!!")


#################### implementaçao do algoritmo ###################################
def escolher_proximo(processos,tempo_atual):
    if len(processos)==1:
        return 0
    tempos=[]
    for processo in processos:
        if tempo_atual>=processo.tempo_chegada:
            tempos.append(processo.tempo_exec)
    if len(tempos)==0:
        return "1"
    menor_tempo=min(tempos)
    for processo in processos:
        if processo.tempo_exec==menor_tempo:
            return processos.index(processo)

def SJF_N_preemptivo(processos,inicio):
    tempo_atual=inicio
    first,comecar,primeiro=0,False,True
    tempos_de_espera=[]
    tempo_de_espera=0
    proximo_processo=0
    while True:
        if type(proximo_processo) is str:
            tempo_atual+=1
            tempo_de_espera=0
            proximo_processo=0
            continue
        if processos[proximo_processo].tempo_chegada<tempo_atual and primeiro==True:
            processos.remove(processos[proximo_processo])
            proximo_processo+=1
            continue
        elif processos[proximo_processo].tempo_chegada>=tempo_atual:
            first=processos[proximo_processo].tempo_chegada
            comecar,primeiro=True,False
        if comecar == True:
            tempo_atual=first
            tempo_de_espera=0
            comecar=False
        print("\n---------------------------------------------------\ninstante: %f executando:|%s| tempo de espera:%f; tempo de execuçao: %f\n---------------------------------------------------" % (tempo_atual, processos[proximo_processo].nome, tempo_de_espera, processos[proximo_processo].tempo_exec))
        tempo_atual+=processos[proximo_processo].tempo_exec
        tempo_de_espera = r.get_waiting_time_1(tempo_atual, processos[proximo_processo].tempo_chegada)
        tempos_de_espera.append(tempo_de_espera)
        processos.remove(processos[proximo_processo])
        proximo_processo=escolher_proximo(processos,tempo_atual)
        if len(processos)==0:
            break
    print("\n----------------------------------------------------------------\nO processamento terminou no instante: %fseg.o tempo medio de espera é: %f seg\n----------------------------------------------------------------\n" % (tempo_atual, sum(tempos_de_espera) / len(tempos_de_espera)))

# ------------------------------------      criar processos     --------------------------------------------------------
class Processo:
    estado = False
    type = choice(["CPU-Bound", "I/O-Bound"])
    waiting_time = 0
    ordem = 0

    def __init__(self, num, tc, te):
        self.nome = "P"+str(num)
        self.tempo_chegada=int(tc)
        self.tempo_exec = int(te)



def criar_processos(numero):
    processos = []
    for n in range(numero):
        processos.append(Processo(n+1,input("Introduzir tempo de chegada do processo %d: "%n),input("Introduzir tempo de execuçao do processo %d: "%n)))
        #processos.append(Processo(n, randint(1,20),randint(1,20)))
    return processos
def ordenar_processos(processos):
    proc,tempos=[],[]
    for processo in processos:
        tempos.append(processo.tempo_chegada)
    for i in sorted(tempos):
        for proce in processos:
             if proce.tempo_chegada==i and proce.ordem==0:
                proc.append(proce)
                proce.ordem=1
    return proc

#################### parametros do algoritmo ######################################
r.display_algorithm_name(algorithm_name)
processos=criar_processos(int(input("Quantos processos deseja criar? ")))
#processos=criar_processos(randint(1,10))
if len(processos)==0:
######################## sair do algoritmo atual ###################################
    r.exit_menu()
else:
    r.display_algorithm_name(algorithm_name)
    ordenados=ordenar_processos(processos)
    print("Tabela de Processos:")
    for ordenado in ordenados:
        print("nome:|%s| tempo de chegada:%f; tempo de execuçao: %f"%(ordenado.nome,ordenado.tempo_chegada,ordenado.tempo_exec))
    print()
    SJF_N_preemptivo(ordenados,int(input("Qual é o instante inicial: ")))
    print()
    r.exit_menu()
