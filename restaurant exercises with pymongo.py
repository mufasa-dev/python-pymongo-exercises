import pymongo      

meucli = pymongo.MongoClient("mongodb://localhost:27017/")    

# 1 Utilizando o powershell, crie um banco de dados chamado restaurante_db, 
# uma coleção restaurantes e insira 3 restaurantes com, pelo menos, duas avaliações
# para cada restaurante.
meudb = meucli["restaurate_db"]
restaurants = meudb["restaurantes"]

restaurants.insert_many([
    {
        "nome": "Pizzaria Napolitena",
        "endereco": "Rua uva, 25",
        "categoria": "Pizzaria",
        "avaliacoes": [
            {"cliente": "João", "nota": 4.5, "comentario": "veio fria"},
            {"cliente": "Carlos", "nota": 5, "comentario": "Otima pizza"}
        ]
    },
    {
        "nome": "Dogão do Zé",
        "endereco": "Rua laranja, 12",
        "categoria": "Lanchonete",
        "avaliacoes": [
            {"cliente": "João", "nota": 5, "comentario": "Otimo lanche"},
            {"cliente": "Carlos", "nota": 5, "comentario": "Entregador simpatico"}
        ]
    },
    {
        "nome": "Haishi",
        "endereco": "Rua arroz, 1",
        "categoria": "Restaurante Japones",
        "avaliacoes": [
            {"cliente": "Musashi", "nota": 5, "comentario": "Kono tatemono wa oishi desu"},
            {"cliente": "Murasaki", "nota": 5, "comentario": "Kono Restorante wa sugoi desu"}
        ]
    }
])

# 2 Liste apenas os nomes e categorias dos restaurantes.
exibicao = {"nome": 1, "categoria": 1}

for x in restaurants.find({}, exibicao):
     print(x)

# 3 Liste todas as avaliações feitas para um restaurante específico
print(restaurants.find_one({"nome": "Pizzaria Napolitena"}, {"avaliacoes": 1}))

# 4 Liste o nome e o endereço dos restaurantes da categoria "Restaurante Japones"
consulta = {"categoria": "Restaurante Japones"}

for x in restaurants.find(consulta, {"nome": 1, "endereco": 1}):
     print(x)

# 5 Adicione uma nova avaliação para o restaurante "Dogão do Zé"
novaAvaliacao = {"cliente": "Patricia", "nota": 5, "comentario": "Restaurante muito limpo e arrumado"}
consulta = {"nome": "Dogão do Zé"}

x = restaurants.update_one(consulta, {"$push": novaAvaliacao})

print(x)
print(restaurants.find_one(consulta))

# 6 Atualize a nota de uma avaliação
consulta = {"avaliacoes.cliente": "Carlos"}
novoValor = {"$set": {"nota": 4.5}}

x = restaurants.update_one(consulta, novoValor)
print(x)

# 7 Remova uma avaliação
consulta = {"avaliacoes.cliente": "Carlos"}

x = restaurants.update_one(consulta, {"$pull": novaAvaliacao})
print(x)

# 8 Remova o restaurante "Haishi"
x = restaurants.delete_one({"nome": "Haishi"})
print(x)

# 9 Liste o nome dos restaurantes que possuem avaliações com nota maior ou igual a 4.5
consulta = {"avaliacoes.nota": {"$gte": 4.5}}

for x in restaurants.find(consulta, {"nome": 1, "_id": 0}):
     print(x)

# 10 Liste o nome do restaurante e a média das avaliações de cada um
for x in restaurants.find({}, {"nome": 1, "mediaAvaliacoes": {"$avg": "$nota"}}):
	print(x)
