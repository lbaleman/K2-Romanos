import unittest
from romanosClase import romano_a_arabigo, arabigo_a_romano

class RomanNumberTest(unittest.TestCase):
    def test_symbols_romas(self):
        self.assertEqual(romano_a_arabigo('I'),1)
        self.assertEqual(romano_a_arabigo('V'),5)
        self.assertEqual(romano_a_arabigo('X'),10)
        self.assertEqual(romano_a_arabigo('XIV'),14)
        self.assertEqual(romano_a_arabigo('XV'),15)
        self.assertEqual(romano_a_arabigo('XL'),40)
        self.assertEqual(romano_a_arabigo('L'),50)
        self.assertEqual(romano_a_arabigo('C'),100)
    
    def test_crecients_romas(self):
        self.assertEqual(romano_a_arabigo('III'),3)
        self.assertEqual(romano_a_arabigo('XVI'),16)
        self.assertEqual(romano_a_arabigo('XIV'),14)
        self.assertEqual(romano_a_arabigo('XXXX'),0)
        self.assertEqual(romano_a_arabigo('XLVII'),47)
        self.assertEqual(romano_a_arabigo('IIII'),0)
        self.assertEqual(romano_a_arabigo('LXXIII'),73)
        self.assertEqual(romano_a_arabigo('CMXCIX'),999)
        self.assertEqual(romano_a_arabigo('MIIX'),0)
        self.assertEqual(romano_a_arabigo('CLIX'),159)
        self.assertEqual(romano_a_arabigo('VC'),0)
        self.assertEqual(romano_a_arabigo('IC'),0)
        self.assertEqual(romano_a_arabigo('IX'),9)
        self.assertEqual(romano_a_arabigo('XC'),90)
        self.assertEqual(romano_a_arabigo('IL'),0)
        self.assertEqual(romano_a_arabigo('CM'),900)
        self.assertEqual(romano_a_arabigo('VV'),0)

if __name__=='__main__':
    unittest.main()
