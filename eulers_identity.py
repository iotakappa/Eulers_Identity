#!/usr/local/bin/python3
# coding: utf-8
def factorial(n): return 1 if n == 0 else n * factorial(n-1)
def exp(n): return sum(n**x / factorial(x) for x in range(0, 100))
def pi() : return 4 * sum((-1)**n / (2*n+1) for n in range(0, 1000000))
r = exp(1j * pi())
print('({0}+{1}j)'.format(round(r.real,5),round(r.imag,5)))


