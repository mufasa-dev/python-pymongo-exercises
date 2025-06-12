from models.pet import pets
from utils.interface import clear_console

def show_pets():
    clear_console()
    print('-' * 50)
    print('Lista de Pets'.center(50))
    print('-' * 50)
    resultados = pets.find({}, {"_id": 0, "name": 1})
    found = False
    for x in resultados:
        print(f"Nome: {x['name']}")
        found = True
    if not found:
        print('Nenhum animal encontrado')
    input()

def search_pet():
    clear_console()
    print('-' * 50)
    print('Pesquisar Pet'.center(50))
    print('-' * 50)
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
    print('-' * 50)
    print('Inserir novo Pet'.center(50))
    print('-' * 50)
    name = input('Nome:')
    email = input('E-mail:')
    pets.insert_one({"name": name, "email": email})
    print('Usuário inserido com sucesso')
    input()

def update_pet():
    clear_console()
    print('-' * 50)
    print('Alterar Pet'.center(50))
    print('-' * 50)
    name = input('Digite o nome: ')
    user = pets.find_one({"name": name}, {"_id": 0, "name": 1})
    if user is None:
        print('Nenhum pet encontrado')
        input()
        return

    while True:
        clear_console()
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
            clear_console()
            print('\033[031mOpção Inválida\033[m')
            input()

def delete_pet():
    clear_console()
    print('-' * 50)
    print('Apagar usuário'.center(50))
    print('-' * 50)
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
    else:
        print("Ação cancelada")
    input()