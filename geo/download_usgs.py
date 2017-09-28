import requests
import progressbar
import bs4
import glob
import tarfile
import os
import shutil
import random
import homura


class Downloader(object):
    def __init__(self, download_dir="/tmp", username="", password=""):
        self.download_dir = download_dir
        self.username = username
        self.password = password
        self.cena = str()
        self.tar_saida = str()
        randomhash = str(random.getrandbits(50))
        self.pasta_tmp = os.path.join("/home/cicero", "aqml_%s" % randomhash)
        if not os.path.exists(self.pasta_tmp):
            os.mkdir(self.pasta_tmp)
        self.login()

    def login(self):
        url_login = 'https://ers.cr.usgs.gov/login/'

        self.sessao = requests.Session()
        login = self.sessao.get(url_login)
        conteudo_login = login.content
        html = bs4.BeautifulSoup(conteudo_login, "html.parser")

        __ncforminfo = html.find("input", {"name": "__ncforminfo"}).attrs.get("value")
        csrf_token = html.find("input", {"id": "csrf_token"}).attrs.get("value")

        auth = {"username": self.username, "password": self.password, "csrf_token": csrf_token, "__ncforminfo": __ncforminfo}

        self.sessao.post(url_login, data=auth, allow_redirects=False)

    def _download(self, cena, saida):
        download = "https://earthexplorer.usgs.gov/download/12864/%s/STANDARD/EE" % cena
        homura.download(download, saida, session=self.sessao)

    def download(self, cena):
        self.cena = cena
        self.tar_saida = os.path.join(self.pasta_tmp, '%s.tar.gz' % self.cena)
        try:
            self._download(cena, self.tar_saida)
            self.padroniza_download()
        except Exception as e:
            print e
            return False
        else:
            return True
        finally:
            pass
            if os.path.exists(self.pasta_tmp):
                shutil.rmtree(self.pasta_tmp)

    def envia_local_destino(self):
        shutil.copy2(self.tar_saida, self.download_dir)

    def padroniza_download(self):
        tar = tarfile.open(self.tar_saida, 'r:gz')
        tar.extractall(self.pasta_tmp)
        arquivos = self.filtra_arquivos_interesse(self.pasta_tmp)

        for lixo in glob.glob('%s/*' % self.pasta_tmp):
            if lixo not in arquivos:
                os.remove(lixo)

        for arquivo in arquivos:
            saida = os.path.join(self.pasta_tmp, "%s_%s" % (self.cena, arquivo.split("_")[-1]))
            shutil.move(arquivo, saida)
            print arquivo

        arquivos = self.filtra_arquivos_interesse(self.pasta_tmp)
        tar = tarfile.open(self.tar_saida, "w:gz")
        for util in arquivos:
            tar.add(util, arcname=os.path.basename(util))
        tar.close()
        self.envia_local_destino()

    def filtra_arquivos_interesse(self, pasta):
        return sorted(glob.glob("%s/*[B2,B3,B4,B5,B6,B7,B8,BQA,MTL].*" % pasta))


if __name__ == '__main__':
    api = Downloader(download_dir="/tmp", username='user_usgs', password='password_usgs')
    downloaded = api.download('LC82210672017253LGN00')
    print downloaded


