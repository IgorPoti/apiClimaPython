import requests

chave = "e92cef9a5f587783fc36b00f48b9aa77"

cidade = input("Digite a cidade em que quer obter as informações! ")
endereco = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&lang=pt_br&units=metric"

requisicao = requests.get(endereco)

if requisicao.status_code == 200:
    data = requisicao.json()
    climaAtual = data['weather'][0]['description']
    temperaturaMinima = round(data['main']['temp_min'])
    temperaturaMaxima = round(data['main']['temp_max'])
    cidadeSelecionada = data['name']
     
    print('========================')
    print('     TEMPERATURA')
    print('========================')
    print(f'Mínima: {temperaturaMinima}\n Máxima: {temperaturaMaxima}\n O clima está: {climaAtual}\n Cidade: {cidadeSelecionada}')

else:
    print('Houve um erro na requisição!')
    
    