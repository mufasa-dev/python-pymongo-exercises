from services import (pet_service,
                      service_service,
                      tutor_service)
from utils import interface

def main():
    while True:
        interface.clear_console()
        print('-' * 50)
        print('Clínica de Pets'.center(50))
        print('-' * 50)
        print(f'{interface.text_yellow("[1]")} {interface.text_blue("Pets")}')
        print(f'{interface.text_yellow("[2]")} {interface.text_blue("Tutores")}')
        print(f'{interface.text_yellow("[3]")} {interface.text_blue("Serviços")}')
        print(f'{interface.text_yellow("[4]")} {interface.text_blue("Consultas")}')
        print(f'{interface.text_yellow("[5]")} {interface.text_blue("Sair")}')

        print('-' * 50)
        opt = input(interface.text_yellow('Sua opção: '))
        if opt == '1':
            pet_service.menu()
        elif opt == '2':
            tutor_service.menu()
        elif opt == '3':
            service_service.menu()
        elif opt == '4':
            break
        elif opt == '5':
            break
        else:
            interface.clear_console()
            print(opt)
            print(f'{interface.text_red("Opção Inválida")}')
            input()

if __name__ == "__main__":
    main()