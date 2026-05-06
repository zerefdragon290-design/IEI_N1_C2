# Esto es una operación aritmética sencilla
# print(4 + 5)
# a = float(input('Ingrese el primer número: '))
# b = float(input('Ingrese el segundo número: '))
# print(a + b)

# Realizamos la misma operación creando un método
# Para crear un método usamos la palabra reservada DEF (definir)
# Luego ponemos el nombre del método
# Finalmente definimos los argumentos del métodos, es decir, 
# los insumos que necesitará la función para trabajar
print('\nOperaciones aritméticas con 2 números mediante métodos')
def suma(a,b):
    try:
        resultado = a + b
        return resultado
    except Exception as error:
        print(f'No se puede realizar la operación, por el siguiente error: {error}')

def resta(a,b):
    try:
        resultado = a - b
        return resultado
    except Exception as error:
        print(f'No se puede realizar la operación, por el siguiente error: {error}')

def multiplicacion(a,b):
    try:
        resultado = a * b
        return resultado
    except Exception as error:
        print(f'No se puede realizar la operación, por el siguiente error: {error}')

def division(a,b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print('No se puede dividir por 0.')
    except Exception as error:
        print(f'No se puede dividir por el siguiente error: {error}')

def convertir_float(valor):
    try:
        num_decimal = float(valor)
        return num_decimal
    except ValueError: 
            print('No se puede convertir el valor ingresado a decimal')
    except Exception as error:
        print(f'No se puede realizar la conversión por el siguiente error: {error}')

def solicitar_datos():
    numero1 = convertir_float(input('Ingrese el primer número: '))
    numero2 = convertir_float(input('Ingrese el segundo número: '))
    return(numero1,numero2)

ciclo = True
print('Mi Primera Súper Calculadora en Python!!')
print('========================================')

while ciclo == True:
    print()
    print('[1] Suma')
    print('[2] Resta')
    print('[3] Multiplicación')
    print('[4] División')
    print('[0] Salir')

    opcion = input('Seleccione su opción [0-4]: ')
    opciones_validas = ['0','1','2','3','4']
    if opcion in opciones_validas:
        if opcion == '0':
            print('Gracias por usar la calculadora, vuelva pronto!')
            ciclo = False
        elif opcion == '1':
            num1,num2 = solicitar_datos()
            resultado = suma(num1,num2)
            print(f'El resultado de la suma es: {resultado}')
        elif opcion == '2':
            num1,num2 = solicitar_datos()
            resultado = resta(num1,num2)
            print(f'El resultado de la resta es: {resultado}')
        elif opcion == '3':
            num1,num2 = solicitar_datos()
            resultado = multiplicacion(num1,num2)
            print(f'El resultado de la multiplicación es: {resultado}')
        elif opcion == '4':
            num1,num2 = solicitar_datos()
            resultado = division(num1,num2)
            print(f'El resultado de la división es: {resultado}')
    else:
        print('Opción NO corresponde, ingrese nuevamente...')