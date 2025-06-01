import os
from pymongo import MongoClient

# Operação Create (Criar: Inserir um documento na coleção)
def criar_documento(dados):
 resultado = colecao.insert_one(dados)
 print(f'Restaurante inserido com id: {resultado.inserted_id}')

# Operação Read (Ler documentos da coleção)
def ler_documentos():
 clear_console()
 documentos = colecao.find()
 for doc in documentos:
     print(f"Restaurante: {doc["nome"]}")
 input()

# Operação Update (Atualizar um documento existente)
def atualizar_documento(filtro, novos_dados):
 resultado = colecao.update_one(filtro, {'$set': novos_dados})
 print(f'Documentos atualizados: {resultado.modified_count}')

# Operação Delete (Excluir um documento)
def excluir_documento(nome):
 print('-' * 40)
 print('Apagar restaurante'.center(40))
 print('-' * 40)
 print()
 nome = input("Nome no restaurante que deseja excluir: ")
 restaurante = colecao.find_one({"nome": nome})
 if restaurante is None:
    print('Nenhum restaurante encontrado com esse nome')
    input()
    return

 while True:
    clear_console()
    confirm = input(f'Tem certeza de que deseja apagar {nome}? (S/n)')
    if confirm == 'S' or confirm == '':
        break
    if confirm.upper() == "N":
        return
    else:
        print('\033[031mOpção Inválida\033[m')
 resultado = colecao.delete_one({"nome": nome})
 print(f'Restaurante excluído: {resultado.deleted_count}')

# Método para receber a nota de avaliação
def receber_nota():
    while True:
        entrada = input("Digite uma nota (0 a 5): ")
        try:
            nota = float(entrada)
            if nota <= 0 or nota > 5:
                print("A nota deve estar entre 0 e 5")
            else:
                return nota
        except:
            print("Nota inválida")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Interface de Linha de Comando
