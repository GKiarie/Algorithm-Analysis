#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:14:34 2021

@author: isaacgitau
"""
def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    """Class Fraction"""
    
    def __init__(self, top, bottom):
        """Constructor definition"""
        self.num = top
        self.den = bottom
        common = gcd(new_num, new_den)
        
        
        
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den
        
    def show(self):
        print(f"{self.num}/{self.den}")
        
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        
        return first_num == second_num
    
    def __lt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        
        return first_num < second_num
    
    def __gt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        
        return first_num > second_num
    
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)
    
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)





f1 = Fraction(1,4)
f2 = Fraction(1,2)

print(f1.get_den())
print(f1.get_num())

print(f1 == f2)
