import requests
import openpyxl
from datetime import date

chave = "e92cef9a5f587783fc36b00f48b9aa77"

cidade = input("Digite a cidade em que quer obter as informações! ")
endereco = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&lang=pt_br&units=metric"

requisicao = requests.get(endereco)

def criarplanilha(cidade, temperatura_minima, temperatura_maxima, clima_atual):
    data_atual = date.today()
    # Cria um novo arquivo do Excel
    workbook = openpyxl.Workbook()

    # Seleciona a primeira aba (Sheet1)
    worksheet = workbook.active

    # Escreve alguns dados na célula A1
    worksheet['A1'] = 'Dados do Python'

    # Escreve mais alguns dados nas células abaixo
    worksheet['A2'] = 'Temperatura Mínima'
    worksheet['A3'] = 'Temperatura Máxima'
    worksheet['A4'] = 'Clima atual'
    worksheet['A5'] = 'Cidade'
    
    worksheet['B2'] = temperatura_minima
    worksheet['B3'] = temperatura_maxima
    worksheet['B4'] = clima_atual
    worksheet['B5'] = cidade

    # Salva o arquivo
    workbook.save(f'dados{cidade}_{data_atual}.xlsx')
    


if requisicao.status_code == 200:
    data = requisicao.json()
    clima_atual = data['weather'][0]['description']
    temperatura_minima = round(data['main']['temp_min'])
    temperatura_maxima = round(data['main']['temp_max'])
    cidade_selecionada = data['name']
     
    criarplanilha(cidade_selecionada, temperatura_minima, temperatura_maxima, clima_atual)
    print('========================')
    print('     TEMPERATURA')
    print('========================')
    print(f'Mínima: {temperatura_minima}\nMáxima: {temperatura_maxima}\nO clima está: {clima_atual}\nCidade: {cidade_selecionada}')

else:
    data = requisicao.json()
    print(f'Erro código: ' + str(data['cod']) + ', entre em contato com o administrador!')
    
