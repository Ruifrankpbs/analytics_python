#!/usr/bin/env python
# coding: utf-8

# # Parte 1 - Princípios Básicos

# # Principais tipo de Células no Notebook

# # Markdown
# ## Variando a quantidade de # eu posso variar o tamanho do texto
# ### com mais # o texto fica menor
# 
# #### o Markdown é um tipo de célula que usamos quando queremos documentar o código e escrever explicações que não irão fazer parte do programa ( não são linhas de código)

# In[2]:


#linha de código - Posso usar # na Linha de código para documentar etapas também, porém o texto não ficará formatado já que não é uma celular de Markdown.

print('Olá Mundo')


# # Python 
# 
# ## Python --> Linguagem de tipagem forte ---> Diferencia letras maiúsculas de minúsculas;
# 
# ## Variável --> Usada para armazenar informações que usaremos com recorrência;
# 
#   ### Tipos de Variáveis mais comuns no Python:
#   
#   * String >>> Texto ( Definida sempre com um texto entre aspas simples ou duplas);
#   * Int >>>>>> Número Inteiro;
#   * Float >>>> Número Decimal ( Casa decimal sempre delimitada com ponto e não virgula);
#   * Bool >>>>> Booleano ( Verdadeiro ou Falso);
#   * Lista;
#   * Dicionário.
#   
#   ### Operações com variáveis
#   
#   * Operadores:
#    (+) Soma ( 2+3 = 5)
#    (-) Subtração (3-1 = 2)
#    (/) Divisão (2/2=1)
#    (^) Potência (2^3=8)
#    
#   * Operação com texto:
#    (+) Soma ( 'Oi' + '!' = Oi!)
#    (*) Multiplicação ('Oi' * 2=OiOi)
#    
#   * Comparação:
#    (==) >>>> Igual
#    (!=) >>>> Diferente
#    (>) >>>>> Maior
#    (>=) >>>> Maior ou Igual
#    (<) >>>>> Menor
#    (<=) >>>> Menor ou igual
#   
# 

# # Variáveis
# ## Usadas para armazenar informação que usamos de forma frequente.

# In[3]:


3


# In[9]:


numero=3


# In[10]:


numero


# ## Tipos de Variáveis no Python

# ### Texto

# In[15]:


# Texto - String

texto = 'Testando'


# In[16]:


texto


# In[17]:


# Replace substitui o primeiro elemento de texto pelo segundo dentro do ()

texto.replace ('T','t')


# In[18]:


texto.replace ('e', 'B')


# In[20]:


texto[0:3]


# In[21]:


texto[-2:]


# In[23]:


print (texto)


# ### número Inteiro - int

# In[24]:


inteiro = 3


# In[25]:


inteiro2 = 2


# In[26]:


inteiro+inteiro2


# ### número decimal - float

# In[27]:


floatt = 1.5


# In[28]:


floattt = 1.6


# In[29]:


floatt+floattt


# ### Booleano - Verdadeiro ou Falso

# In[30]:


print(floatt==floattt)


# In[31]:


#True tem o valor numerico de 1 e False tem valor numerico de 0

verdadeiro = True

falso = False

print(verdadeiro+falso)

print(verdadeiro+2)

print(verdadeiro *2)


# ### Listas

# In[33]:


isso_eh_uma_lista = [1,2,3,'quatro',5,5.2,True]

print(isso_eh_uma_lista)


# ### Dicionário
# Um dicionário é uma coleção com elementos chave-valor que permite representar melhor o mundo real. 

# In[37]:


dicionario = {'Rui':1, 'Silmara':2, 'Brenda':3}


# ### Operações com texto
# 

# In[45]:


texto01 = 'Eu'
texto02 = 'Programar'

print(texto01+' '+'AMO'+' ' +texto02)


# ### Operações com Listas

# In[46]:


ListaAdd =['z','y','w']

print(isso_eh_uma_lista+ListaAdd)


