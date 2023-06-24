import requests
from bs4 import BeautifulSoup

# Requisitar uma página e pegar o conteúdo dela
html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/56/salvador-ba').content

# Parsei sobre o conteúdo HTML
soup = BeautifulSoup(html, 'html.parser')

# Titulo da página
titulo = soup.title.text

# Busquei os elementos HTML
texto = soup.find(class_ = '-gray -line-height-24 _center') #Class_ para buscar elementos com class. Class é uma palavra reservd
temp_min = soup.find(id = 'min-temp-1')
temp_max = soup.find(id = 'max-temp-1')
img_tag = soup.find(class_= 'logo')
alt_text = img_tag['alt']
resumo = texto.text.split()
texto_clear = ' '.join(resumo)
# Exibir valores encontrados

print("\nA empresa:" , alt_text)
print(titulo)
print("Temperatura minima: " , temp_min.text)
print("Temperatura maxima: " , temp_max.text)
print("Resumo do clima:" , texto_clear)

