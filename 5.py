import resources as r

algorithm_name = "Round-Robin"


# ----------------------------------- implementaçao do algoritmo --------------------------------------
def gerar_lista(processos_in, tempo_atual):
    proc = []
    for processo in processos_in:
        if processo.arrival_time <= tempo_atual:
            proc.append(processos_in.index(processo))
    return proc


def remover_processos(processos_in):
    proc2, tempos = [], []
    for proc in processos_in:
        if proc.tempo_exec != 0:
            proc2.append(proc)
        else:
            tempos.append(sum(proc.tempo_espera) / len(proc.tempo_espera))
    return [proc2, tempos]


def Round_Robin(processos_in, inicio, quantum):
    tempo_atual = inicio
    tempos = []
    for p in processos_in:
        if p.arrival_time < tempo_atual:
            processos_in.remove(p)
    while True:
        if len(processos_in) == 1:
            executaveis = [0]
        else:
            executaveis = gerar_lista(processos_in, tempo_atual)
        if len(executaveis) == 0:
            tempo_atual += 1
            print(
                "-------------------------------------------\n"
                "instante: %d -> Sem processos a serem executados\n"
                "-------------------------------------------\n" % tempo_atual)
            continue
        print("####################################\nprocessos sem executar:", len(processos_in))
        print("sequencia de processos sendo exeutados neste ciclo: %d \n####################################" % len(
            executaveis))
        for indx in executaveis:
            if not processos_in[indx].estado:
                processos_in[indx].estado = True
                if tempo_atual - processos_in[indx].arrival_time <= 0:
                    tempo = 0
                else:
                    tempo = tempo_atual - processos_in[indx].arrival_time
                processos_in[indx].tempo_espera.append(tempo)
            else:
                processos_in[indx].tempo_espera.append(quantum * len(executaveis))
            if processos_in[indx].tempo_exec >= quantum:
                processos_in[indx].tempo_exec = processos_in[indx].tempo_exec - quantum
                print(
                    "-------------------------------------------------\n"
                    "instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao restante: %f\n"
                    "---------------------------------------------------" % (
                        tempo_atual, processos_in[indx].nome, processos_in[indx].tempo_espera[-1],
                        processos_in[indx].tempo_exec))
                tempo_atual += quantum
            elif processos_in[indx].tempo_exec <= quantum:
                avanco = processos_in[indx].tempo_exec
                processos_in[indx].tempo_exec = 0
                print(
                    "-------------------------------------------------\n"
                    "instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao restante: %f\n"
                    "---------------------------------------------------" % (
                        tempo_atual, processos_in[indx].nome, processos_in[indx].tempo_espera[-1],
                        processos_in[indx].tempo_exec))
                print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                print("Processo %s terminou a sua execuçao" % processos_in[indx].nome)
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
                tempo_atual = tempo_atual + avanco
        result = remover_processos(processos_in)
        processos_in = result[0]
        tempos.append(result[1])
        if len(processos_in) == 0:
            break
    tempo_medio_espera = r.get_waiting_time_5(processos_in)
    r.display_process_end(tempo_atual, tempo_medio_espera, 1)


# -----------------------------------      criar processos     ---------------------------------------------
def criar_processos(numero):
    processos_in = []
    for n in range(numero):
        processos_in.append(r.Process(n + 1, input(f"Introduzir tempo de chegada do processo {n}: "),
                            input(f"Introduzir tempo de execuçao do processo {n}: ")))
        # processos_in.append(r.Process(n, randint(1,20),randint(1,20)))
    return processos_in


def ordenar_processos(processos_in):
    proc, tempos = [], []
    for processo in processos_in:
        tempos.append(processo.arrival_time)
    for i in sorted(tempos):
        for proce in processos_in:
            if proce.arrival_time == i and proce.ordem == 0:
                proc.append(proce)
                proce.ordem = 1
    return proc


# ------------------------------------- parametros do algoritmo ---------------------------------------------
r.display_algorithm_name(algorithm_name)
processos = criar_processos(int(input("Quantos processos deseja criar? ")))
# processos=criar_processos(randint(1,10))
if len(processos) == 0:
    r.exit_menu()
else:
    r.display_algorithm_name(algorithm_name)
    ordenados = ordenar_processos(processos)
    print("Tabela de Processos:")
    for ordenado in ordenados:
        print("nome:|%s| tempo de chegada:%f; tempo de execuçao: %f" % (
            ordenado.nome, ordenado.arrival_time, ordenado.tempo_exec))
    print()
    Round_Robin(ordenados, int(input("Qual é o instante inicial: ")), float(input("Qual é o quantum de tempo: ")))
    print("\n")
    r.exit_menu()
