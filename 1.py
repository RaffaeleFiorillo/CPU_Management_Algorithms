import resources as r

algorithm_name = "FCFS"


#################### implementaçao do algoritmo ###################################

def esperar(processos,tempo_atual):
    if processos[0].tempo_chegada>tempo_atual:
        tempo=processos[0].tempo_chegada-tempo_atual
        for i in range(tempo):
            print("---------------------------------------------\n"
                  f"Instante: {i} -> Sem processos a serem executados\n"
                  "---------------------------------------------\n")
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
                tempo_de_espera=r.get_waiting_time_1(tempo_atual,proc.tempo_chegada)
                if proc.tempo_chegada> tempo_atual:
                    for i in range(proc.tempo_chegada-tempo_atual):
                        print("-------------------------------------------\ninstante: %d -> Sem processos a serem executados\n-------------------------------------------\n" %(i+tempo_atual))
                    tempo_atual = proc.tempo_chegada
                print("instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao: %f\n---------------------------------------------------" % (tempo_atual, proc.nome, tempo_de_espera, proc.tempo_exec))
                tempo_atual += proc.tempo_exec
                tempos_de_espera.append(tempo_de_espera)

    print("\n----------------------------------------------------------------\nO processamento terminou no instante: %fseg.o tempo medio de espera é: %f seg\n----------------------------------------------------------------\n"%(tempo_atual,sum(tempos_de_espera)/len(tempos_de_espera)))

####################      criar processos     ######################################


def criar_processos(numero):
    processos=[]
    for n in range(numero):
        processos.append(r.Process(n+1,input("Introduzir tempo de chegada do processo %d: "%n),input("Introduzir tempo de execuçao do processo %d: "%n)))
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


# ------------------------------------- parametros do algoritmo ---------------------------------------------
r.display_algorithm_name(algorithm_name)
processos=criar_processos(int(input("Quantos processos deseja criar? ")))
# processos=criar_processos(randint(1,10))
if len(processos)==0:
    r.exit_menu()  # exits current algorithm
else:
    r.display_algorithm_name(algorithm_name)
    ordenados=ordenar_processos(processos)
    print("Tabela de Processos:")
    for ord in ordenados:
        print("nome:|%s| tempo de chegada:%d; tempo de execuçao: %d"%(ord.nome,ord.tempo_chegada,ord.tempo_exec))
    print()
    FCFS(ordenados, int(input("Qual é o instante inicial: ")))
    r.exit_menu()


