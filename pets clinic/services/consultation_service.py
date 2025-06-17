from models.consultation import consultation
from utils import interface

def show():
    interface.clear_console()
    print('-' * 50)
    print('Lista de Consultas'.center(50))
    print('-' * 50)
    resultados = consultation.find({})
    found = False
    for x in resultados:
        print(f"{interface.text_blue("Nome:")} {x['name']}")
        print(f"{interface.text_blue("Preço:")} {x['price']}")
        print()
        found = True
    if not found:
        print(f'{interface.text_red('Nenhuma consulta encontrada')}')
    input()

def insert():
    interface.clear_console()
    print('-' * 50)
    print('Agendar nova consulta'.center(50))
    print('-' * 50)
    name = input(interface.text_blue('Nome: '))
    price = input(interface.text_blue('Preço: '))
    consultation.insert_one({"name": name, "price": price})
    print()
    print(interface.text_green('Consulta agendada com sucesso'))
    input()

def update():
    interface.clear_console()
    print('-' * 50)
    print('Alterar Consulta'.center(50))
    print('-' * 50)
    name = input('Digite o nome do pet: ')
    user = consultation.find_one({"name": name}, {"_id": 0, "name": 1})
    if user is None:
        print(f'{interface.text_red('Nenhum animal encontrado')}')
        input()
        return

    while True:
        interface.clear_console()
        print("-" * 50)
        print(f"O que deseja alterar na consulta {name}?")
        print("-" * 50)
        print(f"{interface.text_yellow("[1]")} {interface.text_blue("Nome")}")
        print(f"{interface.text_yellow("[2]")} {interface.text_blue("Preço")}")
        print(f"{interface.text_yellow("[3]")} {interface.text_blue("Voltar")}")
        print("-" * 50)
        opt = input('Sua opção:')
        if opt == "1":
            newName = input(interface.text_blue("Novo nome:"))
            consultation.update_one({"name": name}, {"$set": {"name": newName}})
            print("Nome alterado com sucesso")
            input()
            return
        elif opt == "2":
            newPrice = input(interface.text_blue("Novo preço:"))
            consultation.update_one({"name": name}, {"$set": {"price": newPrice}})
            print()
            print(interface.text_green("Preço alterado com sucesso"))
            input()
            return
        elif opt == "3":
            break
        else:
            interface.clear_console()
            print(f'{interface.text_red("Opção Inválida")}')
            input()

def delete():
    interface.clear_console()
    print('-' * 50)
    print('Apagar consulta'.center(50))
    print('-' * 50)
    name = input('Digite o nome: ')
    user = consultation.find_one({"name": name}, {"_id": 0, "name": 1, "email": 1})
    if user is None:
        print(f'{interface.text_red('Nenhum serviço encontrado')}')
        input()
        return

    interface.clear_console()
    confirm = input(f'Tem certeza de que deseja apagar {name}? (S/n)')
    if confirm == 'S' or confirm == '':
        consultation.delete_one({"name": name})
        print(interface.text_green("Serviço removido com sucesso"))
    else:
        print(f'{interface.text_red('Ação cancelada')}')
    input()

def menu():
    while True:
        interface.clear_console()
        print('-' * 50)
        print('Consultas'.center(50))
        print('-' * 50)
        print(f'{interface.text_yellow("[1]")} {interface.text_blue("Listar")}')
        print(f'{interface.text_yellow("[2]")} {interface.text_blue("Agendar")}')
        print(f'{interface.text_yellow("[3]")} {interface.text_blue("Alterar")}')
        print(f'{interface.text_yellow("[4]")} {interface.text_blue("Apagar")}')
        print(f'{interface.text_yellow("[5]")} {interface.text_blue("Voltar")}')

        print('-' * 50)
        opt = input(interface.text_yellow('Sua opção: '))
        if opt == '1':
            show()
        elif opt == '2':
            insert()
        elif opt == '3':
            update()
        elif opt == '4':
            delete()
        elif opt == '5':
            break
        else:
            interface.clear_console()
            print(opt)
            print(f'{interface.text_red("Opção Inválida")}')
            input()