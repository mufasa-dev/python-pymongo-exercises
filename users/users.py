import os

def show_users():
    print('Lista de usuários')
    input()

def search_user():
    name = input('Nome: ')
    print('Usuário')
    input()

def insert_user():
    name = input('Nome:')
    email = input('E-mail:')

def clear_console():
    os.system('clz' if os.name == 'nt' else 'clear')

def main() :
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