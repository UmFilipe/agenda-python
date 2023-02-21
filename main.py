# Classe base para criação de compromissos
class Compromisso:
    data = None
    hora = None
    duracao = None
    descricao = None

listaDeCompromissos = []

# Funções para reutilização de código
def templateImpressao(compromisso):
    print("------------------------------------")
    print(f"Data do compromisso: {compromisso.data}")
    print(f"Hora do compromisso: {compromisso.hora}")
    print(f"Duração do compromisso (em horas): {compromisso.duracao}")
    print(f"Descrição do compromisso: {compromisso.descricao}")
    print("------------------------------------")

# Filtro que será utilizado posteriormente no código
def filtroPadrao():
    data = input("Digite a data do evento (dd/mm/aaaa): ")
    hora = input("Digite a hora do evento (hh:mm): ")

    for i in range(len(listaDeCompromissos)):
        if listaDeCompromissos[i].data == data and listaDeCompromissos[i].hora == hora:
            return listaDeCompromissos[i]

# Funções da agenda        
def criarCompromisso(vetor):
    # Utiliza estrutura da classe para criar um novo compromisso
    comp = Compromisso()

    comp.data = input("Digite a data do compromisso (dd/mm/aaaa): ")
    comp.hora = input("Digite a hora do compromisso (hh:mm): ")
    comp.duracao = input("Digite a duração em horas do compromisso: ")
    comp.descricao = input("Digite a descrição para seu compromisso: ")

    # Verifica se já existe algum compromisso na mesma data e hora
    for i in range(len(vetor)):
        if vetor[i].data == comp.data and vetor[i].hora == comp.hora:
            print("Já existe um compromisso nesta mesma data e hpra")
            menu()
        
    vetor.append(comp)
    print("Compromisso criado com sucesso!")
    menu()
    return vetor 

def consultarCompromisso():
    print("Opção 1: Consulta com data")
    print("Opção 2: Consulta com data e hora")

    opcao = input("Digite a opção de consulta desejada: ")

    resultadosPesquisa = []

    if opcao == "1":
        data = input("Digite a data do evento (dd/mm/aaaa): ")

        for i in range(len(listaDeCompromissos)):
            if listaDeCompromissos[i].data == data:
                resultadosPesquisa.append(listaDeCompromissos[i])
    elif opcao == "2":
        data = input("Digite a data do evento (dd/mm/aaaa): ")
        hora = input("Digite a hora do evento (hh:mm): ")

        for i in range(len(listaDeCompromissos)):
            if listaDeCompromissos[i].data == data and listaDeCompromissos[i].hora == hora:
                resultadosPesquisa.append(listaDeCompromissos[i])
    else:
        print("Opção inválida!")

    # Verifica se existem itens dentro do vetor de resultados
    if len(resultadosPesquisa) > 0:
        for i in range(len(resultadosPesquisa)):
            templateImpressao(resultadosPesquisa[i])
    else:
        print("Nenhum compromisso correspondente foi encontrado.")

    menu()

def editarCompromisso(vetor):
    compromisso = filtroPadrao()
    
    if compromisso:
        # Salva a data e hora do compromisso a ser editado
        data = compromisso.data
        hora = compromisso.hora

        # Remove compromisso antigo para a adição do editado
        vetor.remove(compromisso)
        compromissoEditado = Compromisso()

        # Insere a data e hora salva previamente
        compromissoEditado.data = data
        compromissoEditado.hora = hora

        # Insere os novos dados
        compromissoEditado.duracao = input("Digite a nova duração (em horas) para seu compromisso: ")
        compromissoEditado.descricao = input("Digite a nova descrição para seu compromisso: ")
        
        # Inclui o compromisso editado ao vetor
        vetor.append(compromissoEditado)
        print("Compromisso editado com sucesso!")
    else:
        print("Nenhum compromisso correspondente foi encontrado.")
    menu()

def excluirCompromisso(vetor):
    compromisso = filtroPadrao()

    if compromisso:
        # Remove o compromisso selecionado pelo usuário
        vetor.remove(compromisso)
        print("Compromisso removido com sucesso!")
    else:
        print("Nenhum compromisso foi encontrado!")
    menu()

def mostrarCompromissos():
    # Percorre o vetor e coloca todos os compromissos em tela
    if listaDeCompromissos:
        for i in range(len(listaDeCompromissos)):
            templateImpressao(listaDeCompromissos[i])
    else:
        print("Não existem compromissos na sua agenda!")
    menu()

# Função que mostra o menu
def menu():
    print("------------------------------------")
    print("Opções da agenda:")
    print("Opção 1: Criar compromisso")
    print("Opção 2: Consultar compromisso")
    print("Opção 3: Alterar compromisso")
    print("Opção 4: Excluir compromisso")
    print("Opção 5: Mostrar todos os seus compromissos")
    print("Opção 6: Sair")
    print("------------------------------------")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        criarCompromisso(listaDeCompromissos)
    elif opcao == "2":
        consultarCompromisso()
    elif opcao == "3":
        editarCompromisso(listaDeCompromissos)
    elif opcao == "4":
        excluirCompromisso(listaDeCompromissos)
    elif opcao == "5":
        mostrarCompromissos()
    elif opcao == "6":
        print("Obrigado por usar a agenda!")
        print("Desenvolvido por Filipe Medeiros de Almeida")
    else:
        print("Opção inválida!")
        menu()

# Primeira chamada do menu
menu()

