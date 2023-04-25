import unittest
from CambioDeNumeracion import decimal2binario
from CambioDeNumeracion import decimal2hexadecimal
from CambioDeNumeracion import decimal2octal
from CambioDeNumeracion import binario2decimal
from CambioDeNumeracion import octal2decimal
from CambioDeNumeracion import hexa2decimal
from CambioDeNumeracion import binario2octal
from CambioDeNumeracion import binario2hexa
from CambioDeNumeracion import octal2binario
from CambioDeNumeracion import octal2hexa
from CambioDeNumeracion import hexa2binario
from CambioDeNumeracion import hexa2octal
class TestNumeracion(unittest.TestCase):
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal('01011100'), 96)
    def test_decimal2binario(self):
        self.assertEqual(decimal2binario(97), '01100001')
    def test_decimal2hexadecimal(self):
        self.assertEqual(decimal2hexadecimal(249), 'F9')
    def test_decimal2octal(self):
        self.assertEqual(decimal2octal(98), 142)
    def test_octal2decimal(self):
        self.assertEqual(octal2decimal(143), 99)
    def test_hexa2decimal(self):
        self.assertEqual(hexa2decimal('FA'), 250)
    def test_binario2octal(self):
        self.assertEqual(binario2octal('00010111011'), 273)
    def test_binario2hexa(self):
        self.assertEqual(binario2hexa('00010111011'), 'BB')
    def test_octal2binario(self):
        self.assertEqual(octal2binario(100), ' 1000000 ')
    def test_octal2hexa(self):
        self.assertEqual(octal2hexa(100), 40)
    def test_hexa2binario(self):
        self.assertEqual(hexa2binario(101), '100000001')
    def test_hexa2octal(self):
        self.assertEqual(hexa2octal(101), 401)
if __name__ =="__main__":
    unittest.main