"""
Son aquellos números que son iguales a la suma de sus divisores propios
(excluyendo el número mismo). Ejemplo: 6 (1 + 2 + 3 = 6), 28 (1 + 2 + 4 + 7 + 14 = 28).
Se espera que el interesado ingrese una serie de número enteros positivos mayores
que dos y después del ingreso de cada uno el programa indique si es un número
perfecto o no. Esta lista termina cuando el que introduce la lista digita un número
negativo

"""
def numero_perfecto(n):
    suma = 0
    for perfecto in range(1, n):
        if n % perfecto  == 0 :
            suma = suma + perfecto
    return suma == n



def lista():
    while True:
        n = int(input("ingrese un numero "))
        if n < 0:
            break
        if n <= 2:
            print("el numero debe ser mayor que dos")
        elif numero_perfecto(n):
            print(n,"es un numero perfecto")
        else:
            print(n,"no es un numero perfecto")


lista()
