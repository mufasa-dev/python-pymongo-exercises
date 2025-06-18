# 🐾 Clínica Veterinária - Sistema de Gestão com Python e MongoDB

Este projeto é um sistema simples de gestão para uma clínica veterinária, desenvolvido em **Python** e utilizando o banco de dados **MongoDB** com o driver **PyMongo**.

---

## 📋 Funcionalidades

O sistema realiza o gerenciamento de quatro entidades principais:

- **Pets**
  - Cadastro de pets
  - Listagem
  - Busca por nome
  - Atualização
  - Remoção

- **Tutores**
  - Cadastro de tutores (donos dos pets)
  - Listagem e busca
  - Atualização e exclusão

- **Serviços**
  - Definição de serviços oferecidos (banho, consulta, vacinação, etc.)
  - Gerenciamento dos serviços (CRUD)

- **Consultas**
  - Registro de consultas entre tutores, pets e serviços
  - Listagem de histórico por pet ou tutor

---

## 🧰 Tecnologias Utilizadas

- Python 3.10+
- MongoDB
- PyMongo
- Terminal interativo

---

## 🗂️ Estrutura de Pastas

```bash
.
├── models/              # Modelos de dados (schemas)
│   ├── pet.py
│   ├── tutor.py
│   ├── service.py
│   └── consultation.py
├── services/            # Regras de negócio (camada service)
│   ├── pet_service.py
│   ├── tutor_service.py
│   ├── service_service.py
│   └── consultation_service.py
├── db.py                # Conexão com o MongoDB
├── utils/               # Cores dos menus
│   └── inteface.py
├── app.py              # Menu principal de navegação
└── README.md
````

---

## ⚙️ Requisitos

* Python 3 instalado
* MongoDB em execução local (ou remotamente)
* pip para instalar dependências

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/mufasa-dev/python-pymongo-exercises.git
cd nome-do-repositorio
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie o MongoDB (caso esteja local):

```bash
sudo systemctl start mongod
```

4. Execute o projeto:

```bash
python3 app.py
```

---

## 🧪 Exemplos de Dados

Você pode cadastrar:

* **Pets**: Nome, espécie, idade, tutor relacionado
* **Tutores**: Nome, telefone, email
* **Serviços**: Tipo de serviço, descrição, preço
* **Consultas**: Data, pet, serviço e tutor vinculados

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou quiser expandir a aplicação, sinta-se à vontade para enviar um PR ou abrir uma issue.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.
