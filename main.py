class Compromisso:
    data = None
    hora = None
    duracao = None
    descricao = None

listaDeCompromissos = []

def criaCompromisso(vetor):
    comp = Compromisso()

    comp.data = input("Digite a data do compromisso (dd/mm/aaaa): ")
    comp.hora = input("Digite a hora do compromisso: ")
    comp.duracao = input("Digite a duração em horas do compromisso: ")
    comp.descricao = input("Digite a descrição para seu compromisso: ")

    vetor.append(comp)
    print("Compromisso criado com sucesso!")
    menu()
    return vetor

def templateImpressao(compromisso):
    print("------------------------------------")
    print(f"Data do compromisso: {compromisso.data}")
    print(f"Hora do compromisso: {compromisso.hora}")
    print(f"Duração do compromisso (em horas): {compromisso.duracao}")
    print(f"Descrição do compromisso: {compromisso.descricao}")
    print("------------------------------------")

def filtro():
    data = input("Digite a data do evento: ")
    hora = input("Digite a hora do evento: ")

    for i in range(len(listaDeCompromissos)):
        if listaDeCompromissos[i].data == data and listaDeCompromissos[i].hora == hora:
            return listaDeCompromissos[i]


def consultarCompromisso():
    compromisso = filtro()
    if compromisso:
        templateImpressao(compromisso)
    else:
        print("Não foi encontrado nenhum compromisso correspondente!")
    menu()

def editarCompromisso():
    compromisso = filtro()
    menu()

def excluirCompromisso():
    compromisso = filtro()
    menu()


def mostraCompromisso(vetor):
    if vetor:
        for i in range(len(vetor)):
            templateImpressao(vetor[i])
    else:
        print("Não existem eventos na sua agenda!")
    
    menu()
    

def menu():
    print("------------------------------------")
    print("Opções da agenda:")
    print("Opção 1: Criar compromisso")
    print("Opção 2: Consultar compromissos")
    print("Opção 3: Alterar compromisso")
    print("Opção 4: Excluir compromisso")
    print("Opção 5: Mostrar todos os seus compromissos")
    print("Opção 6: Sair")
    print("------------------------------------")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        criaCompromisso(listaDeCompromissos)
    elif opcao == 2:
        consultarCompromisso()
    elif opcao == 3:
        editarCompromisso()
    elif opcao == 4:
        excluirCompromisso()
    elif opcao == 5:
        mostraCompromisso(listaDeCompromissos)
    elif opcao == 6:
        print("Obrigado por usar a agenda!")
        print("Desenvolvido por Filipe Medeiros de Almeida")
    else:
        print("Opção inválida!")
        menu()

menu()

