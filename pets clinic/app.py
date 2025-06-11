import pymongo
import os

cli = pymongo.MongoClient("mongodb://localhost:27017/")
db = cli["clinic_db"]
pets = db["pets"]

def show_pets():
    clear_console()
    print('-' * 30)
    print('Lista de Pets'.center(30))
    print('-' * 30)
    resultados = pets.find({}, {"_id": 0, "name": 1})
    if resultados:
        for x in resultados:
            print(f"Nome: {x['name']}")
    else: 
        print('Nenhum animal encontrado')
    input()

def search_pet():
    clear_console()
    print('-' * 30)
    print('Pesquisar Pet'.center(30))
    print('-' * 30)
    name = input('Nome: ')
    resultados = list(pets.find({"name": name}, {"_id": 0, "name": 1, "email": 1}))
    if resultados:
        for x in resultados:
            print(x)
    else:
        print('Nenhum usuário encontrado')
    input()

def insert_pet():
    clear_console()
    print('-' * 30)
    print('Inserir novo Pet'.center(30))
    print('-' * 30)
    name = input('Nome:')
    email = input('E-mail:')
    pets.insert_one({"name": name, "email": email})
    print('Usuário inserido com sucesso')
    input()

def update_pet():
    clear_console()
    print('-' * 30)
    print('Alterar Pet'.center(30))
    print('-' * 30)
    name = input('Digite o nome: ')
    user = pets.find_one({"name": name}, {"_id": 0, "name": 1})
    if user is None:
        print('Nenhum pet encontrado')
        input()
        return
    
    while True:
        clear_console()
        print("-" * 30)
        print(f"O que deseja alterar no pet {name}?")
        print("-" * 30)
        print("[1] Nome")
        print("[2] E-mail")
        print("[3] Voltar")
        opt = input('Sua opção:')
        if opt == "1":
            newName = input("Novo nome:")
            pets.update_one({"name":name}, {"$set": {"name": newName}})
            print("Nome alterado com sucesso")
            input()
            return
        elif opt == "3":
            break
        else: 
            clear_console()
            print('\033[031mOpção Inválida\033[m')
            input()
    
def delete_pet():
    clear_console()
    print('-' * 30)
    print('Apagar usuário'.center(30))
    print('-' * 30)
    name = input('Digite o nome: ')
    user = pets.find_one({"name": name}, {"_id": 0, "name": 1, "email": 1})
    if user is None:
        print('Nenhum usuário encontrado')
        input()
        return
    
    clear_console()
    confirm = input(f'Tem certeza de que deseja apagar {name}? (S/n)')
    if confirm == 'S' or confirm == '':
        pets.delete_one({"name": name})

    print("Usuário removido com sucesso")
    input()

def clear_console():
    os.system('clz' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console()
        print('-' * 30)
        print('Cadastro de usuários'.center(30))
        print('-' * 30)
        print('[1] listar Pets')
        print('[2] Pesquisar Pet')
        print('[3] Cadastrar Pet')
        print('[4] Alterar Pet')
        print('[5] Apagar Pet')
        print('[6] Sair')

        opt = input('Sua opção:')
        if opt == '1':
            show_pets()
        elif opt == '2':
            search_pet()
        elif opt == '3':
            insert_pet()
        elif opt == '4':
            update_pet()
        elif opt == '5':
            delete_pet()
        elif opt == '6':
            break
        else:
            clear_console()
            print(opt)
            print('\033[031mOpção Inválida\033[m')
            input()

main()