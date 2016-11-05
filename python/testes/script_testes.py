import script as p
import unittest


class TesteScript(unittest.TestCase):
    def teste_soma(self):
        self.assertEquals(p.soma(1,2), 3)



if __name__ == "__main__":
    unittest.main(verbosity=2)
