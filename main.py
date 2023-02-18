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
    menu()
    return vetor

def consultarCompromisso():
    # função de consulta
    menu()

def editarCompromisso():
    #função de edição
    menu()

def excluirCompromisso():
    #função de exclusão
    menu()

def templateImpressão(compromisso):
    print(f"Data do compromisso: {compromisso.data}")
    print(f"Hora do compromisso: {compromisso.hora}")
    print(f"Duração do compromisso: {compromisso.duracao} horas")
    print(f"Descrição do compromisso: {compromisso.descricao}")
    print("-----------------------------------")

def mostraCompromisso(vetor):
    if vetor:
        for i in range(len(vetor)):
            templateImpressão(vetor[i])
    else:
        print("Não existem eventos na sua agenda!")
    
    menu()
    

def menu():
    print("----------------------------")
    print("Opções da agenda:")
    print("Opção 1: Criar compromisso")
    print("Opção 2: Consultar compromissos")
    print("Opção 3: Alterar compromisso")
    print("Opção 4: Excluir compromisso")
    print("Opção 5: Mostrar todos os seus compromissos")
    print("Opção 6: Sair")
    print("------------------------------")

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

