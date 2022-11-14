import unittest


from complex import Complex


class TestComplex(unittest.TestCase):

    def test_equal(self):
        first = Complex(2, 5)
        second = Complex(2, 5)
        self.assertEqual(first, second)
        self.assertTrue(first.__eq__(second))

    def test_sum(self):
        first = Complex(2, 4)
        second = Complex(1, -3)
        self.assertEqual(first + second, Complex(3, 1))

    def test_sub(self):
        first = Complex(2, 4)
        second = Complex(1, -3)
        self.assertEqual(first - second, Complex(1, 7))

    def test_mul(self):
        first = Complex(1, 3)
        second = Complex(2, -2)
        self.assertEqual(first * second, Complex(8, 4))

    def test_mul_by_num(self):
        first = Complex(1, 2)
        num = 5
        self.assertEqual(first.multiply_by_num(num), Complex(5, 10))

    def test_abs(self):
        num = Complex(6, -8)
        self.assertEqual(abs(num), 10)

    def test_complex_conj(self):
        num = Complex(20, 21)
        self.assertEqual(num.complex_conjugate(), Complex(20, -21))

    def test_str(self):
        num1 = Complex(2, -1)
        num2 = Complex(0, 1)
        num3 = Complex(5, 0)
        self.assertEqual(str(num1), '2-1i')
        self.assertEqual(str(num2), '1i')
        self.assertEqual(str(num3), '5')

if __name__ == '__main__':
    unittest.main()
