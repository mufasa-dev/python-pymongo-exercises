# Bruno Ribeiro Antunes    11251405538
# Brenno de Sousa Lemos    11222100597
# João Victor Tigges Godoy 11231400100

import os
from pymongo import MongoClient

# Operação Create (Criar: Inserir um documento na coleção)
def criar_documento():
 clear_console()
 print("-" * 50)
 print("Inserir novo restaurante".center(50))
 print("-" * 50)
 
 nome = input(text_yellow("Nome: "))
 if len(nome) <= 3:
    print()
    print(text_red("Nome muito curto"))
    input()
    criar_documento()
    return
 
 restaurante = colecao.find_one({"nome": nome})
 if restaurante is not None:
    print('Já existe um restaurante cadastrado com esse nome')
    input()
    criar_documento()
    return
 
 while True:
    endereco = input(text_yellow("Endereço: "))
    if len(endereco) >= 3:
        break
    else:
        print()
        print(text_red("Endereço muito curto"))
        input()

 while True:
    categoria = input(text_yellow("Categoria: "))
    if len(categoria) > 0:
        break
    else:
        print()
        print(text_red("Categoria inválida"))
        input()
 resultado = colecao.insert_one({"nome":nome, "endereco":endereco, "categoria": categoria, "avaliacoes": []})
 print()
 print(f'{text_green("Restaurante inserido com id:")} {resultado.inserted_id}')
 input()

# Operação Read (Ler documentos da coleção)
def ler_documentos():
 clear_console()
 print("-" * 50)
 print("Consultar todos os restaurantes".center(50))
 print("-" * 50)
 documentos = colecao.find()
 for doc in documentos:
     print(f"{text_blue("Restaurante:")} {doc["nome"]}")
     print(f"{text_blue("Categoria:")} {doc["categoria"]}")
     print(f"{text_blue("Endereço:")} {doc["endereco"]}")
     print()
 input()

# Operação Update (Atualizar um documento existente)
def atualizar_documento():
 clear_console()
 print("-" * 50)
 print("Atualizar um restaurante:".center(50))
 print("-" * 50)
 print(text_yellow('Digite o nome do restaurante que deseja alterar '))
 nome = input()
 restaurante = colecao.find_one({"nome": nome})
 if restaurante is None:
    print('Nenhum restaurante encontrado com esse nome')
    input()
    return

 while True:
    clear_console()
    print("-" * 50)
    print(f"O que deseja alterar no restaurante {nome}?")
    print("-" * 50)
    print(f"{text_yellow("[1]")} {text_blue("Nome")} {nome}")
    print(f"{text_yellow("[2]")} {text_blue("Endereço")} {restaurante["endereco"]}")
    print(f"{text_yellow("[3]")} {text_blue("Categoria")} {restaurante["categoria"]}")
    print(f"{text_yellow("[4]")} {text_blue("Voltar")}")
    print("-" * 50)
    opt = input(text_yellow('Sua opção: '))
    print()
    if opt == "1":
        novoNome = input(text_yellow("Novo nome: "))
        colecao.update_one({"nome":nome}, {"$set": {"nome": novoNome}})
        print()
        print(text_green("Nome alterado com sucesso"))
        input()
        return
    elif opt == "2":
        novoEndereco = input(text_yellow("Novo endereço: "))
        colecao.update_one({"nome":nome}, {"$set": {"endereco": novoEndereco}})
        print()
        print(text_green("Endereço alterado com sucesso"))
        input()
        return
    elif opt == "3":
        novaCategoria = input(text_yellow("Nova categoria: "))
        colecao.update_one({"nome":nome}, {"$set": {"categoria": novaCategoria}})
        print()
        print(text_green("Categoria alterada com sucesso"))
        input()
        return
    elif opt == "4":
        break
    else: 
        clear_console()
        print(text_red("Opção Inválida"))
        input()

# Operação Delete (Excluir um documento)
def excluir_documento():
 clear_console()
 print('-' * 50)
 print('Apagar restaurante'.center(50))
 print('-' * 50)
 print()
 nome = input(text_yellow("Nome no restaurante que deseja excluir: "))
 restaurante = colecao.find_one({"nome": nome})
 if restaurante is None:
    print()
    print(text_red('Nenhum restaurante encontrado com esse nome'))
    input()
    return

 while True:
    print()
    confirm = input(f'{text_yellow(f"Tem certeza de que deseja apagar {nome}? (S/n) ")}')
    if confirm == 'S' or confirm == '':
        break
    if confirm.upper() == "N":
        return
    else:
        print(text_red("Opção Inválida"))
 resultado = colecao.delete_one({"nome": nome})
 print(f'{text_blue("Restaurantes excluídos:")} {resultado.deleted_count}')
 input()

