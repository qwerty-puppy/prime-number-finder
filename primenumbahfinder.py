number = 1
prime = 0
yayorney = 0
while True:
    number += 2
    if number % 101 == 0:
        yayorney = input("keep going? y/n")
        if yayorney == "n":
            break
    prime = 2 ** number - 1
    print(str(prime))
    print()