# In[ ]:





# # Funções Básicas:
# 
#     ### print() >>>> Imprime o texto ou variável entre parênteses na tela;
#     ### import >>> Carrega bibliotecas Python;
#     ### !pip install >> Instala bibliotecas Python.
#     
# ## Métodos
#     
#     ### São funções implícitas dentro de cada tipo de variável, acessadas usando ponto após a variável;
#         Ex. string.replace >>>> Substitui uma parte do texto por outra.
#         
# ### Instruções sobre o uso de funções e métodos >>> Shift + Tab ( Atalho no Jupyter Notebook)
# 
# 

# In[49]:


## Sobre Métodos: Métodos não subscrevem os valores de variáveis, somente se você informe isso no código;

    ##* Exemplo: se você chama uma variável e atribui um valor, e em seguida faz a alteração com algum método:

Varia ='Valor'


# In[51]:


Varia.replace('V', 'W')


# In[52]:


Varia


# In[53]:


## Então se você quer que o valor seja realmente alterado perpetuamente tem que informar da seguinte forma:

Varia = Varia.replace('V','WW')


# In[54]:


Varia


# # LISTAS
# 
# ## Usadas para armazenar vários valores dentro de uma mesma variável;
# ## Identificadas por colchetes ( EX: Lista = [1,2,3,'quatro', 5.2] )
# 
# ## Operações com listas:
# 
# * lista 1 + lista 2 = lista contendo todos os elementos da lista 1 e lista 2
# * lista 1 * 2 = Lista com informações da lista 1 repetidos 2 vezes
# 
# 
# # LISTAS - PRINCIPAIS MÉTODOS
# 
# ## lista.append(n) >>>> Adiciona o elemento n à lista
# ## lista.remove(n) >>>> Remove o elemento n da lista
# ## lista.sort() >>>>>>>> Ordena a lista
# ## lista.count(n) >>>>>> Conta quantos elementos n na lista
# ## lista.len() >>>>>>>>> Conta quantos elementos na lista
# ## lista.index(n) >>>>>> Retorna qual a posição do elemento n na lista
# 
# 
# # DICIONÁRIOS
# 
# ## Dicionários são usados para armazenar pares chave-valor, para posterior uso ou comparação;
# ## identificados por chaves;
# ## Muito usados para realizar de-para de chaves-valor.
# 
# * Ex> dicionario={'Primeiro':1, 'Segundo':2, 'Terceiro':3}
# 
# ## PRINCIPAIS MÉTODOS :
# 
# ### dict.keys() >>>>>>> Retorna as chaves armazenadas no dicionário
# ### dict.values() >>>>>> Retornas os valores armazenados no dicionario
# ### dict.get(n) >>>>>>>> Retorna o valor associado à chave no dicionario
# ### dict.pop(n)>>>>>>>> Remove a chave n e o valor associado a ela no dicionario
# 
# 

# # MÃO NA MASSA!!!

# ## Parte 2 - Listas
# 
# ### Listas são extremamente úteis no Python, quando queremos armazenar valores referentes a uma mesma medida ou dimensão, ou alguma informação que iremos ler sequencialmente;
# 
# ### Digamos que estamos anotando a idade de cada pessoa na turma, podemos usar uma lista para armazenar os resultados

# In[1]:


# Vamos dar o nome de idades para a Lista
# O colchete é o simbolo usado para delimitar uma lista

idades = [30,27,31,45,50,33,18,27,30]


# ### Agora que temos a lista, vamos tentar fazer algumas operações com esta lista.

# In[2]:


# digamos que eu queira a soma da lista
# Posso usar a função SUM para obter a soma:

sum(idades)


# ### Para operações mais complexas, veremos a Biblioteca Numpy que nos ajudará a fazer diversas operações matemáticas;
# ### Digamos que eu queira fazer mudanças na lista

# In[ ]:


# A lista nase é essa
idades


# In[3]:


