from os import system
from random import randint,random

def mostrar_algoritmo():
    system("cls")
    print("#########################################################################\n########################          FCFS          #########################\n#########################################################################\n")

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

def esperar(processos,tempo_atual):
    if processos[0].tempo_chegada>tempo_atual:
        tempo=processos[0].tempo_chegada-tempo_atual
        for i in range(tempo):
            print("-------------------------------------------\ninstante: %d -> Sem processos a serem executados\n-------------------------------------------\n" %i)
        return tempo
    else:
        return 0
def FCFS(processos,inicio):
    comeco,comeco2=True,False
    tempo_atual=inicio
    tempo_de_espera,tempos_de_espera=0,[]
    tempo_atual=esperar(processos,tempo_atual)+tempo_atual
    for proc in processos:
        if proc.tempo_chegada>=tempo_atual or comeco2==True:
            if comeco==True:
                print("instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao: %f\n---------------------------------------------------" % (proc.tempo_chegada, proc.nome, tempo_de_espera, proc.tempo_exec))
                tempo_atual+=proc.tempo_exec
                tempos_de_espera.append(0)
                comeco=False
                comeco2=True
            elif comeco==False:
                tempo_de_espera=calcular_t_espera(tempo_atual,proc.tempo_chegada)
                if proc.tempo_chegada> tempo_atual:
                    for i in range(proc.tempo_chegada-tempo_atual):
                        print("-------------------------------------------\ninstante: %d -> Sem processos a serem executados\n-------------------------------------------\n" %(i+tempo_atual))
                    tempo_atual = proc.tempo_chegada
                print("instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao: %f\n---------------------------------------------------" % (tempo_atual, proc.nome, tempo_de_espera, proc.tempo_exec))
                tempo_atual += proc.tempo_exec
                tempos_de_espera.append(tempo_de_espera)

    print("\n----------------------------------------------------------------\nO processamento terminou no instante: %fseg.o tempo medio de espera é: %f seg\n----------------------------------------------------------------\n"%(tempo_atual,sum(tempos_de_espera)/len(tempos_de_espera)))

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
    for ord in ordenados:
        print("nome:|%s| tempo de chegada:%d; tempo de execuçao: %d"%(ord.nome,ord.tempo_chegada,ord.tempo_exec))
    print()
    FCFS(ordenados,int(input("Qual é o instante inicial: ")))
    sair()


