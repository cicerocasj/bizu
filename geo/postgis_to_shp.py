import subprocess
pcall = """ogr2ogr -overwrite -skipfailures -s_srs EPSG:4326 -t_srs EPSG:4326 -f 'ESRI Shapefile' {arquivo_tmp} PG:'{conexao}' -sql "{sql}" """.format(
    arquivo_tmp="/tmp/out.shp", conexao="dbname=123 host=123 user=123 password=123", sql="select id, geom from pais"
)
erro = subprocess.call(pcall, shell=True) # 0: success
