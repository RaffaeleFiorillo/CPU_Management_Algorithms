from os import system
import resources as r

algorithm_name = "Round-Robin"


def sair():
    escolha = input("Deseja voltar ao Menu?\n  Sim............1\n  Nao............2 ")
    if escolha == "1":
        system("python Menu.py")
    else:
        system("cls")
        print("Obrigado,ate a proxima!!!")

#################### implementaçao do algoritmo ###################################
def gerar_lista(processos,tempo_atual):
    proc=[]
    for processo in processos:
        if processo.tempo_chegada<=tempo_atual:
            proc.append(processos.index(processo))
    return proc

def remover_processos(processos):
    proc2,tempos=[],[]
    for proc in processos:
        if proc.tempo_exec!=0:
            proc2.append(proc)
        else:
            tempos.append(sum(proc.tempo_espera)/len(proc.tempo_espera))
    return [proc2,tempos]


def Round_Robin(processos,inicio,quantum):
    tempo_atual=inicio
    tempos=[]
    for p in processos:
        if p.tempo_chegada<tempo_atual:
            processos.remove(p)
    while True:
        if len(processos)==1:
            executaveis=[0]
        else:
            executaveis=gerar_lista(processos,tempo_atual)
        if len(executaveis)==0:
            tempo_atual+=1
            print("-------------------------------------------\ninstante: %d -> Sem processos a serem executados\n-------------------------------------------\n"%tempo_atual)
            continue
        print("####################################\nprocessos sem executar:", len(processos))
        print("sequencia de processos sendo exeutados neste ciclo: %d \n####################################"%len(executaveis))
        for indx in executaveis:
            if processos[indx].estado == False:
                processos[indx].estado = True
                if tempo_atual - processos[indx].tempo_chegada<=0:
                    tempo=0
                else:
                    tempo=tempo_atual - processos[indx].tempo_chegada
                processos[indx].tempo_espera.append(tempo)
            else:
                processos[indx].tempo_espera.append(quantum * len(executaveis))
            if processos[indx].tempo_exec>=quantum:
                processos[indx].tempo_exec=processos[indx].tempo_exec-quantum
                print("-------------------------------------------------\ninstante: %f executando:|%s| tempo de espera:%f; tempo de execuçao restante: %f\n---------------------------------------------------" % (tempo_atual, processos[indx].nome, processos[indx].tempo_espera[-1], processos[indx].tempo_exec))
                tempo_atual+=quantum
            elif processos[indx].tempo_exec<= quantum:
                avanco=processos[indx].tempo_exec
                processos[indx].tempo_exec = 0
                print("-------------------------------------------------\ninstante: %f executando:|%s| tempo de espera:%f; tempo de execuçao restante: %f\n---------------------------------------------------" % (tempo_atual, processos[indx].nome, processos[indx].tempo_espera[-1], processos[indx].tempo_exec))
                print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                print("Processo %s terminou a sua execuçao" % processos[indx].nome)
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
                tempo_atual = tempo_atual +avanco
        result=remover_processos(processos)
        processos=result[0]
        tempos.append(result[1])
        if len(processos) == 0:
            break
    tempo_medio_espera=r.get_waiting_time_5(processos)
    print("\n----------------------------------------------------------------\nO processamento terminou no instante: %fseg.o tempo medio de espera é: %f seg"%(tempo_atual,tempo_medio_espera))


####################      criar processos     ######################################
def criar_processos(numero):
    processos=[]
    for n in range(numero):
        processos.append(r.Process(n+1, input(f"Introduzir tempo de chegada do processo {n}: "),
                                   input(f"Introduzir tempo de execuçao do processo {n}: ")))
        # processos.append(r.Process(n, randint(1,20),randint(1,20)))
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
    sair()
else:
    r.display_algorithm_name(algorithm_name)
    ordenados=ordenar_processos(processos)
    print("Tabela de Processos:")
    for ordenado in ordenados:
        print("nome:|%s| tempo de chegada:%f; tempo de execuçao: %f"%(ordenado.nome,ordenado.tempo_chegada,ordenado.tempo_exec))
    print()
    Round_Robin(ordenados,int(input("Qual é o instante inicial: ")),float(input("Qual é o quantum de tempo: ")))
    print("\n")
    sair()