def menu():
 while True:
    clear_console()
    print("-" * 40)
    print("Escolha uma operação:".center(40))
    print("-" * 40)
    print("1. Inserir novo restaurante")
    print("2. Consultar todos os restaurantes")
    print("3. Atualizar um restaurante")
    print("4. Excluir restaurante")
    print("5. Avaliar restaurante")
    print("6. Mostrar avaliações de um restaurante")
    print("7. Alterar uma avaliação")
    print("8. Excluir uma avaliação")
    print("9. Mostrar média de avaliações")
    print("10.Sair")
    print()
    escolha = input("Digite o número da operação: ")
    if escolha == '1':
        clear_console()
        print("-" * 40)
        print("Inserir novo restaurante:".center(40))
        print("-" * 40)
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        categoria = input("Categoria: ")
        criar_documento({"nome":nome, "endereco":endereco, "categoria": categoria, "avaliacoes": []})
        input()
    elif escolha == '2':
        clear_console()
        print("-" * 40)
        print("Consultar todos os restaurantes:".center(40))
        print("-" * 40)
        ler_documentos()
    elif escolha == '3':
        clear_console()
        print("-" * 40)
        print("Atualizar um restaurante:".center(40))
        print("-" * 40)
        nome = input('Digite o nome do restaurante que deseja alterar: ')
        restaurante = colecao.find_one({"nome": nome})
        if restaurante is None:
            print('Nenhum restaurante encontrado com esse nome')
            input()
            return
        
        while True:
            clear_console()
            print("-" * 40)
            print(f"O que deseja alterar no restaurante {nome}?")
            print("-" * 40)
            print("[1] Nome")
            print("[2] Endereço")
            print("[3] Categoria")
            print("[4] Voltar")
            opt = input('Sua opção:')
            if opt == "1":
                novoNome = input("Novo nome:")
                colecao.update_one({"nome":name}, {"$set": {"nome": colecao}})
                print("Nome alterado com sucesso")
                input()
                return
            elif opt == "2":
                novoEndereco = input("Novo endereço:")
                colecao.update_one({"nome":nome}, {"$set": {"endereco": novoEndereco}})
                print("Endereço alterado com sucesso")
                input()
                return
            elif opt == "3":
                novaCategoria = input("Nova categoria:")
                colecao.update_one({"nome":nome}, {"$set": {"categoria": novaCategoria}})
                print("Categoria alterada com sucesso")
                input()
                return
            elif opt == "4":
                break
            else: 
                clear_console()
                print('\033[031mOpção Inválida\033[m')
                input()
    elif escolha == '4':
        excluir_documento(nome)
    elif escolha == '5':
        clear_console()
        nome = input("Nome no restaurante que deseja avaliar: ")
        restaurante = colecao.find_one({"nome": nome})
        if restaurante is None:
            print('Nenhum restaurante encontrado com esse nome')
            input()
            return
        nome_cliente = input("Nome do cliente:")
        nota = receber_nota()
        comentario = input("Comentário: ")
        colecao.update_one({"nome": nome}, {"$push": {"avaliacoes" : {"cliente": nome_cliente, "nota": nota, "comentario": comentario}}})
        input("Avaliação incluida com sucesso!")
    elif escolha == '6':
        clear_console()
        nome = input("Nome no restaurante que deseja consultar avaliações: ")
        restaurante = colecao.find_one({"nome": nome})
        if restaurante is None:
            print('Nenhum restaurante encontrado com esse nome')
            input()
            return   
        avaliacoes = restaurante["avaliacoes"]
        for a in avaliacoes:
            print(f"Cliente:{a["cliente"]} Nota: {a["nota"]} Comentário: {a["comentario"]}")
        input()
    elif escolha == '7':
        clear_console()
        nome = input("Nome no restaurante que deseja alterar a avaliação: ")
        restaurante = colecao.find_one({"nome": nome})
        if restaurante is None:
            print('Nenhum restaurante encontrado com esse nome')
            input()
            return   
        print("-" * 40)
        print(nome.center(40))
        print("-" * 40)
        avaliacoes = restaurante["avaliacoes"]
        index = 0
        for a in list(avaliacoes):
            index = index + 1
            print(f" [{index}] Cliente:{a["cliente"]} Nota: {a["nota"]} Comentário: {a["comentario"]}")
        print()
        avIndex = int(input("Selecione uma avaliação: "))
        avaliacao = avaliacoes[avIndex - 1]
        clear_console()

        while True:
            clear_console()
            print("-" * 40)
            print(f"O que deseja alterar na avaliação de {avaliacao["cliente"]}?")
            print("-" * 40)
            print("[1] Nome do cliente")
            print("[2] Nota")
            print("[3] Comentário")
            print("[4] Voltar")
            opt = input('Sua opção: ')
            if opt == "1":
                novoCliente = input("Novo nome: ")
                colecao.update_one({"nome":nome}, {"$set": {f"avaliacoes.{avIndex - 1}.cliente": novoCliente}})
                print("Nome do cliente alterado com sucesso")
                input()
                break
            elif opt == "2":
                novaNota = receber_nota()
                colecao.update_one({"nome":nome}, {"$set": {f"avaliacoes.{avIndex - 1}.cliente": novaNota}})
                print("Nota alterada com sucesso")
                input()
                break
            elif opt == "3":
                novoComentario = input("Novo comentário: ")
                colecao.update_one({"nome":nome}, {"$set": {f"avaliacoes.{avIndex - 1}.comentario": novoComentario}})
                print("Comentário alterado com sucesso")
                input()
                break
            elif opt == "4":
                break
            else: 
                clear_console()
                print('\033[031mOpção Inválida\033[m')
                input()
    elif escolha == '8':
        clear_console()
        nome = input("Nome do restaurante que deseja excluir uma avaliação: ")
        restaurante = colecao.find_one({"nome": nome})
        if restaurante is None:
            print('Nenhum restaurante encontrado com esse nome')
            input()
            return   
        print("-" * 40)
        print(nome.center(40))
        print("-" * 40)
        avaliacoes = restaurante["avaliacoes"]
        index = 0
        for a in list(avaliacoes):
            index = index + 1
            print(f" [{index}] Cliente:{a["cliente"]} Nota: {a["nota"]} Comentário: {a["comentario"]}")
        print()
        avIndex = int(input("Selecione uma avaliação: "))
        avaliacao = avaliacoes[avIndex - 1]
        clear_console()
        print(avaliacao)
        colecao.update_one({"nome":nome}, {"$pull": {"avaliacoes":{"nome": avaliacao["nome"]}}})  
        print("avaliação excluída com sucesso")
        input()  
    elif escolha == '10':
        clear_console()
        break
    else:
        print("Escolha inválida. Tente novamente.")
        input()


# Corpo da aplicação
# Comandos para conectar com o servidor local, banco de dados meu_banco_de_dados,
# coleção minha_colecao
cliente = MongoClient('localhost', 27017)
bd = cliente['restaurate_db']
colecao = bd['restaurantes']
menu()