from os import system
from random import randint,random

def mostrar_algoritmo():
   system("cls")
   print("#########################################################################\n#######################     SJF(preemptivo)     #########################\n#########################################################################\n")

def sair():
    escolha = input("Deseja voltar ao Menu?\n  Sim............1\n  Nao............2 ")
    if escolha == "1":
        system("python Menu.py")
    else:
        system("cls")
        print("Obrigado,ate a proxima!!!")

#################### implementaçao do algoritmo ###################################
def calcular_t_espera(processos):
    tempos=[]
    for p in processos:
        tem=[]
        for i in p.tempo_espera:
            if p.tempo_espera.index(i)==0:
                tem.append(i)
            else:
                if i !=0:
                    tem.append(i)

        tempos.append(sum(tem)/len(tem))
    return sum(tempos)/len(tempos)

def escolher_proximo(processos,tempo_atual):
    tempo=5000
    estados=[]
    for processo in processos:
        if processo.tempo_exec!=0 and processo.tempo_chegada<=tempo_atual:
            if processo.tempo_exec<tempo:
                tempo=processo.tempo_exec
    for processo in processos:
        estados.append(processo.estado)
        if processo.tempo_exec==tempo:
            return processos.index(processo)
    if False in estados:
        return "cont"
    return "break"
def ver_tempo_atual(processos,tempo_atual,indx):
    if processos[indx].estado2==True:
        return 0
    if processos[indx].tempo_interrompido == 0:
        tempo_de_espera = 0
        if processos[indx].tempo_chegada < tempo_atual:
            tempo_de_espera = tempo_atual - processos[indx].tempo_chegada
    else:
        tempo_de_espera = tempo_atual - processos[indx].tempo_interrompido
    return tempo_de_espera

def remover_processos(processos,tempo_atual):
    nomes=[]
    pro=[]
    for processo in processos:
        if processo.tempo_chegada< tempo_atual:
            nomes.append(processo.nome)
    for processo in processos:
        if processo.nome not in nomes:
            pro.append(processo)
    return pro

def SJF_Preemptivo(processos, inicio):
    tempo_atual=inicio
    processos=remover_processos(processos,tempo_atual)
    while True:
        if processos[0].tempo_chegada>tempo_atual:
            tempo_atual+=1
            continue
        indx=escolher_proximo(processos,tempo_atual)
        if indx=="break":
            break
        elif indx=="cont":
            print("-------------------------------------------\ninstante: %d -> Sem processos a serem executados\n-------------------------------------------\n" % tempo_atual)
            tempo_atual+=1
            continue
        processos[indx].tempo_exec-=1
        print("-------------------------------------------\ntempo interrompido: %d tempo de chegada: %d"%(processos[indx].tempo_interrompido,processos[indx].tempo_chegada))
        tempo_de_espera=ver_tempo_atual(processos,tempo_atual,indx)
        processos[indx].estado = True
        print("\ninstante: %f executando:|%s| tempo de espera:%f; tempo de execuçao restante: %f\n---------------------------------------------------\n" % (tempo_atual, processos[indx].nome, tempo_de_espera,processos[indx].tempo_exec))
        processos[indx].tempo_espera.append(tempo_de_espera)
        tempo_atual += 1
        if processos[indx].tempo_exec==0:
            print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("Processo %s terminou a sua execuçao" % processos[indx].nome)
            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        if escolher_proximo(processos,tempo_atual) != indx and processos[indx].tempo_exec!=0:
            processos[indx].tempo_interrompido=tempo_atual
            processos[indx].estado2=False
        else:
            processos[indx].estado2=True
    tempo_medio_espera=calcular_t_espera(processos)
    print("\n----------------------------------------------------------------\nO processamento terminou no instante: %fseg.o tempo medio de espera é: %f seg"%(tempo_atual,tempo_medio_espera))

####################      criar processos     ######################################
class Processo (object):
    def __init__ (self,num,tc,te):
        self.nome = "P"+str(num)
        self.tempo_chegada=int(tc)
        self.tempo_exec = int(te)
        self.estado=False
        self.estado2=False
        self.tempo_interrompido = 0
        if random()<=50:
            self.type="CPU-Bound"
        else:
            self.type="I/O-Bound"
        self.tempo_espera=[]
        self.ordem=0

def criar_processos(numero):
    processos=[]
    for n in range(numero):
        #processos.append(Processo(n+1,input("Introduzir tempo de chegada do processo %d: "%n),input("Introduzir tempo de execuçao do processo %d: "%n)))
        processos.append(Processo(n, randint(1,20),randint(1,20)))
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
#processos=criar_processos(int(input("Quantos processos deseja criar? ")))
processos=criar_processos(randint(1,10))
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
    SJF_Preemptivo(ordenados,int(input("Qual é o instante inicial: ")))
    print("\n")
    sair()
