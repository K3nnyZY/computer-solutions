def taylor_series(x, a, n): 
    '''funcion en la cual calcula la serie de taylor
    tiene los siguentes parametors:
    x = punto que quiere evaluar
    a = punto donde hace la expansion
    n = los terminos que quieres de la serie'''
    series = [] # se crea una lista para guardar los valores
    for i in range(n): # un ciclo donde i es el termino inicial y n hasta el termino donde va a evaluar
        sum = (-1)**i * (x - a)**(i+1) / (i+1) # sumatoria que nos da la serie de taylor
        series.append(sum) # se añade los valores de cada iteracion en la lista
        
    return series # retorna la lista de valores guardada

x = float(input("punto que quiere calcular: "))  # punto para el cual se quiere calcular ln(x)
a = float(input("punto para la expansion: "))  # punto alrededor del cual se está haciendo la expansión
n = int(input("numero de terminos que quieres evaluar: "))  # número de términos en la serie

series = taylor_series(x, a, n) # se crea la serie
print("Serie de Taylor para ln(x):", series) # imprime la serie

j = int(input("posicion para mostrar de la serie: "))

if j <= len(series):
    print("valor de la posicion pedida es: ", series[j])
else:
    print("valor no valido intentelo de nuevo.")



