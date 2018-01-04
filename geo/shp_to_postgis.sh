#gera SQL
shp2pgsql -a -e -s 4326 -W utf-8 -N skip arquivo.shp public.tabela >> saida.sql
#SQL to postgres
psql -h localhost -p 5432 -U cicero nome_banco -f saida.sql -a