# adicionando itens
idades.append(29)


# In[4]:


print(idades)


# In[5]:


# digamos que quero remover um item:
idades.remove(30)


# In[6]:


print(idades)


# In[7]:


# digamos que queremos multiplicar a lista, ou seja, os itens da lista serão duplicados:
idades*2


# ## Perceba que quando utilizamos os operadores append e remove, nós estamos modificando a lista existente.
# ## Quando eu simplesmente multiplico a lista, a variável da lista não se altera, apenas estou usando temporariamente os valores

# In[8]:


## Vamos criar uma segunda lista com as idades de uma segunta turma

idades2 = [15,25,30,33,25,28,51,36,56]


# In[9]:


# Digamos que queremos juntar as duas listas em uma:

idades.append(idades2)


# In[10]:


idades


# ## Perceba que agora temos uma lista dentro de outra lista, note que tem um grupo dentre de colchetes novamente, esses são os itens da segunda lista

# In[11]:


# Agora vamos verificar o tipo da variável

type(idades)


# In[12]:


type(idades2)


# ## Vamos verificar outros operadores de lista que são úteis
# 
# ### sort >>>>> Ordena os elementos da lista
# ### index>>>> Tras o indice do elemento que digitarmos em ( )
# ### count>>> Trás quantas vezes o item entre ( ) se repete na lista em questão

# In[13]:


# voltando à lista idades para o formato inicial
idades.remove(idades2)


# In[14]:


# Sort - Ordena os elementos

idades.sort()


# In[15]:


idades


# #### como pode ver a list está em ordem, do menor para o maior numero

# In[17]:


# Se verificarmos com o Shift TAB os parâmetros desse método, podemos ver que se colocarmos o parametro "reverse";
# Veremos que a lista ficará do valor maior para o menor:

idades.sort(reverse=True)


# In[18]:


idades


# In[20]:


# Vamos verificar agora a função index, que trará em qual indice estará o item que digitarmos no nosso codigo.
# Lembrando que a contagem dos indices sempre começa com o numero 0.


idades.index(30)


# In[21]:


# Nessa função podemos descobrir quantas vezes o item se repete em uma lista, no nosso caso 1 vez.

idades.count(30)


# In[22]:


# Agora queremos saber quantos elementos/itens temos na nossa lista;

len(idades)


# In[23]:


# Pegando algum elemento da lista, para isso devemos saber previamente o indice do elemento em questão;
# Em seguida informamos ele entre colchetes;
# Lembrando que a contagem de indices começa no 0;

idades[3]


# In[24]:


# Caso você queira criar uma lista vazia, basta colocar o nome da lista e os colchetes vazios;

lista = []


# # Parte 3 - Dicionários
# 
# ### Dicionários são usados como consultas, para checar o par chave-valor de uma chave que possa existir na sua base de dados. É uma maneira fácil de converter valores quando a correspondencia é conhecida
# 
# ### A principal característica de um dicionário é estar contido entre chaves { } ao contrário da lista que está contida dentre de colchetes [ ];
# 
# ### Os pares chave-valor são representados Chave:Valor

# In[25]:


# Pegando a lista de idades da última parte do curso

idades


# In[26]:


# Suponha que agora precisamos fazer uma correspondencia com o nome da pessoa 

nomes = ['Rui','Silmara','Brenda','Camila','Frank','Medeiros','Costa','Oliveira','Mara']


# In[27]:


dict_idades = {'Rui':50,'Silmara':45,'Brenda':33,'Camila':31,'Frank':30,
               'Medeiros':29,'Costa':27,'Oliveira':27,'Mara':18}


# In[28]:


# Método Get obtem o valor com base na chave que voce digitar entre ()

dict_idades.get('Brenda')


# In[29]:


# Uma dica muito legal, é que caso você queira criar um dicionário, e você não queira digitar tudo a mão;
# No nosso exemplo, tendo já as duas lista criadas a de idades e nomes, podemos criar o dicionário com...;
# A Função Zip, podemos criar rapidamente o dicionário com essas duas listas previamentes criadas;

