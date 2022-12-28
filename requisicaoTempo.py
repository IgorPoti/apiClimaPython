import requests

chave = "e92cef9a5f587783fc36b00f48b9aa77"

cidade = input("Digite a cidade em que quer obter as informações! ")
endereco = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&lang=pt_br&units=metric"

requisicao = requests.get(endereco)

if requisicao.status_code == 200:
    data = requisicao.json()
    clima_atual = data['weather'][0]['description']
    temperatura_minima = round(data['main']['temp_min'])
    temperatura_maxima = round(data['main']['temp_max'])
    cidade_selecionada = data['name']
     
    print('========================')
    print('     TEMPERATURA')
    print('========================')
    print(f'Mínima: {temperatura_minima}\nMáxima: {temperatura_maxima}\nO clima está: {clima_atual}\nCidade: {cidade_selecionada}')

else:
    print('Houve um erro na requisição!')
    
    