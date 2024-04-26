conjunto = {'python', 'cebola', 'carne', 'cebola'}
comida = {'macarrao','milho','frango','milho','tomate','cebola'}

for i, elemento in enumerate(comida):
    print(i, elemento)

print(conjunto.intersection(comida))
print(conjunto.difference(comida))
print(conjunto.symmetric_difference(comida))

# elementos contidos
print(conjunto.issubset(comida))

# elementos nao contidos
print(conjunto.issuperset(comida))


# DICIONARIO

dados = {
    "yaguera@gmail.com":{"nome":"Yago", "idade":25,"telefone":33333333},
    "filipi@gmail.com":{"nome":'Filipe',"idade":30,"telefone":45241434}
}

telefone = dados['filipi@gmail.com']["telefone"]
telefone2 = dados['yaguera@gmail.com']["telefone"]
print(telefone)
print(telefone2)


