from os import system
from random import randint,random

def mostrar_algoritmo():
   system("cls")
   print("#########################################################################\n######################     SJF(nao-preemptivo)     ######################\n#########################################################################\n")

def sair():
    escolha = input("Deseja voltar ao Menu?\n  Sim............1\n  Nao............2 ")
    if escolha == "1":
        system("python Menu.py")
    else:
        system("cls")
        print("Obrigado,ate a proxima!!!")
#################### implementaçao do algoritmo ###################################
def calcular_t_espera(tempo_atual,tempo_chegada):
    if tempo_chegada>=tempo_atual:
        return 0
    return tempo_atual-tempo_chegada

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
        tempo_de_espera = calcular_t_espera(tempo_atual,processos[proximo_processo].tempo_chegada)
        tempos_de_espera.append(tempo_de_espera)
        processos.remove(processos[proximo_processo])
        proximo_processo=escolher_proximo(processos,tempo_atual)
        if len(processos)==0:
            break
    print("\n----------------------------------------------------------------\nO processamento terminou no instante: %fseg.o tempo medio de espera é: %f seg\n----------------------------------------------------------------\n" % (tempo_atual, sum(tempos_de_espera) / len(tempos_de_espera)))

####################      criar processos     ######################################
class Processo (object):
    def __init__ (self,num,tc,te):
        self.nome = "P"+str(num)
        self.tempo_chegada=int(tc)
        self.tempo_exec = int(te)
        self.estado=False
        if random()<=50:
            self.type="CPU-Bound"
        else:
            self.type="I/O-Bound"
        self.waiting_time=0
        self.ordem=0

def criar_processos(numero):
    processos=[]
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
mostrar_algoritmo()
processos=criar_processos(int(input("Quantos processos deseja criar? ")))
#processos=criar_processos(randint(1,10))
if len(processos)==0:
######################## sair do algoritmo atual ###################################
    sair()
else:
    mostrar_algoritmo()
    ordenados=ordenar_processos(processos)
    print("Tabela de Processos:")
    for ordenado in ordenados:
        print("nome:|%s| tempo de chegada:%f; tempo de execuçao: %f"%(ordenado.nome,ordenado.tempo_chegada,ordenado.tempo_exec))
    print()
    SJF_N_preemptivo(ordenados,int(input("Qual é o instante inicial: ")))
    print()
    sair()
