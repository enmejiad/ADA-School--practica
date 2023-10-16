#
#? Punto 3: Define una variable de cada tipo de primitivo

Nombre = "Esdras Mejia" # Tipo String (Texto)
print(f"La variable Nombre de tipo {type(Nombre)} \n")

print(f"Bienvenido, {Nombre}, esto es una prueba.\n") #uso del format (f)

Edad = 40 # Tipo int
print(f"La variable Edad de tipo {type(Edad)}")

Estatura  = 1.70 # tipo Float
print(f"La variable Estatura de tipo {type(Estatura)}")

Is_Honduras = True  # Tipo Boolean (True o False)
print(f"La variable 'Is_Colombian' de tipo {type(Is_Colombian)}")


#? Punto 3.1: Concatena a la cadena las otras variables aplicando la conversión 
#? correcta para funcionar, guarda el resultado en una variable

#! Estructura para definir una variable: nombre_varable = contenido_variable

Texto = Nombre + str(Edad) + str(Estatura) + str(Is_Colombian) #convertir a strig y concatenar

#? Punto 3.2: Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo

# El límite de los enteros en Python es sys.maxsize, que es 2^63 - 1 en una máquina de 64 bits
# El límite de los floats es aproximadamente 1.8e308
""" Bibliografia: 
    https://realpython.com/python-data-types/
    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
    """
    


#? Punto 3.3: Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable

    # Fórmula suma de los primeros n números pares
    # La fórmula es n*(n+1)

n = Edad 
sumatoria = n*(n+1)

#? Punto 3.4: Imprimir los resultados de las tareas anteriores


print(f"La cadena de texto concatenada es: '{Texto}'") #imprimir en consola la cadena de texto

print(f"La sumatoria de los primeros {n} numeros pares es igual a: {sumatoria}")
