from string import *
import webbrowser as web

# Mostrar url usando o navegador padrão. Se o novo for 0, a url é aberto na mesma janela do navegador,
# se possível. Se é novo 1, uma nova janela do navegador é aberto, se possível.

fala = str(input('Digite seu comando: '))
#Pegando a frase 
if(fala.count("abrir")):
    fala = fala.replace("abrir", "")
    fala = fala.replace(" ", "")
    #tirando abrir pra ficar só o nome do site
    #tirando o espaço para ficar sem espaço, 22/10/2020 não funcionou com .split()
    print(f" Abrindo {fala}")
    #Informando ao usuario que está sendo aberto
    web.open(f'https://www.{fala}.com', new=0, autoraise=True)
else:
    print("Eror 404")
