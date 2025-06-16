from models.tutor import tutor
from utils import interface

def show_tutors():
    interface.clear_console()
    print('-' * 50)
    print('Lista de Tutores'.center(50))
    print('-' * 50)
    resultados = tutor.find({}, {"_id": 0, "name": 1})
    found = False
    for x in resultados:
        print(f"Nome: {x['name']}")
        found = True
    if not found:
        print(f'{interface.text_red('Nenhum animal encontrado')}')
    input()

def search_tutors():
    interface.clear_console()
    print('-' * 50)
    print('Pesquisar Tutor'.center(50))
    print('-' * 50)
    name = input('Nome: ')
    resultados = list(tutor.find({"name": name}, {"_id": 0, "name": 1, "email": 1}))
    if resultados:
        for x in resultados:
            print(x)
    else:
        print(f'{interface.text_red('Nenhum tutor encontrado')}')
    input()

def insert_tutors():
    interface.clear_console()
    print('-' * 50)
    print('Inserir novo Tutor'.center(50))
    print('-' * 50)
    name = input('Nome:')
    email = input('E-mail:')
    tutor.insert_one({"name": name, "email": email})
    print('Tutor inserido com sucesso')
    input()

def update_tutors():
    interface.clear_console()
    print('-' * 50)
    print('Alterar Tutor'.center(50))
    print('-' * 50)
    name = input('Digite o nome: ')
    user = tutor.find_one({"name": name}, {"_id": 0, "name": 1})
    if user is None:
        print(f'{interface.text_red('Nenhum tutor encontrado')}')
        input()
        return

    while True:
        interface.clear_console()
        print("-" * 50)
        print(f"O que deseja alterar no tutor {name}?")
        print("-" * 50)
        print("[1] Nome")
        print("[2] E-mail")
        print("[3] Voltar")
        opt = input('Sua opção:')
        if opt == "1":
            newName = input("Novo nome:")
            tutor.update_one({"name": name}, {"$set": {"name": newName}})
            print("Nome alterado com sucesso")
            input()
            return
        elif opt == "2":
            newEmail = input("Novo e-mail:")
            tutor.update_one({"name": name}, {"$set": {"email": newEmail}})
            print("E-mail alterado com sucesso")
            input()
            return
        elif opt == "3":
            break
        else:
            interface.clear_console()
            print(f'{interface.text_red("Opção Inválida")}')
            input()

def delete_tutors():
    interface.clear_console()
    print('-' * 50)
    print('Apagar tutor'.center(50))
    print('-' * 50)
    name = input('Digite o nome: ')
    user = tutor.find_one({"name": name}, {"_id": 0, "name": 1, "email": 1})
    if user is None:
        print(f'{interface.text_red('Nenhum tutor encontrado')}')
        input()
        return

    interface.clear_console()
    confirm = input(f'Tem certeza de que deseja apagar {name}? (S/n)')
    if confirm == 'S' or confirm == '':
        tutor.delete_one({"name": name})
        print("Tutor removido com sucesso")
    else:
        print(f'{interface.text_red('Ação cancelada')}')
    input()

def menu():
    while True:
        interface.clear_console()
        print('-' * 50)
        print('Cadastro de tutores'.center(50))
        print('-' * 50)
        print(f'{interface.text_yellow("[1]")} {interface.text_blue("Listar")}')
        print(f'{interface.text_yellow("[2]")} {interface.text_blue("Pesquisar")}')
        print(f'{interface.text_yellow("[3]")} {interface.text_blue("Cadastrar")}')
        print(f'{interface.text_yellow("[4]")} {interface.text_blue("Alterar")}')
        print(f'{interface.text_yellow("[5]")} {interface.text_blue("Apagar")}')
        print(f'{interface.text_yellow("[6]")} {interface.text_blue("Sair")}')

        print('-' * 50)
        opt = input(interface.text_yellow('Sua opção: '))
        if opt == '1':
            show_tutors()
        elif opt == '2':
            search_tutors()
        elif opt == '3':
            insert_tutors()
        elif opt == '4':
            update_tutors()
        elif opt == '5':
            delete_tutors()
        elif opt == '6':
            break
        else:
            interface.clear_console()
            print(opt)
            print(f'{interface.text_red("Opção Inválida")}')
            input()