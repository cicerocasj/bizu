import requests
import glob
import homura
import tarfile
import os
import shutil
import random
import bs4
import pandas as pd


class Usgs(object):
    def __init__(self):
        self.download_dir = str()
        self.cena = str()
        self.tar_saida = str()
        self.pasta_saida = str()
        self.username = str()
        self.senha = str()
        self.logado = False
        self.interesse = str()
        self.arquivo_download = str()
        self.pasta_tmp = str()
        self.o_p_interesse = list()
        self.catalogo = None
        self.arquivo_full = '/dados/catalogo/LANDSAT_8_C1.csv.gz'

    def login(self, usuario, senha):
        self.username = usuario
        self.senha = senha
        url_login = 'https://ers.cr.usgs.gov/login/'

        self.sessao = requests.Session()
        login = self.sessao.get(url_login)
        conteudo_login = login.content
        html = bs4.BeautifulSoup(conteudo_login, "html.parser")

        __ncforminfo = html.find("input", {"name": "__ncforminfo"}).attrs.get("value")
        csrf_token = html.find("input", {"id": "csrf_token"}).attrs.get("value")

        auth = {"username": usuario, "password": senha, "csrf_token": csrf_token, "__ncforminfo": __ncforminfo}

        self.sessao.post(url_login, data=auth, allow_redirects=False)
        if not self.check_login():
            raise Exception('login error: is_logged = False')
        else:
            self.logado = True

    def check_login(self):
        profile = self.sessao.get('https://ers.cr.usgs.gov/profile/password')
        conteudo_profile = profile.content
        html = bs4.BeautifulSoup(conteudo_profile, "html.parser")
        return html.find("input", {"name": "username"}).attrs.get("value") == self.username

    def download(self, cena, pasta_saida):
        if not self.logado:
            raise Exception('usuario nao esta logado')
        self.pasta_saida = pasta_saida
        url_download = "https://earthexplorer.usgs.gov/download/12864/%s/STANDARD/EE" % cena
        self.arquivo_download = os.path.join(pasta_saida, '%s.tar.gz' % cena)
        print url_download, self.arquivo_download
        homura.download(url_download, self.arquivo_download, session=self.sessao)

    def cria_tar_filtrado(self):
        print 'cria pasta tmp'
        randomhash = str(random.getrandbits(50))
        self.pasta_tmp = os.path.join("/tmp", "downloading_%s" % randomhash)
        if not os.path.exists(self.pasta_tmp):
            os.mkdir(self.pasta_tmp)

        print "extraindo o tar..."
        tar = tarfile.open(self.arquivo_download, 'r:gz')
        tar.extractall(self.pasta_tmp)
        tar.close()

        print "filtra arquivos de interesse..."
        quantidade_inicial = len(os.listdir(self.pasta_tmp))
        arquivos_interesse = self.filtra_arquivos_interesse(self.pasta_tmp)

        print "Arquivos para ser apagado:", quantidade_inicial - len(arquivos_interesse)
        for lixo in glob.glob('%s/*' % self.pasta_tmp):
            if lixo not in arquivos_interesse:
                print 'deletando', lixo
                os.remove(lixo)

        print "criando tar novo..."
        tar = tarfile.open(self.arquivo_download, "w:gz")
        for util in arquivos_interesse:
            tar.add(util, arcname=os.path.basename(util))
        tar.close()

        print "removendo pasta temp..."
        if os.path.exists(self.pasta_tmp):
            shutil.rmtree(self.pasta_tmp)

    def filtra_arquivos_interesse(self, pasta):
        return sorted(glob.glob("%s/*[%s].*" % (pasta, self.interesse)))

    def carrega_catalogo(self, arquivo=None):
        self.catalogo = pd.read_csv(arquivo or self.arquivo_full, compression='gzip')
        self.catalogo.head()

    def gera_catalogo_interesse(self, nome_arquivo, o_ps=list()):
        if self.catalogo is None:
            self.carrega_catalogo()
        dfs = []
        for op in o_ps:
            dfs.append(self.catalogo[self.catalogo['sceneID'].str.contains('%s' % op.replace('_', ''))])
        df = pd.concat(dfs).sort_values(['acquisitionDate'], ascending=True, kind='quicksort')
        df.to_csv(nome_arquivo, index=False, compression='gzip')
