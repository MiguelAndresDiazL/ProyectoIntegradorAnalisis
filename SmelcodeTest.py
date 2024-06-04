# Ejemplo de código Python Smellcode

# Variable global
some_var = 42

# TODO: Refactor this function
def long_function_with_many_parameters(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
    # Función larga
    global some_var
    x = 10  # Variable con nombre poco descriptivo
    y = 20  # Variable con nombre poco descriptivo
    result = 0
    for i in range(x):
        for j in range(y):
            result += i * j

    if arg1:
        print("Argument 1 is True")
    elif arg2:
        print("Argument 2 is True")
    elif arg3:
        print("Argument 3 is True")
    # Código duplicado
    elif arg4:
        print("Argument 4 is True")
    elif arg5:
        print("Argument 5 is True")
    elif arg6:
        print("Argument 6 is True")
    elif arg7:
        print("Argument 7 is True")
    elif arg8:
        print("Argument 8 is True")
    elif arg9:
        print("Argument 9 is True")
    elif arg10:
        print("Argument 10 is True")
    else:
        print("No arguments are True")

    # Código comentado
    # print("This line is commented out")

    some_var += result
    return some_var

# Función que repite código
def another_function():
    # TODO: Refactor this function
    global some_var
    x = 10  # Variable con nombre poco descriptivo
    y = 20  # Variable con nombre poco descriptivo
    result = 0
    for i in range(x):
        for j in range(y):
            result += i * j

    print("Result is:", result)
    some_var += result
    return some_var

# Llamada a las funciones
if __name__ == "__main__":
    long_function_with_many_parameters(True, False, False, False, False, False, False, False, False, False)
    another_function()
