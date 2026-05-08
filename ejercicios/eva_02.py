# Resuelva los siguientes ejercicios mediante funciones,
# las que serán llamadas dentro de un menú de opciones.

def solicitar_datos_personales():
    nombre = input('Ingrese su nombre: ')
    print('[H] Hombre')
    print('[M] Mujer')
    genero = input('Ingrese su Género, H para hombre o M para mujer: ')
    return nombre,genero

def solicitar_datos_cilindro():
    radio = float(input('Ingrese el radio del cilindro: '))
    altura = float(input('Ingrese la altura del cilindro: '))
    return radio, altura
    pass

def solicitar_numero():
    numero = int(input('Ingrese un número entero: '))
    return numero

# 1.- Cree una función que entregue el saludo "Buen día!"
def saludo_cordial():
    saludo = "Buen día!"
    return saludo

# 2.- Cree una función que solicite el nombre y el género al usuario y luego, 
# llamando a la función anterior, salude al usuario, el saludo debe quedar así: 
# "Buen día nombre_usuario!", 
# y agregue el texto "Hoy te ves hermosa" si el usuario es mujer 
# o "cómo estás campeón?" si el usuario es hombre
def saludo_personal(nombre,genero):
    saludo = saludo_cordial()
    mensaje = ""
    saludo = saludo.replace("!", "")
    saludo_split = saludo.split("!")
    if genero == 'M':
        return f"{saludo[:-1]} {nombre}! Hoy te ves hermosa."
    elif genero == 'H':
        return f"{saludo[:-1]} {nombre}! Cómo estás campeón?"
    else:
        return f"genero invalido, ingrese nuevamente."
    return mensaje

# 3.- Cree una función que permita calcular el área de una circunferencia 
# y otra que permita calcular el volumen de un cilindro usando la función anterior
# los datos deben ser ingresados por el usuario
def area_circunferencia(radio):
    # area = Pi * r**2
    area = math.pi * radio ** 2
    return area

def volumen_cilindro(radio, altura):
    # volumen = area * altura
    area = area_circunferencia(radio)
    volumen = area * altura
    return f"El volumen del cilindro es: {volumen:.2f}"
# 4.- Cree una función que pida un número entero al usuario 
# y calcule el factorial de ese número
def factorial(numero):
    # !5 = 1*2*3*4*5
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)

def menu_principal():
    while True:        
        print()
        print('[1] Saludo')
        print('[2] Saludo Personal')
        print('[3] Volumen Cilindro')
        print('[4] Calcular Factorial')
        print('[0] Salir')
        opcion = input('Seleccione su opción [0-4]: ')
        opciones_validas = ['0','1','2','3','4']

        if opcion in opciones_validas:
            if opcion != '0':
                if opcion == '1':
                    resultado = saludo_cordial()
                elif opcion == '2':
                    nombre,genero = solicitar_datos_personales()
                    resultado = saludo_personal(nombre,genero)
                elif opcion == '3':
                    radio, altura = solicitar_datos_cilindro()
                    resultado = volumen_cilindro(radio, altura)
                elif opcion == '4':
                    numero = solicitar_numero()
                    resultado = factorial(numero)
                print(f'\n{resultado}')
            else:
                print('Saliendo del sistema...')
        else:
            print('Opción NO corresponde, ingrese nuevamente...')

menu_principal()