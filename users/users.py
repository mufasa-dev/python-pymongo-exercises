import pymongo
import os

cli = pymongo.MongoClient("mongodb://localhost:27017/")
db = cli["users_db"]
users = db["users"]

def show_users():
    clear_console()
    print('-' * 30)
    print('Lista de usuários'.center(30))
    print('-' * 30)
    resultados = users.find({}, {"_id": 0, "name": 1, "email": 1})
    if resultados:
        for x in resultados:
            print(f"Nome: {x['name']} E-mail: {x['email']}")
    else: 
        print('Nenhum usuário encontrado')
    input()

def search_user():
    clear_console()
    print('-' * 30)
    print('Pesquisar usuário'.center(30))
    print('-' * 30)
    name = input('Nome: ')
    resultados = list(users.find({"name": name}, {"_id": 0, "name": 1, "email": 1}))
    if resultados:
        for x in resultados:
            print(x)
    else:
        print('Nenhum usuário encontrado')
    input()

def insert_user():
    clear_console()
    print('-' * 30)
    print('Inserir novo usuário'.center(30))
    print('-' * 30)
    name = input('Nome:')
    email = input('E-mail:')
    users.insert_one({"name": name, "email": email})
    print('Usuário inserido com sucesso')
    input()

def update_user():
    clear_console()
    print('-' * 30)
    print('Alterar usuário'.center(30))
    print('-' * 30)
    name = input('Digite o nome: ')
    user = users.find_one({"name": name}, {"_id": 0, "name": 1, "email": 1})
    if user is None:
        print('Nenhum usuário encontrado')
        input()
        return
    
    while True:
        clear_console()
        print("-" * 30)
        print(f"O que deseja alterar do usuário {name}?")
        print("-" * 30)
        print("[1] Nome")
        print("[2] E-mail")
        print("[3] Voltar")
        opt = input('Sua opção:')
        if opt == "1":
            newName = input("Novo nome:")
            users.update_one({"name":name}, {"$set": {"name": newName}})
            print("Nome alterado com sucesso")
            input()
            return
        elif opt == "2":
            newEmail = input("Novo e-mail:")
            users.update_one({"name":name}, {"$set": {"email": newEmail}})
            print("E-mail alterado com sucesso")
            input()
            return
        elif opt == "3":
            break
        else: 
            clear_console()
            print('\033[031mOpção Inválida\033[m')
            input()
    
def delete_user():
    clear_console()
    print('-' * 30)
    print('Apagar usuário'.center(30))
    print('-' * 30)
    name = input('Digite o nome: ')
    user = users.find_one({"name": name}, {"_id": 0, "name": 1, "email": 1})
    if user is None:
        print('Nenhum usuário encontrado')
        input()
        return
    
    clear_console()
    confirm = input(f'Tem certeza de que deseja apagar {name}? (S/n)')
    if confirm == 'S' or confirm == '':
        users.delete_one({"name": name})

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
        print('[1] listar usuários')
        print('[2] Pesquisar usuário')
        print('[3] Cadastrar usuário')
        print('[4] Alterar usuário')
        print('[5] Apagar Usuário')
        print('[6] Sair')

        opt = input('Sua opção:')
        if opt == '1':
            show_users()
        elif opt == '2':
            search_user()
        elif opt == '3':
            insert_user()
        elif opt == '4':
            update_user()
        elif opt == '5':
            delete_user()
        elif opt == '6':
            break
        else:
            clear_console()
            print(opt)
            print('\033[031mOpção Inválida\033[m')
            input()

main()