#Dataframe é uma tabela dentro do python, onde cada coluna da tabela é uma série do pandas
#Se um dia encontrar "pd.serie", ou seja, uma serie do pandas é uma coluna do seu dataframe/tabela

import pandas as pd
import openpyxl #O pandas precisa da biblioteca openpyxl para trabalhar com arquivos do Excel no formato .xlsx .
#from IPython.display import display

# === Criando um dataframe a partir de um dicionário do python ===
venda = {'data': ['15/02/2021','16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50,70],}

vendas_df = pd.DataFrame(venda)

#=== Visualização do DataFrame ===
print(vendas_df)

#display(vendas_df) #Visualiza melhor as informações

#=== Importando arquivos e bases de dados ===
vendas_df = pd.read_excel("Vendas.xlsx") #Vai ler o arquivo excel "Vendas" e vai transformar esse arquivo em uma tabela
#Se o arquivo estiver em outro lugar tem que colocar o caminho do arquivo em Excel
#vendas_df = pd.read_excel("C://Users/Bruno/download/Vendas.xlsx")
display(vendas_df) #Visualizando o dataframe/tabela do arquivo Excel

#=== Resumos de Visualização de Dados simples e úteis ===
display(vendas_df.head()) #O metodo head só mostra os 5 primeiros itens/linhas do DataFrame

display(vendas_df.head(10)) #Caso eu queira mostrar os 10 primeiros itens/linhas do DataFrame

print(vendas_df.shape) #O metodo shape, mostra quantos linhas e quantos colunas tem dentro da sua tabela. Independente do tamanho da tabela, esse comando executa muito rapido

display(vendas_df.describe()) #Esse comando vai pegar as colunas númericas e vai dar o resumo

produtos = vendas_df['Produto'] #Quero visualizar na tela, somente uma coluna do arquivo excel, ou seja, a coluna "Produto"
display(produtos)

produtos = vendas_df[['Produto', 'ID Loja']]#Quero visualizar na tela, somente duas coluna do arquivo excel, ou seja, a coluna "Produto" e a coluna "ID Loja"
display(produtos)

#Metodo .loc permite pegar:
# Pegar 1 unica linha
# Pegar linhas de acordo com alguma condição. Exemplo: Quero pegar todas as linhas da loja "iguatemi esplanada", ou todas as linhas do produto "calça"
# Pegar linhas e colunas especificas. Exemplo: Quero conseguir pegar as duas últimas colunas até a decima linha da minha tabela
# Pegar um valor especifico 

#Exemplo: Pegando uma linha
vendas_df.loc

#Exemplo: Pegando uma linha especifica
display(vendas_df.loc[1])

#Exemplo: Pegando uma linha especifica, nesse caso da linha 1 até a linha 5
display(vendas_df.loc[1:5])

#Pegar linhas que correspondem a uma condição