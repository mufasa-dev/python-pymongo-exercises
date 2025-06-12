from services import pet_service
from services import service_service
from utils import interface

def main():
    while True:
        interface.clear_console()
        print('-' * 50)
        print('Cadastro de pets'.center(50))
        print('-' * 50)
        print('[1] Pets')
        print('[2] Tutores')
        print('[3] Serviços')
        print('[4] Consultas')
        print('[5] Sair')

        opt = input('Sua opção:')
        if opt == '1':
            pet_service.menu()
        elif opt == '2':
            service_service.menu()
        elif opt == '3':
            break
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