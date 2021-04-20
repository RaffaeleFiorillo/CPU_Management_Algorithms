from os import system

system("cls")
escolha=input("Algoritmos de Escalonamento:\n"
              "  FCFS........................1\n"
              "  SJF(nao-preemptivo).........2\n"
              "  SJF(preemptivo).............3\n"
              "  Por prioridade..............4\n"
              "  Round-Robin.................5\n"
              "  Sair........................6\n"
              "Qual algoritmo deseja executar? ")
if int(escolha)<6:
    system(f"python {escolha}.py")
else:
    system("cls")
    print("See you soon, Bye!!!")