# Método para avaliar restaurantes
def avaliar():
    clear_console()
    print('-' * 50)
    print('Avaliar restaurante'.center(50))
    print('-' * 50)
    print()
    nome = input(text_yellow("Nome no restaurante: "))
    restaurante = colecao.find_one({"nome": nome})
    if restaurante is None:
        print(text_red('Nenhum restaurante encontrado com esse nome'))
        input()
        avaliar()
        return
    nome_cliente = input(text_yellow("Nome do cliente: "))
    nota = receber_nota()
    comentario = input(text_yellow("Comentário: "))
    colecao.update_one({"nome": nome}, {"$push": {"avaliacoes" : {"cliente": nome_cliente, "nota": nota, "comentario": comentario}}})
    print()
    input(text_green("Avaliação incluida com sucesso!"))

# Método para consultar avaliações de um restaurante
def consultar_avaliacoes():
    clear_console()
    print('-' * 50)
    print('Mostrar avaliações'.center(50))
    print('-' * 50)
    print()
    nome = input(text_yellow("Nome no restaurante que deseja consultar: "))
    restaurante = colecao.find_one({"nome": nome})
    if restaurante is None:
        print()
        print(text_red('Nenhum restaurante encontrado com esse nome'))
        input()
        return  

    clear_console()
    print("-" * 50)
    print(nome.center(50))
    print("-" * 50) 
    
    avaliacoes = restaurante["avaliacoes"]

    if len(avaliacoes) == 0:
        print(text_red("O restaurante ainda não possuí avaliações".center(50)))
        input()
        return
    
    for a in avaliacoes:
        print(f"{text_blue("Cliente:")} {a["cliente"]}")
        print(f"{text_blue("Nota:")} {a["nota"]}")
        print(f"{text_blue("Comentário:")} {a["comentario"]}")
        print()
    input()

# Método para alterar uma avaliação de um restaurante
def alterar_avaliacao():
    clear_console()
    print('-' * 50)
    print('Alterar uma avaliação'.center(50))
    print('-' * 50)
    print()
    print("Nome no restaurante que deseja alterar a avaliação: ")
    nome = input()
    restaurante = colecao.find_one({"nome": nome})
    if restaurante is None:
        print()
        print(text_red('Nenhum restaurante encontrado com esse nome'))
        input()
        return   
    clear_console()
    print("-" * 50)
    print(nome.center(50))
    print("-" * 50)
    avaliacoes = restaurante["avaliacoes"]

    if len(avaliacoes) == 0:
        print(text_red("O restaurante ainda não possuí avaliações".center(50)))
        input()
        return
    
    index = 0
    for a in list(avaliacoes):
        index = index + 1
        print(f"{text_yellow(f"[{index}]")} {text_blue("Cliente:")} {a["cliente"]:27} {text_blue("Nota:")} {a["nota"]}")
    print(f"{text_yellow(f"[{index + 1}]")} {text_blue("Voltar")}")
    print("-" * 50)
    while True:
        try:
            avIndex = int(input("Selecione uma avaliação: "))
            if avIndex == index + 1:
                return
            elif avIndex > (index + 1):
                print(text_red("Opção inválida"))
            else:
                break
        except:
            print(text_red("Opção inválida"))
            print()
    
    avaliacao = avaliacoes[avIndex - 1]
    clear_console()

    while True:
        clear_console()
        print("-" * 50)
        print(f"O que deseja alterar na avaliação de {avaliacao["cliente"]}?".center(50))
        print("-" * 50)
        print(f"{text_yellow("[1]")} {text_blue("Nome do cliente")} {avaliacao["cliente"]}")
        print(f"{text_yellow("[2]")} {text_blue("Nota")} {avaliacao["nota"]}")
        print(f"{text_yellow("[3]")} {text_blue("Comentário")} {avaliacao["comentario"]}")
        print(f"{text_yellow("[4]")} {text_blue("Voltar")}")
        print("-" * 50)
        opt = input('Sua opção: ')
        if opt == "1":
            novoCliente = input("Novo nome: ")
            colecao.update_one({"nome":nome}, {"$set": {f"avaliacoes.{avIndex - 1}.cliente": novoCliente}})
            print()
            print(text_green("Nome do cliente alterado com sucesso"))
            input()
            break
        elif opt == "2":
            novaNota = receber_nota()
            colecao.update_one({"nome":nome}, {"$set": {f"avaliacoes.{avIndex - 1}.cliente": novaNota}})
            print()
            print(text_green("Nota alterada com sucesso"))
            input()
            break
        elif opt == "3":
            novoComentario = input("Novo comentário: ")
            colecao.update_one({"nome":nome}, {"$set": {f"avaliacoes.{avIndex - 1}.comentario": novoComentario}})
            print()
            print(text_green("Comentário alterado com sucesso"))
            input()
            break
        elif opt == "4":
            break
        else: 
            print()
            print(text_red("Escolha inválida. Tente novamente."))
            input()

