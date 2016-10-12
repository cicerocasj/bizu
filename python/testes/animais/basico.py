import unittest

class TesteAnimais(unittest.TestCase):

    def teste_soma(self):
        self.assertEqual(1+1, 2)

if __name__ == '__main__':
    unittest.main()

"""
Obs:
__init__.py tem 
from animais import *
linha de comando:
python -m unittest animais
python -m unittest animais.TesteAnimais
python -m unittest animais.TesteAnimais.teste_soma
"""
