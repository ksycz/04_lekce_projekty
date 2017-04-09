import math
import random
for cislo in range(0,99):
    if cislo%3==0 and not cislo%5==0:
        print('bum')
    elif cislo%5==0 and not cislo%3==0:
        print('bac')
    elif cislo%3==0 and cislo%5==0:
        print('bum-bac')
