listaDeCompromissos = []

class compromisso():
    data = None
    hora = None
    duracao = None
    descricao = None

def criaCompromisso(vetor):
    comp = compromisso()

    comp.data = input("Digite a data do compromisso (dd/mm/aaaa): ")
    comp.hora = input("Digite a hora do compromisso: ")
    comp.duracao = input("Digite a duração em horas do compromisso: ")
    comp.descricao = input("Digite a descrição para seu compromisso: ")

    vetor.append(comp.data)
    vetor.append(comp.hora)
    vetor.append(comp.duracao)
    vetor.append(comp.descricao)
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

def mostraComprpmisso(vetor):
    print(vetor)
    menu()

def menu():
    print("Bem vindo a sua agenda!")
    print("Opções da agenda:")
    print("Opção 1: Criar compromisso")
    print("Opção 2: Consultar compromissos")
    print("Opção 3: Alterar compromisso")
    print("Opção 4: Excluir compromisso")
    print("Opção 5: Mostrar todos os seus compromissos")
    print("Opção 6: Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        criaCompromisso(listaDeCompromissos)
    if opcao == 2:
        consultarCompromisso()
    if opcao == 3:
        editarCompromisso()
    if opcao == 4:
        excluirCompromisso()
    if opcao == 5:
        mostraComprpmisso(listaDeCompromissos)
    if opcao == 6:
        print("Obrigado por usar a agenda!")
        print("Desenvolvido por Filipe Medeiros de Almeida")

menu()