dict_idades2 = dict(zip(nomes, idades))


# In[30]:


# Dessa forma, temos nosso dicionário rapidamente criado;b

dict_idades2


# ### Outros métodos usados em Dicionários

# In[31]:


# Método Keys - Retorna as chaves do dicionario

dict_idades2.keys()


# In[32]:


# Método Values - Retorna os valores do dicionário

dict_idades2.values()


# In[34]:


# Append - Adiciona elementos ao dicionário
# Note que vc nao precisa colocar .append, o python já entende que vc quer adicionar

dict_idades2['João'] = 48

dict_idades2


# In[35]:


# Pop - Remove elementos do dicionário

dict_idades2.pop('João')

dict_idades2


# In[36]:


# Atualizar elementos do dicionario

dict_idades2['Rui'] = 65

dict_idades2


# In[8]:



import os
import requests
from bs4 import BeautifulSoup

# Nomes dos jogadores a serem buscados
image_name = input("Insira o nome da imagem a ser buscada: ")

#Caminho da pasta onde as imagens serão salvas
path = input("Insira o caminho da pasta para salvar as imagens: ")

#Criando a pasta
if not os.path.exists(path):
    os.makedirs(path)

# Formatar o nome da imagem para usar na pesquisa
query = "+".join(image_name.split())
url = f"https://www.google.com/search?q={query}+images"

# Fazer a solicitação e obter o conteúdo da página
response = requests.get(url)
content = response.content

# Analisar o HTML
soup = BeautifulSoup(content, "html.parser")
img_tags = soup.find_all("img")

# Salvar as imagens
for i, img_tag in enumerate(img_tags):
    img_url = img_tag["src"]
    response = requests.get(img_url)
    open(f"{path}/{i}.jpeg", "wb").write(response.content)




# In[9]:


import csv

data = [["category","value"],
        ["frutas",20],
        ["legumes",10],
        ["carnes",5],
        ["pães",8],
        ["laticínios",7]
        ]

