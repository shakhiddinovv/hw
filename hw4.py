num = int(input('Enter the number: '))
while True:
    if num % 2 == 1:
        num = int(input('Enter the number: '))
    else: break

while True:
    num = int(input('Enter the number: '))
    try:
        if num % 2 == 0: break
        else: raise ValueError
    except ValueError as ve:
        print(ve)