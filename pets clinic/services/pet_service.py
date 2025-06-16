from models.pet import pets
from utils import interface

def show_pets():
    interface.clear_console()
    print('-' * 50)
    print('Lista de Pets'.center(50))
    print('-' * 50)
    resultados = pets.find({})
    found = False
    for x in resultados:
        print(f"{interface.text_blue("Nome: ")} {x["name"]}")
        print(f"{interface.text_blue("Espécie: ")} {x["species"]}")
        print(f"{interface.text_blue("Raça: ")} {x["breed"]}")
        print(f"{interface.text_blue("Idade: ")} {x["age"]} ano(s)")
        print()
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
    print()
    resultados = list(pets.find({"name": name}))
    if resultados:
        for x in resultados:
            print(f"{interface.text_blue("Nome: ")} {x["name"]}")
            print(f"{interface.text_blue("Espécie: ")} {x["species"]}")
            print(f"{interface.text_blue("Raça: ")} {x["breed"]}")
            print(f"{interface.text_blue("Idade: ")} {x["age"]} ano(s)")
            print()
    else:
        print(f'{interface.text_red('Nenhum animal encontrado')}')
    input()

def insert_pet():
    interface.clear_console()
    print('-' * 50)
    print('Inserir novo Pet'.center(50))
    print('-' * 50)
    name = input(interface.text_blue('Nome: '))
    species = input(interface.text_blue("Espécie: "))
    breed = input(interface.text_blue('Raça: '))
    age = input(interface.text_blue('Idade: '))
    pets.insert_one({"name": name, "species": species, "breed": breed, "age": age})
    print('Pet inserido com sucesso')
    input()

def update_pet():
    interface.clear_console()
    print('-' * 50)
    print('Alterar Pet'.center(50))
    print('-' * 50)
    name = input('Digite o nome: ')
    pet = pets.find_one({"name": name}, {"_id": 0, "name": 1})
    if pet is None:
        print(f'{interface.text_red('Nenhum animal encontrado')}')
        input()
        return

    while True:
        interface.clear_console()
        print("-" * 50)
        print(f"O que deseja alterar no pet {name}?")
        print("-" * 50)
        print(f"{interface.text_yellow("[1]")} {interface.text_blue("Nome")}: {pet["name"]}")
        print(f"{interface.text_yellow("[2]")} {interface.text_blue("Espécie")}: {pet["species"]}")
        print(f"{interface.text_yellow("[3]")} {interface.text_blue("Raça")}: {pet["breed"]}")
        print(f"{interface.text_yellow("[4]")} {interface.text_blue("Idade")}: {pet["age"]}")
        print(f"{interface.text_yellow("[5]")} {interface.text_blue("Voltar")}")
        opt = input('Sua opção:')
        if opt == "1":
            newName = input("Novo nome:")
            pets.update_one({"name": name}, {"$set": {"name": newName}})
            print()
            print(interface.text_green("Nome alterado com sucesso"))
            input()
            return
        elif opt == "2":
            newSpecie = input(interface.text_blue("Nova espécie: "))
            pets.update_one({"name": name}, {"$set": {"species": newSpecie}})
            print()
            print(interface.text_green("Espécie alterada com sucesso"))
            input()
            return
        elif opt == "3":
            newBreed = input(interface.text_blue("Nova raça: "))
            pets.update_one({"name": name}, {"$set": {"breed": newBreed}})
            print()
            print(interface.text_green("Raça alterada com sucesso"))
            input()
            return
        elif opt == "4":
            newAge = input(interface.text_blue("Nova idade: "))
            pets.update_one({"name": name}, {"$set": {"age": newAge}})
            print()
            print(interface.text_green("Idade alterada com sucesso"))
            input()
            return
        elif opt == "5":
            break
        else:
            interface.clear_console()
            print(f'{interface.text_red("Opção Inválida")}')
            input()

def delete_pet():
    interface.clear_console()
    print('-' * 50)
    print('Apagar pet'.center(50))
    print('-' * 50)
    name = input(interface.text_blue('Digite o nome: '))
    user = pets.find_one({"name": name}, {"_id": 0, "name": 1})
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
        print(f'{interface.text_yellow("[1]")} {interface.text_blue("Listar Pets")}')
        print(f'{interface.text_yellow("[2]")} {interface.text_blue("Pesquisar Pet")}')
        print(f'{interface.text_yellow("[3]")} {interface.text_blue("Cadastrar Pet")}')
        print(f'{interface.text_yellow("[4]")} {interface.text_blue("Alterar Pet")}')
        print(f'{interface.text_yellow("[5]")} {interface.text_blue("Apagar Pet")}')
        print(f'{interface.text_yellow("[6]")} {interface.text_blue("Sair")}')

        print('-' * 50)
        opt = input(interface.text_yellow('Sua opção: '))
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