# Método para apagar uma avaliação
def apagar_avaliacao():
    clear_console()
    print('-' * 50)
    print('Excluir uma avaliação'.center(50))
    print('-' * 50)
    print()
    print(text_yellow("Nome do restaurante que deseja excluir uma avaliação: "))
    nome = input()
    restaurante = colecao.find_one({"nome": nome})
    if restaurante is None:
        print(text_red('Nenhum restaurante encontrado com esse nome'))
        input()
        return   
    clear_console()
    print("-" * 50)
    print(nome.center(50))
    print("-" * 50)
    avaliacoes = restaurante["avaliacoes"]

    if len(avaliacoes) == 0:
        print(text_red("O restaurante ainda não possuí avaliações".center(50)))
        input()
        return
    
    index = 0
    for a in list(avaliacoes):
        index = index + 1
        print(f"{text_yellow(f"[{index}]")} {text_blue("Cliente:")} {a["cliente"]:27} {text_blue("Nota:")} {a["nota"]}")
    print(f"{text_yellow(f"[{index + 1}]")} {text_blue("Voltar")}")
    print("-" * 50)
    while True:
        try:
            avIndex = int(input(text_yellow("Selecione uma avaliação: ")))
            if avIndex == index + 1:
                return
            elif avIndex > (index + 1):
                print(text_red("Opção inválida"))
            else:
                break
        except:
            print(text_red("Opção inválida"))
            print()
    avaliacao = avaliacoes[avIndex - 1]
    clear_console()
    print(avaliacao)
    colecao.update_one({"nome":nome}, {"$pull": {"avaliacoes":{"nome": avaliacao["nome"]}}})  
    print()
    print(text_green("avaliação excluída com sucesso"))
    input() 

# Operação para trazer a média das avaliações dos restaurantes
def consultar_media():
 clear_console()
 print("-" * 50)
 print("Consultar todos os restaurantes".center(50))
 print("-" * 50)
 documentos = colecao.aggregate([
     {
         "$project": {
             "nome": 1,
             "media": {"$avg": "$avaliacoes.nota"}
         }
     },
     {
        "$sort" : { "nome": 1 }   
     }
 ])
 for doc in documentos:
     print(f"{text_blue("Restaurante:")} {doc["nome"]}")
     if (doc["media"] is not None): 
         print(f"{text_blue("Média:")} {doc["media"]:.2f}")
     else: 
        print("Nenhuma avaliação")
     print()
 input()

# Método para receber a nota de avaliação
def receber_nota():
    while True:
        entrada = input(text_yellow("Digite uma nota (0 a 5): "))
        try:
            nota = float(entrada)
            if nota < 0 or nota > 5:
                print(text_red("A nota deve estar entre 0 e 5"))
                print()
            else:
                return nota
        except:
            print(text_red("Nota inválida"))
            print()

def text_yellow(text):
    return f"\033[93m{text}\033[m"

def text_blue(text):
    return f"\033[94m{text}\033[m"

def text_red(text):
    return f"\033[91m{text}\033[m"

def text_green(text):
    return f"\033[92m{text}\033[m"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Interface de Linha de Comando
def menu():
 while True:
    clear_console()
    print("-" * 50)
    print("Escolha uma operação".center(50))
    print("-" * 50)
    print(f"{text_yellow("[1]")}  {text_blue("Inserir novo restaurante")}")
    print(f"{text_yellow("[2]")}  {text_blue("Consultar todos os restaurantes")}")
    print(f"{text_yellow("[3]")}  {text_blue("Atualizar um restaurante")}")
    print(f"{text_yellow("[4]")}  {text_blue("Excluir restaurante")}")
    print(f"{text_yellow("[5]")}  {text_blue("Avaliar restaurante")}")
    print(f"{text_yellow("[6]")}  {text_blue("Mostrar avaliações de um restaurante")}")
    print(f"{text_yellow("[7]")}  {text_blue("Alterar uma avaliação")}")
    print(f"{text_yellow("[8]")}  {text_blue("Excluir uma avaliação")}")
    print(f"{text_yellow("[9]")}  {text_blue("Mostrar média de avaliações")}")
    print(f"{text_yellow("[10]")} {text_blue("Sair")}")
    print("-" * 50)
    escolha = input(text_yellow("Digite o número da operação: "))
    if escolha == '1':
        criar_documento()
    elif escolha == '2':
        ler_documentos()
    elif escolha == '3':
        atualizar_documento()
    elif escolha == '4':
        excluir_documento()
    elif escolha == '5':
        avaliar()
    elif escolha == '6':
        consultar_avaliacoes()
    elif escolha == '7':
        alterar_avaliacao()
    elif escolha == '8':
         apagar_avaliacao()
    elif escolha == '9':
        consultar_media()
    elif escolha == '10':
        clear_console()
        break
    else:
        print()
        print(text_red("Escolha inválida. Tente novamente."))
        input()


# Corpo da aplicação
# Comandos para conectar com o servidor local, banco de dados meu_banco_de_dados,
# coleção minha_colecao
cliente = MongoClient('localhost', 27017)
bd = cliente['restaurate_db']
colecao = bd['restaurantes']
menu()
