from models.pet import pets
from utils import interface

def show_pets():
    interface.clear_console()
    print('-' * 50)
    print('Lista de Pets'.center(50))
    print('-' * 50)
    resultados = pets.find({}, {"_id": 0, "name": 1})
    found = False
    for x in resultados:
        print(f"Nome: {x['name']}")
        found = True
    if not found:
        print(f'{interface.text_red('Nenhum animal encontrado')}')
    input()

def search_pet():
    interface.clear_console()
    print('-' * 50)
    print('Pesquisar Pet'.center(50))
    print('-' * 50)
    name = input('Nome: ')
    resultados = list(pets.find({"name": name}, {"_id": 0, "name": 1, "email": 1}))
    if resultados:
        for x in resultados:
            print(x)
    else:
        print(f'{interface.text_red('Nenhum animal encontrado')}')
    input()

def insert_pet():
    interface.clear_console()
    print('-' * 50)
    print('Inserir novo Pet'.center(50))
    print('-' * 50)
    name = input('Nome:')
    email = input('E-mail:')
    pets.insert_one({"name": name, "email": email})
    print('Pet inserido com sucesso')
    input()

def update_pet():
    interface.clear_console()
    print('-' * 50)
    print('Alterar Pet'.center(50))
    print('-' * 50)
    name = input('Digite o nome: ')
    user = pets.find_one({"name": name}, {"_id": 0, "name": 1})
    if user is None:
        print(f'{interface.text_red('Nenhum animal encontrado')}')
        input()
        return

    while True:
        interface.clear_console()
        print("-" * 50)
        print(f"O que deseja alterar no pet {name}?")
        print("-" * 50)
        print("[1] Nome")
        print("[2] E-mail")
        print("[3] Voltar")
        opt = input('Sua opção:')
        if opt == "1":
            newName = input("Novo nome:")
            pets.update_one({"name": name}, {"$set": {"name": newName}})
            print("Nome alterado com sucesso")
            input()
            return
        elif opt == "2":
            newEmail = input("Novo e-mail:")
            pets.update_one({"name": name}, {"$set": {"email": newEmail}})
            print("E-mail alterado com sucesso")
            input()
            return
        elif opt == "3":
            break
        else:
            interface.clear_console()
            print(f'{interface.text_red("Opção Inválida")}')
            input()

def delete_pet():
    interface.clear_console()
    print('-' * 50)
    print('Apagar usuário'.center(50))
    print('-' * 50)
    name = input('Digite o nome: ')
    user = pets.find_one({"name": name}, {"_id": 0, "name": 1, "email": 1})
    if user is None:
        print(f'{interface.text_red('Nenhum animal encontrado')}')
        input()
        return

    interface.clear_console()
    confirm = input(f'Tem certeza de que deseja apagar {name}? (S/n)')
    if confirm == 'S' or confirm == '':
        pets.delete_one({"name": name})
        print("Pet removido com sucesso")
    else:
        print(f'{interface.text_red('Ação cancelada')}')
    input()

def menu():
    while True:
        interface.clear_console()
        print('-' * 50)
        print('Cadastro de pets'.center(50))
        print('-' * 50)
        print('[1] Listar Pets')
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
            interface.clear_console()
            print(opt)
            print(f'{interface.text_red("Opção Inválida")}')
            input()