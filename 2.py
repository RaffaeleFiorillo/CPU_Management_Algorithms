import resources as r

algorithm_name = "SJF(nao-preemptivo)"


# ----------------------------------- implementaçao do algoritmo --------------------------------------
def escolher_proximo(processos_in, tempo_atual):
    if len(processos_in) == 1:
        return 0
    tempos = []
    for processo in processos_in:
        if tempo_atual >= processo.arrival_time:
            tempos.append(processo.tempo_exec)
    if len(tempos) == 0:
        return "1"
    menor_tempo = min(tempos)
    for processo in processos_in:
        if processo.tempo_exec == menor_tempo:
            return processos_in.index(processo)


def SJF_N_preemptivo(processos_in, inicio):
    tempo_atual = inicio
    first, comecar, primeiro = 0, False, True
    tempos_de_espera = []
    tempo_de_espera = 0
    proximo_processo = 0
    while True:
        if type(proximo_processo) is str:
            tempo_atual += 1
            tempo_de_espera = 0
            proximo_processo = 0
            continue
        if processos_in[proximo_processo].arrival_time < tempo_atual and primeiro:
            processos_in.remove(processos_in[proximo_processo])
            proximo_processo += 1
            continue
        elif processos_in[proximo_processo].arrival_time >= tempo_atual:
            first = processos_in[proximo_processo].arrival_time
            comecar, primeiro = True, False
        if comecar:
            tempo_atual = first
            tempo_de_espera = 0
            comecar = False
        print(
            "\n---------------------------------------------------\n"
            "instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao: %f\n"
            "---------------------------------------------------" %(
             tempo_atual, processos_in[proximo_processo].nome, tempo_de_espera,
             processos_in[proximo_processo].tempo_exec))
        tempo_atual += processos_in[proximo_processo].tempo_exec
        tempo_de_espera = r.get_waiting_time_1(tempo_atual, processos_in[proximo_processo].arrival_time)
        tempos_de_espera.append(tempo_de_espera)
        processos_in.remove(processos_in[proximo_processo])
        proximo_processo = escolher_proximo(processos_in, tempo_atual)
        if len(processos_in) == 0:
            break
    r.display_process_end(tempo_atual, tempos_de_espera)


# ------------------------------------      criar processos     --------------------------------------------------------
def criar_processos(numero):
    processos_in = []
    for n in range(numero):
        processos_in.append(r.Process(n + 1, input("Introduzir tempo de chegada do processo %d: " % n),
                            input("Introduzir tempo de execuçao do processo %d: " % n)))
        # processos_in.append(Processo(n, randint(1,20),randint(1,20)))
    return processos_in


# ------------------------------------- parametros do algoritmo ---------------------------------------------
r.display_algorithm_name(algorithm_name)
processos = criar_processos(int(input("Quantos processos deseja criar? ")))
# processos=criar_processos(randint(1,10))
if len(processos) == 0:
    r.exit_menu()
else:
    r.display_algorithm_name(algorithm_name)
    ordenados = r.ordenar_processos(processos)
    print("Tabela de Processos:")
    for ordenado in ordenados:
        print("nome:|%s| tempo de chegada:%f; tempo de execuçao: %f" % (
              ordenado.nome, ordenado.arrival_time, ordenado.tempo_exec))
    print()
    SJF_N_preemptivo(ordenados, int(input("Qual é o instante inicial: ")))
    print()
    r.exit_menu()
