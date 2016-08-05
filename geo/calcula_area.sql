select st_area(st_transform(campo_geom, 96820))/1000000 as area from pais
