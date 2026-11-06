import unittest
def add(a, b):
    return a + b

class teste(unittest.TestCase):
    def test_add_num_positivo(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_num_negativo(self):
        self.assertEqual(add(-4, -8), -12)

if __name__ == "__main__":
    import unittest
    unittest.main()
    print()
