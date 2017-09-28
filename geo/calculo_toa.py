ELEVATION = 0 # informacao no arquivo de metadado
mascara = numpy.array # leitura da banda
toa = (
         numpy.ma.masked_equal(
             mascara, 0
         ) * 0.00002 + -0.1
     ) * (
         1 / math.sin(math.radians(ELEVATION))
     )
