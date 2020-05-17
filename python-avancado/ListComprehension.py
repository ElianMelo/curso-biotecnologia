# -*- coding: utf-8 -*-

# Utilizando for
x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2)

print("Utilizando for")
print(x)
print(y)
print()

# Utilizando list comprehension
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if i % 2 != 0]
print("Utilizando list comprehension")
print(x)
print(y)
print(z)
print()


