class Complex:

    def __init__(self, re, im):
        self.re = re
        self.im = im


    def __add__(self, x2):
        re_sum = self.re + x2.re
        im_sum = self.im + x2.im
        return Complex(re_sum, im_sum)


    def __mul__(self, x2):
        re_mul = self.re * x2.re - self.im * x2.im
        im_mul = self.re * x2.im + x2.re * self.im
        return Complex(re_mul, im_mul)


    def __sub__(self, x2):
        re_sub = self.re - x2.re
        im_sub = self.im - x2.im
        return Complex(re_sub, im_sub)

    def multiply_by_num(self, num):
        re_mul = self.re * num
        re_im = self.im * num
        return Complex(re_mul, re_im)

    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def __eq__(self, other):
        return (self.re == other.re) and (self.im == other.im)

    def complex_conjugate(self):
        con_im = self.im * (-1)
        return Complex(self.re, con_im)

    def __str__(self):
        if self.re == 0 and self.im == 0:
            return 0
        if self.re == 0 and self.im != 0:
            return '{}i'.format(self.im)

        if self.re != 0:
            if self.im > 0:
                return '{}+{}i'.format(self.re, self.im)
            if self.im == 0:
                return str(self.re)
            if self.im < 0:
                return '{}{}i'.format(self.re, self.im)

