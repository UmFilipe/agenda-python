listaDeCompromissos = []

class compromisso():
    data = None
    hora = None
    duracao = None
    descricao = None

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
        menu()
    if opcao == 2:
        # função de consulta
        menu()
    if opcao == 3:
        # função de edição
        menu()
    if opcao == 4:
        #função de exclusão
        menu()
    if opcao == 5:
        mostraComprpmisso(listaDeCompromissos)
        menu()
    if opcao == 6:
        print("Obrigado por usar a agenda!")
        print("Desenvolvido por Filipe Medeiros de Almeida")

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

def mostraComprpmisso(vetor):
    print(vetor)

menu()

