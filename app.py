# python

from utils import find_max
try:
    list = input('>input the numbers: ').split(' ')
    print(f'maximmum: {find_max(list)}')
except  ValueError:
    print('invalid vlues !')

from mammal import mammal
class Dog(mammal):
    pass
dog1 = Dog('floyd')
dog1.walk()