with open("data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)


# In[10]:


data


# In[11]:


get_ipython().system('pip install matplotlib')


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

# lendo o arquivo .csv
data = pd.read_csv("data.csv")

# Criando o gráfico de pizza
plt.pie(data["value"], labels=data["category"], autopct='%1.1f%%')
plt.axis('equal')
plt.title("Gráfico de pizza")
plt.show()


# In[13]:


get_ipython().system('pip install beautifulsoup4 requests')


# In[15]:



import os
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup

# função para buscar as imagens no site
def search_images(img_name):
    url = f"https://www.google.com/search?q={img_name}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    return urls

# perguntando ao usuário sobre o nome da imagem
img_name = input("Enter the name of the image you want to search: ")

# definindo o caminho para salvar as imagens
save_path = os.path.join(os.path.expanduser("~"), "Downloads")

# buscando imagens no site
urls = search_images(img_name)

# salvando as imagens
for i, url in enumerate(urls):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # redimensionando a imagem
    img = img.resize((1200, 800))

    # salvando imagem na pasta downloads
img.save(f"{save_path}/{img_name}_{i}.jpg")

print(f"{len(urls)} images saved to {save_path}")


# In[16]:


#!pip install requests BeautifulSoup4
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image

# definindo o caminho para salvar as imagens
save_path = os.path.join(os.path.expanduser("~"), "Downloads")

# função para buscar as imagens no google
def search_images(img_name):
    url = f"https://www.google.com/search?q={img_name}&tbm=isch"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    return urls[:5]

# buscando imagens no google
img_name = "neymar"
urls = search_images(img_name)

# salvando as imagens
for i, url in enumerate(urls):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # salvando imagem na pasta downloads
    img.save(f"{save_path}/{img_name}_{i}.jpg")

print(f"{len(urls)} images saved to {save_path}")


# In[17]:


get_ipython().system('pip install requests')


# In[18]:


import requests


# In[19]:


url = "https://images.ctfassets.net/3mv54pzvptwz/5eTv6hTyA1pqkFClYRn0qt/be626a573cbf1ee7e421b73f87ed6851/20221205_foto_GETTY_neymar_jr_jogo_brasil_x_coreia_copa_do_mundo__209_.jpg"


# In[20]:


response = requests.get(url)


# In[22]:


if response.status_code == 200:
    # requisição feita com sucesso!
else:
    # requisição falhou
    print('falhou')


# In[23]:


get_ipython().system('pip install matplotlib')


# In[24]:


get_ipython().system('pip install bs4')


# In[25]:


get_ipython().system('pip install requests')


# In[26]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# In[35]:


products = [
    {'name': 'Feijão'},
    
]


# In[41]:


name = ('Feijão')


# In[42]:


def get_price(name):
    url = "https://www.google.com/search?q="+name
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find("span", class_="a-price-whole").get_text()
    return price


# In[43]:


price


# In[37]:


for product in products:
    product['price'] = get_price(product['name'])


# In[44]:


get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')


# In[46]:


import requests
from bs4 import BeautifulSoup


# In[47]:


product_name = "iphone 12"


# In[59]:


url = "https://www.google.com/search?q=" + product_name
page = requests.get(url)


# In[60]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[61]:


price_element = soup.find("span", class_="a-price-whole")


# In[63]:


price = price_element.content[0]


# In[64]:


print("Preço encontrado: " + price)


# In[65]:


import pandas as pd
import matplotlib.pyplot as plt


# In[66]:


products = [
    {'name': 'Produto 1', 'brand':'Brand 1', 'price': 10.50, 'product_name':'Product 1'},
    {'name': 'Produto 2', 'brand':'Brand 2', 'price': 12.75,'product_name':'Product 2'},
    {'name': 'Produto 3', 'brand':'Brand 3', 'price': 15.00,'product_name':'Product 3'},
    {'name': 'Produto 4', 'brand':'Brand 1', 'price': 8.25,'product_name':'Product 4'}
]


# In[67]:


import csv
with open('precos_produtos.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'brand','price','product_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for product in products:
        writer.writerow(product)


# In[68]:


df = pd.read_csv("precos_produtos.csv")


# In[69]:


df.plot(kind='line', x='product_name', y='price')


# In[70]:


plt.xlabel("Nome dos produtos")
plt.ylabel("Preços")


# In[72]:


plt.show()


# In[73]:


plt.savefig("grafico_precos.png")


# In[74]:


import pandas as pd
import matplotlib.pyplot as plt
import csv

products = [
    {'name': 'Produto 1', 'brand':'Brand 1', 'price': 10.50, 'product_name':'Product 1', 'date':'01/01/2022', 'location':'City 1'},
    {'name': 'Produto 2', 'brand':'Brand 2', 'price': 12.75,'product_name':'Product 2', 'date':'01/02/2022', 'location':'City 2'},
    {'name': 'Produto 3', 'brand':'Brand 3', 'price': 15.00,'product_name':'Product 3', 'date':'01/03/2022', 'location':'City 3'},
    {'name': 'Produto 4', 'brand':'Brand 1', 'price': 8.25,'product_name':'Product 4', 'date':'01/04/2022', 'location':'City 1'}
]

def search_product(product_name):
    for product in products:
        if product['product_name'] == product_name:
            print(product)

with open('precos_produtos.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'brand','price','product_name','date','location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for product in products:
        writer.writerow(product)

df = pd.read_csv("precos_produtos.csv")
df.plot(kind='line', x='product_name', y='price')
plt.xlabel("Nome dos produtos")
plt.ylabel("Preços")
plt.savefig("grafico_precos.png")
plt.show()

product_name = input("Enter product name for search: ")
search_product(product_name)

