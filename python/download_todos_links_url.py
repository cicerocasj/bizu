import bs4
import requests
import homura
import os

url_principal = 'http://page.com'
path_saida = "/tmp/download"

conteudo = requests.get(url_principal).content

html = bs4.BeautifulSoup(conteudo, "html.parser")
links = html.find_all("a")

if not os.path.exists(path_saida):
    os.makedirs(path_saida)

for k, i in enumerate(links):
    arquivo = i.attrs.get("href")
    print k, arquivo,
    url = url_principal + arquivo
    homura.download(url, "%s/%s" % (path_saida, arquivo))
    print "fim"
