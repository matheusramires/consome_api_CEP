import requests

cep = input("digite o cep: ")

url = (f'https://viacep.com.br/ws/{cep}/json/')
request = requests.get(url)
dados = request.json()
cep_numero = dados["cep"]
logradouro = dados["logradouro"]
bairro = dados["bairro"]
cidade = dados["localidade"]
uf = dados["uf"]
ddd = dados["ddd"]

print(f'CEP: {cep_numero}\nRua: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nUF: {uf}\nDDD: {ddd}')