# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 22:10:28 2019

@author: hakan
"""

def sumPrimes(input):
    sum = 0
    for number in range(0,input+1):
        if number > 1:
            for i in range(2,number):
                if (number % i) == 0:
                    break
            else:
                sum += number
    print(sum)

sumPrimes(15)