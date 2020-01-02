number = 3
loop = 0
while True:
    primeorcomposite = 0
    number += 1

    if number % 2 == 1:
        loop = int((number+1)/2)
    if number % 2 == 0:
        number += 1

        loop = int(number/2)
    for x in range(2, loop):
        if number % x == 0:
            primeorcomposite += 1
    if primeorcomposite == 0:
        print(number)

