# 🍽️ Aplicação de Gerenciamento de Restaurantes com MongoDB e PyMongo

Este é um projeto em Python que permite gerenciar uma base de dados de **restaurantes** utilizando **MongoDB** como banco de dados e **PyMongo** como driver de conexão.

## 🔧 Funcionalidades

O usuário pode, através de um menu interativo no terminal:

- ➕ **Adicionar** novos restaurantes
- 🍽️ **Consultar** lista todos os restaurantes
- ✏️ **Editar** informações de um restaurante
- 🗑️ **Excluir** um restaurante
- ⭐ **Avaliar** um restaurante (adicionar avaliações)
- 📝 **Editar** uma avaliação existente
- ❌ **Excluir** uma avaliação
- 🔍 **Consultar Avaliação** ver sa avaliações de um restaurante
- ✴️ **Mostrar média de avaliações** lista todos os restaurantes e a média de avaliações

As avaliações podem conter:

- Nome do cliente avaliador
- Nota (0 a 5)
- Comentário

---

## 🛠️ Requisitos

- Python 3.7+
- MongoDB (instalado e rodando localmente ou em um servidor)
- Bibliotecas Python:
  - `pymongo`

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/mufasa-dev/python-pymongo-exercises.git
   cd python-pymongo-exercises


2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install pymongo
   ```

---

## 🚀 Como Usar

1. Certifique-se de que o MongoDB está rodando localmente (ou edite a URI de conexão no código).

2. Execute o script principal:

   ```bash
   python app.py
   ```

3. Use o menu interativo para navegar pelas opções disponíveis:

   ```
   ==== MENU ====
   [1] Inserir novo restaurante
   [2] Consultar todos os restaurantes
   [3] Atualizar um restaurante
   [4] Excluir restaurante
   [5] Avaliar restaurante
   [6] Mostrar avaliações de um restaurante
   [7] Alterar uma avaliação
   [8] Excluir uma avaliação
   [9] Mostrar média de avaliações
   [10]Sair
   ```

---

## 🗃️ Estrutura do Banco (Exemplo)

```json
{
  "nome": "Pizza da Casa",
  "endereco": "Rua das Flores, 123",
  "categoria": "Pizzaria",
  "avaliacoes": [
    {
      "cliente": "João",
      "nota": 4,
      "comentario": "Muito boa a pizza!"
    },
    {
      "cliente": "Maria",
      "nota": 5,
      "comentario": "Excelente atendimento."
    }
  ]
}
```


## 🧑‍💻 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para abrir *issues* ou enviar *pull requests*.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT.
