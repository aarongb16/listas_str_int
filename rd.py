# numeros = [1, 2, 4, 19, 5, 8, 6]
# for n in numeros:
#     if n == 3:
#         break
# else:
#     print('No se encontró el número 3')

numeros = input('ingrese unos numeros: ')

numbers  = numeros.split(',')

numbers = list(map(lambda x: int(x), numbers))


for n in numbers:
     if n == 3:
        print("encontre el tres")
        break
else:
    print('No se encontró el número 3')
    print(max(numbers))
