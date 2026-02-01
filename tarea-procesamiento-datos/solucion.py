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
