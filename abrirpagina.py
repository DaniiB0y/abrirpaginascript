from string import *
import webbrowser as web
from bs4 import BeautifulSoup as bs
import requests


fala = str(input('Digite seu comando: '))
if(fala.count("abrir")):
    fala = fala.replace("abrir", "")
    fala = fala.replace(" ", "+")
    #Tratamento de string
    e = "&"
    #O python não reconhece o & então vamos armazenar em uma variavel
    page = requests.get(f"https://www.google.com/search?q={fala}{e}oq={fala}{e}aqs=chrome..69i57j35i39j35i39i457j69i60l2j69i65j69i60l2.652j0j7&sourceid=chrome&ie=UTF-8")
    soup = bs(page.text, 'html.parser')
    # Parseamento e pegando conteudo da pagina
    links = soup.find_all("a")
    # Pegando todos os links e selecionando um
    link = links[17]
    link = link['href']
    link = link.replace("/url?q=", "")
    # Tratamento de string
    web.open(f'{link}', new=0, autoraise=True)
