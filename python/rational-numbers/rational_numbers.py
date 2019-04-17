from __future__ import division

from math import gcd


class Rational(object):
    def __init__(self, numer, denom):
        if denom is None or denom == 0:
            raise ValueError("Invalid denominator!")
        self.numer = numer // gcd(numer, denom) if denom > 0 else (numer * -1) // gcd(numer, denom)
        self.denom = denom // gcd(numer, denom) if denom > 0 else (denom * -1) // gcd(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(
            (self.numer * other.denom + other.numer * self.denom),
            (self.denom * other.denom))

    def __sub__(self, other):
        return Rational(
            (self.numer * other.denom - other.numer * self.denom),
            (self.denom * other.denom))

    def __mul__(self, other):
        return Rational(
            (self.numer * other.numer),
            (self.denom * other.denom))

    def __truediv__(self, other):
        return Rational(
            (self.numer * other.denom),
            (self.denom * other.numer))

    def __abs__(self):
        return Rational(
            abs(self.numer),
            abs(self.denom))

    def __pow__(self, power):
        return Rational(
            self.numer ** power if power >= 0 else self.denom ** abs(power),
            self.denom ** power if power >= 0 else self.numer ** abs(power))

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
