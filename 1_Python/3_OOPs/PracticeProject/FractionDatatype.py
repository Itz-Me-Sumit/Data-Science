import math

class Fraction:
    def __init__(self, n=0, d=1):
        self.n = n
        self.d = d
        self._simplify()

    def _simplify(self):
        gcd = math.gcd(self.n, self.d)
        self.n //= gcd
        self.d //= gcd

    def __str__(self):
        return f"{self.n}/{self.d}"

    def _parse(self, frac):
        if isinstance(frac, str):
            n, d = map(int, frac.strip().split('/'))
            return n, d
        elif isinstance(frac, Fraction):
            return frac.n, frac.d
        else:
            raise ValueError("Invalid input")

    def add(self, *args):
        num = 0
        den = 1

        for frac in args:
            n, d = self._parse(frac)
            num = num * d + n * den
            den = den * d

        return Fraction(num, den)

    def multiply(self, *args):
        num = 1
        den = 1

        for frac in args:
            n, d = self._parse(frac)
            num *= n
            den *= d

        return Fraction(num, den)

    def __add__(self, other):
        n, d = self._parse(other)
        num = self.n * d + n * self.d
        den = self.d * d
        return Fraction(num, den)

    def __mul__(self, other):
        n, d = self._parse(other)
        return Fraction(self.n * n, self.d * d)