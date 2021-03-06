from random import randint
import resources as r

algorithm_name = "Por Prioridade"


# ----------------------------------- implementaçao do algoritmo --------------------------------------
def escolher_proximo(processos_in, tempo_atual):
    prioridade = 5000
    estados = []
    for processo in processos_in:
        if processo.tempo_exec > 0 and processo.arrival_time <= tempo_atual:
            if processo.prioridade < prioridade:
                prioridade = processo.prioridade
    for processo in processos_in:
        estados.append(processo.estado)
        if processo.prioridade == prioridade:
            return processos_in.index(processo)
    if False in estados:
        return "cont"
    return "break"


def ver_tempo_atual(processos_in, tempo_atual, indx):
    if processos_in[indx].estado2:
        return 0
    if processos_in[indx].tempo_interrompido == 0:
        tempo_de_espera = 0
        if processos_in[indx].arrival_time < tempo_atual:
            tempo_de_espera = tempo_atual - processos_in[indx].arrival_time
    else:
        tempo_de_espera = tempo_atual - processos_in[indx].tempo_interrompido
    return tempo_de_espera


def remover_processos(processos_in, tempo_atual):
    nomes = []
    pro = []
    for processo in processos_in:
        if processo.arrival_time < tempo_atual:
            nomes.append(processo.nome)
    for processo in processos_in:
        if processo.nome not in nomes:
            pro.append(processo)
    return pro


def Por_Prioridade(processos_in, inicio):
    tempo_atual = inicio
    processos_in = remover_processos(processos_in, tempo_atual)
    # while True:
    for i in range(200):
        if processos_in[0].arrival_time > tempo_atual:
            tempo_atual += 1
            continue
        indx = escolher_proximo(processos_in, tempo_atual)
        if indx == "break":
            break
        elif indx == "cont":
            print(
                "-------------------------------------------\n"
                "instante: %d -> Sem processos a serem executados\n"
                "-------------------------------------------\n" % tempo_atual)
            tempo_atual += 1
            continue
        processos_in[indx].tempo_exec -= 1
        print("\n-------------------------------------------------\ntempo interrompido: %d tempo de chegada: %d" % (
              processos_in[indx].tempo_interrompido, processos_in[indx].arrival_time))
        tempo_de_espera = ver_tempo_atual(processos_in, tempo_atual, indx)
        # processos_in[indx].estado = True
        print(
            "instante: %f executando:|%s| tempo de espera:%f; tempo de execuçao restante: %f\n"
            "---------------------------------------------------" % (
             tempo_atual, processos_in[indx].nome, tempo_de_espera, processos_in[indx].tempo_exec))
        processos_in[indx].tempo_espera.append(tempo_de_espera)
        tempo_atual += 1
        if processos_in[indx].tempo_exec <= 0:
            print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print("Processo %s terminou a sua execuçao" % processos_in[indx].nome)
            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
            processos_in[indx].estado = True
        if escolher_proximo(processos_in, tempo_atual) != indx and processos_in[indx].tempo_exec > 0:
            processos_in[indx].tempo_interrompido = tempo_atual
            processos_in[indx].estado2 = False
        else:
            processos_in[indx].estado2 = True
    tempo_medio_espera = r.get_waiting_time_3(processos_in)
    r.display_process_end(tempo_atual, tempo_medio_espera, 1)


# -----------------------------------      criar processos     ---------------------------------------------
def criar_processos(numero):
    processos_in = []
    for n in range(numero):
        # processos_in.append(Processo(n+1,input("Introduzir tempo de chegada do processo %d: "%n),
        # input("Introduzir tempo de execuçao do processo %d: "%n),input("Introduzir a prioridade do processo %d: "%n)))
        processos_in.append(r.Process(n, randint(1, 20), randint(1, 20), randint(-20, 20)))
    return processos_in


# ------------------------------------- parametros do algoritmo ---------------------------------------------
r.display_algorithm_name(algorithm_name)
# processos=criar_processos(int(input("Quantos processos deseja criar? ")))
processos = criar_processos(randint(1, 10))
if len(processos) == 0:
    r.exit_menu()
else:
    r.display_algorithm_name(algorithm_name)
    ordenados = r.ordenar_processos(processos)
    print("Tabela de Processos:")
    for ordenado in ordenados:
        print("nome:|%s| tempo de chegada:%f; prioridade: %d" % (
         ordenado.nome, ordenado.arrival_time, ordenado.prioridade))
    print()
    Por_Prioridade(ordenados, int(input("Qual é o instante inicial: ")))
    print("\n")
    r.exit_menu()
