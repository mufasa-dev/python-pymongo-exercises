from services import pet_service
from utils.interface import clear_console

def main():
    while True:
        clear_console()
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
            pet_service.show_pets()
        elif opt == '2':
            pet_service.search_pet()
        elif opt == '3':
            pet_service.insert_pet()
        elif opt == '4':
            pet_service.update_pet()
        elif opt == '5':
            pet_service.delete_pet()
        elif opt == '6':
            break
        else:
            clear_console()
            print(opt)
            print('\033[031mOpção Inválida\033[m')
            input()

if __name__ == "__main__":
    main()