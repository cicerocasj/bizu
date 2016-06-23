conjunto = range(100)
remover = [1,2,3,11,12,13]
conjunto = [v for k, v in enumerate(conjunto) if k not in remover]
