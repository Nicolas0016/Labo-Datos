# se cuenta con el siguiente DER

# Empleado -> DNI, Edad, Cantidad de hijos y salario.

# [DNI, Edad, cantidad de hijos, salario]
empleado_01 = [
    [20222333, 45, 2, 20000],
    [33456234, 40, 0, 18000],
    [45432345, 41, 1, 10000]
]


def superan_umbral(empleados:list[list[int]], umbral:int):
    empleados_superan_umbral = []
    for empleado in empleados:
        if(empleado[3] > umbral):
            empleados_superan_umbral.append(empleado)
    return empleados_superan_umbral


otros_empleados01 = superan_umbral(empleado_01, 15000)

empleado_02 = [
    [20222333, 45, 2, 20000],
    [33456234, 40, 0, 18000],
    [45432345, 41, 1, 10000],
    [43967304, 37, 0, 12000],
    [42236276, 36, 0, 18000]
]

otros_empleados02 = superan_umbral(empleado_02, 15000)

# ¿Qué ocurre si cambiamos el orden de las columnas?

# [Salario, DNI, Edad, Hijos]

empleado_03 = [
    [20222333, 20000, 45, 2],
    [33456234, 18000, 40, 0],
    [45432345, 10000, 41, 1],
    [43967304, 12000, 37, 0],
    [42236276, 18000, 36, 0]
]

otros_empleados03 = superan_umbral(empleado_03, 15000)
print((otros_empleados02 == otros_empleados03) if 'las matiz es la esperada' else 'la matriz no es la esperada')

def superanSalarioActividad03(empleados:list[list[int]], umbral:int):
    resultado = []
    for empleado in empleados:
        salario = empleado[1]
        if(salario > umbral):
            resultado.append([empleado[0], empleado[2],empleado[3],empleado[1]])
    return resultado

otros_empleados03 = superanSalarioActividad03(empleado_03, 15000)
print((otros_empleados02 == otros_empleados03) if 'las matiz es la esperada' else 'la matriz no es la esperada')


empleado_04 = [
    [20222333,33456234,45432345,43967304, 42236276], #DNI
    [20000, 18000, 10000, 12000, 18000], #Salario
    [45, 40, 41, 37, 36],# Edad
    [2,0,1,0,0] #hijos
]

# Ninguna de las funciones anteriores funciona XD

def superanSalarioActividad04(empleados:list[list[int]], umbral:int):
    empleados_que_superan = [[],[],[],[]]
    for i in range(len(empleados[1])):
        salario = empleados[1][i]
        if(salario>umbral):
            empleados_que_superan[0].append(empleados[0][i])
            empleados_que_superan[1].append(empleados[1][i])
            empleados_que_superan[2].append(empleados[2][i])
            empleados_que_superan[3].append(empleados[3][i])
    return empleados_que_superan

otros_empleados04 = superanSalarioActividad04(empleado_04, 15000)

# Al agregar mas filas no cambio el funcionamiento del programa
# ya que al recorrer todas las celdas no tenemos inconsistencias con
# lo esperado y lo devuelto

# Al cambiar el orden de las columnas tuvimos problemas ya que dependiamos
# de ídices fijos

# También tuvimos problemas ya que necesitabamos devolverlo de otra manera
# y además la visualizacion de los datos cambio. Pero como ventaja solo necesitabamos ver
# una lista de datos.

# muchas ventajas
















