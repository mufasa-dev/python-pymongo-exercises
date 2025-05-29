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
            print(x)
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
    name = input('Nome:')
    email = input('E-mail:')
    users.insert_one({"name": name, "email": email})
    print('Usuário inserido com sucesso')
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

        resp = input('Sua opção:')
        if resp == '1':
            show_users()
        elif resp == '2':
            search_user()
        elif resp == '3':
            insert_user()
        elif resp == '6':
            break
        else:
            clear_console()
            print(resp)
            print('\033[031mOpção Inválida\033[m')
            input()

main()