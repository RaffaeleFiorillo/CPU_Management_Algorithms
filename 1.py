import resources as r

algorithm_name = "FCFS"


# ----------------------------------- implementaçao do algoritmo ------------------------------------------------------

def esperar(processos_in, tempo_atual):
    if processos_in[0].arrival_time > tempo_atual:
        tempo = processos_in[0].arrival_time - tempo_atual
        for i in range(tempo):
            print("---------------------------------------------\n"
                  f"Instante: {i} -> Sem processos a serem executados\n"
                  "---------------------------------------------\n")
        return tempo
    else:
        return 0


def FCFS(processos_in, inicio):
    comeco, comeco2 = True, False
    tempo_atual = inicio
    tempo_de_espera, tempos_de_espera = 0, []
    tempo_atual = esperar(processos_in, tempo_atual) + tempo_atual
    for proc in processos_in:
        if proc.arrival_time >= tempo_atual or comeco2:
            if comeco:
                print("instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao: %f\n"
                      "---------------------------------------------------"
                      % (proc.arrival_time, proc.nome, tempo_de_espera, proc.tempo_exec))
                tempo_atual += proc.tempo_exec
                tempos_de_espera.append(0)
                comeco = False
                comeco2 = True
            else:
                tempo_de_espera = r.get_waiting_time_1(tempo_atual, proc.arrival_time)
                if proc.arrival_time > tempo_atual:
                    for i in range(proc.arrival_time - tempo_atual):
                        print(
                            "-------------------------------------------\n"
                            "instante: %d -> Sem processos a serem executados\n"
                            "-------------------------------------------\n" % (i + tempo_atual))
                    tempo_atual = proc.arrival_time
                print(
                    "instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao: %f\n"
                    "---------------------------------------------------" % (
                        tempo_atual, proc.nome, tempo_de_espera, proc.tempo_exec))
                tempo_atual += proc.tempo_exec
                tempos_de_espera.append(tempo_de_espera)
    r.display_process_end(tempo_atual, tempos_de_espera)


# -----------------------------------      criar processos     ---------------------------------------------
def criar_processos(numero):
    processos_in = []
    for n in range(numero):
        processos_in.append(r.Process(n + 1, input("Introduzir tempo de chegada do processo %d: " % n),
                                      input("Introduzir tempo de execuçao do processo %d: " % n)))
        # processos_in.append(Processo(n, randint(1,20),randint(1,20)))
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
    r.exit_menu()  # exits current algorithm
else:
    r.display_algorithm_name(algorithm_name)
    ordenados = ordenar_processos(processos)
    print("Tabela de Processos:")
    for orde in ordenados:
        print("nome:|%s| tempo de chegada:%d; tempo de execuçao: %d" % (orde.nome, orde.arrival_time, orde.tempo_exec))
    print()
    FCFS(ordenados, int(input("Qual é o instante inicial: ")))
    r.exit_menu()
