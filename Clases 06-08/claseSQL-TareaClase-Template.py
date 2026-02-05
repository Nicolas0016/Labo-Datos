# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase. 
Autor  : Pablo Turjanski
Fecha  : 2025-02-03
"""

# Importamos bibliotecas
import pandas as pd
import duckdb as dd

estasEnClases = True 
#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================
if(estasEnClases):
    carpeta = "~/Escritorio/Labo-Datos/Clases 06-08/"
else: 
    carpeta = "~/programacion/Labo-Datos/Clases 06-08/"
# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv(carpeta+"empleado.csv")
# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv(carpeta+"se_inscribe_en.csv")
materia       =pd.read_csv(carpeta+"materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
reserva    = pd.read_csv(carpeta+"reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv(carpeta+"examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv(carpeta+"examen03.csv")



#%%===========================================================================
# Ejemplo inicial
#=============================================================================

print(empleado)

consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()



#%%===========================================================================
# Ejercicios AR-PROJECT <-> SELECT
#=============================================================================
# a.- Listar DNI y Salario de empleados 
consultaSQL = """
                SELECT DISTINCT DNI, Salario
                FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado

#%%-----------
# b.- Listar Sexo de empleados 
consultaSQL = """
                SELECT DISTINCT Sexo 
                FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado


#%%-----------
#c.- Listar Sexo de empleados (sin DISTINCT)
consultaSQL = """
                SELECT Sexo 
                FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado

#%%===========================================================================
# Ejercicios AR-SELECT <-> WHERE
#=============================================================================
# a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino
consultaSQL = """
                SELECT DISTINCT *
                FROM empleado
                WHERE Sexo = 'F';
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado
#%% -----------
#b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000
consultaSQL = """
                SELECT DISTINCT *
                FROM empleado
                WHERE Sexo = 'F' AND Salario >15000;
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado

#%%===========================================================================
# Ejercicios AR-RENAME <-> AS
#=============================================================================
#a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso
consultaSQL = """
                SELECT DISTINCT 
                DNI AS id,
                Salario AS Ingreso
                from empleado
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 01
#=============================================================================
# Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres
consultaSQL = """
                SELECT Codigo, Nombre From aeropuerto
                WHERE Ciudad = 'Londres'
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado

#%% -----------
# Ejercicio 01.2.- ¿Qué retorna 
#                       SELECT DISTINCT Ciudad AS City 
#                       FROM aeropuerto 
#                       WHERE Codigo='ORY' OR Codigo='CDG'; ?
consultaSQL = """
                SELECT DISTINCT Ciudad AS City 
                FROM aeropuerto 
                WHERE Codigo='ORY' OR Codigo='CDG'; 
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado

#%% -----------
# Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR
consultaSQL = """
                SELECT DISTINCT Numero
                FROM vuelo 
                WHERE Origen='CDG' AND Destino='LHR'; 
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado

#%% -----------
# Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
consultaSQL = """
                SELECT DISTINCT Numero
                FROM vuelo 
                WHERE 
                (Origen='CDG' AND Destino='LHR')
                OR
                (Origen='LHR'AND Destino='CDG' ); 
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado

#%% -----------
# Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200
consultaSQL = """
                SELECT Fecha
                FROM reserva
                WHERE Precio > 200

              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
#=============================================================================
# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT
#=============================================================================
# a1.- Listar a los alumnos que cursan BDs o TLENG

consultaSQL = """
                SELECT * FROM alumnosBD 
                UNION 
                SELECT * FROM alumnosTLeng
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado

#%% -----------
# a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)

consultaSQL = """
                SELECT * FROM alumnosBD 
             UNION ALL
                SELECT * FROM alumnosTLeng
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado


#%% -----------
# b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG

consultaSQL = """
                SELECT * FROM alumnosBD 
                INTERSECT 
                SELECT * FROM alumnosTLeng
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
#%% -----------
# c.- Listar a los alumnos que cursan BDs y no cursan TLENG 

consultaSQL = """
                SELECT * FROM alumnosBD 
                EXCEPT 
                SELECT * FROM alumnosTLeng
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#=============================================================================
#  EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 02
#=============================================================================
# Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)
consultaSQL = """
                SELECT Numero 
                FROM vuelo
            INTERSECT
                SElECT NroVuelo 
                FROM reserva
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado
#%%-----------
# Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas
consultaSQL = """
                SELECT Numero 
                FROM vuelo
            EXCEPT
                SELECT NroVuelo 
                FROM reserva
              """

dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado
#%%-----------
# Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos
consultaSQL = """
                SELECT Origen FROM vuelo
                UNION
                SELECT Destino FROM vuelo
              """
              
dataframeResultado = dd.sql(consultaSQL).df()
dataframeResultado



#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#=============================================================================
# Ejercicios AR-... JOIN <-> ... JOIN
#=============================================================================
# a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades

consultaSQL = """
                SELECT DISTINCT * 
                FROM persona
            CROSS JOIN 
                nacionalidades
             """


dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)

consultaSQL = """
                SELECT DISTINCT * 
                FROM persona, nacionalidades
             """
dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%
# Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
# ----------------------------------------------------------------------------------------------
persona        = pd.read_csv(carpeta+"persona_ejemplosJoin.csv")
# ----------------------------------------------------------------------------------------------
# b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN

consultaSQL = """
                SELECT DISTINCT * 
                FROM persona
            INNER JOIN 
                nacionalidades
                ON Nacionalidad = IDN
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)

consultaSQL = """
                SELECT DISTINCT * 
                FROM persona,nacionalidades
                WHERE Nacionalidad=IDN
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
#%%-----------
# c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN

consultaSQL = """
                SELECT DISTINCT * 
                FROM persona
                
            LEFT OUTER JOIN 
            
                nacionalidades
                ON Nacionalidad = IDN
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado 
#%%===========================================================================
# Ejercicios SQL - ¿Mismos Nombres?
#=============================================================================
# a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia

consultaSQL = """
                SELECT DISTINCT LU, nombre
                FROM se_inscribe_en
                
                INNER JOIN materia
                ON materia.codigo_materia = se_inscribe_en.codigo_materia
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
    
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 03
#=============================================================================
# Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165

consultaSQL = """
                SELECT numero, ciudad 
                FROM vuelo
            INNER JOIN aeropuerto
                ON vuelo.Origen = Aeropuerto.codigo
                WHERE vuelo.numero = 165
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
#%%-----------
# Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200

consultaSQL = """
                SELECT nombre
                FROM reserva
            INNER JOIN pasajero 
                ON pasajero.DNI = reserva.dni
                WHERE reserva.precio>200
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
#%%-----------
# Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid

vuelosAMadrid = dd.query("""
                SELECT numero, vuelo.destino
                FROM aeropuerto
            INNER JOIN vuelo
                ON vuelo.origen = aeropuerto.codigo
                WHERE vuelo.origen = 'MAD'
              """).df()
              
dniPersonasDesdeMadrid = dd.query("""
                SELECT dni, fecha, vuelosAMadrid.destino
                FROM reserva
            INNER JOIN vuelosAMadrid
                ON vuelosAMadrid.numero = reserva.NroVuelo
                
              """).df()
              
consultaSQL = """
                SELECT Nombre, Fecha, Destino
                FROM dniPersonasDesdeMadrid
            INNER JOIN pasajero
                ON pasajero.dni = dniPersonasDesdeMadrid.dni
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
#%%===========================================================================
# Ejercicios SQL - Join de varias tablas en simultáneo
#=============================================================================
# a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero.
    
consultaSQL = """
                 SELECT DISTINCT r.Fecha, v.Salida, p.Nombre
                 FROM reserva AS r, pasajero AS p, vuelo as v
                 WHERE r.DNI = p.DNI AND r.NroVuelo = v.numero
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
    
#%%===========================================================================
# Ejercicios SQL - Tuplas espúreas
#=============================================================================
# a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto
    
consultaSQL = """
                SELECT DISTINCT empleado, e.rol, proyecto
                FROM empleadoRol e
            INNER JOIN rolProyecto r
                ON e.rol = r.rol
             """
tupla_espurea = '4    Bruno    Diseñador/a      YPF'
# EVItas que aparezcan tupla espurea si usas superclave de alguna de las dos tablas.
# rol no es superclave.
dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%===========================================================================
# Ejercicios SQL - Funciones de agregación
#=============================================================================
# a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)
    
consultaSQL = """

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia
    
consultaSQL = """
                SELECT instancia, count(*) AS asistieron from examen
                GROUP BY instancia
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)

consultaSQL = """
                 SELECT instancia, count(*) AS asistieron from examen
                 GROUP BY instancia
                 ORDER BY instancia ASC;
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes
    
consultaSQL = """
                SELECT instancia, count(*) AS asistieron from examen
                GROUP BY instancia
                HAVING asistieron < 4 -- having se usa para conjuntos 
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
#%%-----------
# c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen
    
consultaSQL = """
             SELECT instancia, AVG(edad) as promedio FROM examen
             GROUP BY instancia
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
#%%===========================================================================
# Ejercicios SQL - LIKE")
#=============================================================================
# a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial.
    
consultaSQL = """
                SELECT instanica, AVG(nota) as promedio 
                FROM examen
                WHERE instancia='parcial-01' OR instancia = 'parcial-02'
                GROUP BY instancia
             """

dataframeResultado = dd.query(consultaSQL).df()

#%%-----------
# a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE.
    
consultaSQL = """
                SELECT instancia, AVG(nota) as promedio 
                FROM examen
                GROUP BY instancia
                HAVING instancia LIKE 'Parcial-%'
                ORDER BY instancia ASC
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%===========================================================================
# Ejercicios SQL - Eligiendo
#=============================================================================
# a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4).
    
consultaSQL = """
                SELECT Nombre, Nota, 
                    CASE WHEN Nota >=4
                        THEN 'Aprobo'
                        ELSE 'Desaprobo'
                    END AS Estado,
                    'revisado-por-mi' as revision
                    
                FROM examen
                
                WHERE instancia = 'Parcial-01'
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia.
    
consultaSQL = """
                SELECT instancia, 
                    CASE WHEN Nota >=4
                        THEN 'Aprobo'
                        ELSE 'Desaprobo'
                    END AS Estado,
                    COUNT(*) AS Cantidad
                    
                FROM examen
                
                GROUP BY Instancia, Estado -- Junta por la superclave instancia-estadot
                ORDER BY Instancia, Estado -- QUE LOCO
              """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%===========================================================================
# Ejercicios SQL - Subqueries
#=============================================================================
#a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia

consultaSQL = """
                SELECT nombre, instancia, nota
                
                FROM examen as e1
                
                WHERE e1.Nota > (                   -- por cada tupla hace un select nuevo y 
                    SELECT AVG(e2.nota)             -- ve cuando las instancias coinciden
                    FROM  examen AS e2
                    WHERE e2.instancia = e1.instancia 
                    )
                ORDER BY instancia,nombre, nota
                --<> distinto
             """


dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia

consultaSQL = """
                SELECT e1.nombre, e1.instancia, e1.nota
                FROM examen as e1
                WHERE e1.Nota = (                   
                    SELECT max(e2.nota)            
                    FROM  examen AS e2
                    WHERE e2.instancia = e1.instancia 
                )
             """
consultaSQL = """
                SELECT e1.nombre, e1.instancia, e1.nota
                FROM examen as e1
                WHERE e1.Nota >= ALL(  -- Multiple row                
                    SELECT e2.nota     -- IN, ANY, ALL, Exist       
                    FROM  examen AS e2
                    WHERE e2.instancia = e1.instancia 
                )
             """
dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado 

#%%-----------
# c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio
consultaSQL = """
                SELECT e1.nombre, e1.instancia, e1.nota
                FROM examen as e1
                WHERE e1.NOMBRE NOT ALL( -- NOT EXIST                   
                    SELECT e2.nombre            
                    FROM  examen AS e2
                    WHERE e2.instancia LIKE 'Recuperatorio-%'
                )
                ORDER BY nombre ASC, Nota DESC
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%===========================================================================
# Ejercicios SQL - Integrando variables de Python
#=============================================================================
# a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota

umbralNota = 7

consultaSQL = """
                SELECT nombre, intancia, nota
                FROM examen
                WHERE examen.nota > 
              """ + str(umbralNota)

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%===========================================================================
# Ejercicios SQL - Manejo de NULLs
#=============================================================================
# a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9

consultaSQL = """
                SELECT * FROM examen03
                WHERE nota < 9
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
#%%-----------
# b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9

consultaSQL = """
                SELECT * FROM examen03
                WHERE nota >= 9
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9

consultaSQL = """
                SELECT * FROM examen03
                WHERE nota < 9 OR nota >=9 -- OJO 
              """


dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# d1.- Obtener el promedio de notas

consultaSQL = """
             SELECT AVG(Nota)
             from examen03   
             """


dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%-----------
# d2.- Obtener el promedio de notas (tomando a NULL==0)

consultaSQL = """
                SELECT AVG(
                    CASE WHEN Nota IS Null
                    THEN 0
                    ELSE Nota End
                    ) as promedio  -- Siempre es recomendable dejar la base de datos intacta
                from examen03  
              """


dataframeResultado = dd.query(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Mayúsculas/Minúsculas
#=============================================================================
# a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula

consultaSQL = """
                SELECT empleado, UPPER(rol) AS rol
                from empleadoRol
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado
#%%-----------
# b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula

consultaSQL = """
                SELECT empleado, LOWER(rol) AS rol
                from empleadoRol
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado



#%%===========================================================================
# Ejercicios SQL - Reemplazos
#=============================================================================
# a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni

consultaSQL = """
                SELECT Empleado, REPLACE(rol, 'ñ', 'ni') as Rol
                FROM empleadoRol
             """

dataframeResultado = dd.query(consultaSQL).df()
dataframeResultado

#%%===========================================================================
# Ejercicios SQL - Desafío
#=============================================================================
# a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02

# ... Paso 1: Obtenemos los datos de los estudiantes
df_estudiantes = dd.query("""
                SELECT Nombre
                FROM examen
             """).df()
             

cosasquequiero = ['Parcial-01','Parcial-02', 'Recuperatorio-01','Recuperatorio-02']

notaParcial01 = dd.query('''
    SELECT DISTINCT examen.nombre,sexo, edad, nota as NotaParcial01
    FROM df_estudiantes
    LEFT OUTER JOIN examen
    ON examen.nombre = df_estudiantes.nombre AND examen.instancia = 'Parcial-01'
''').df()
notaParcial01
notaParcial02 = dd.query('''
    SELECT DISTINCT 
        notaParcial01.nombre,
        notaParcial01.sexo,
        notaParcial01.edad,
        notaParcial01.NotaParcial01, 
        examen.nota as NotaParcial02
    FROM notaParcial01
    LEFT OUTER JOIN examen
    ON examen.nombre = notaParcial01.nombre AND examen.instancia = 'Parcial-02'
''').df()
notaParcial02

notaRecuperatorio01 = dd.query('''
    SELECT DISTINCT 
        notaParcial02.nombre,
        notaParcial02.sexo,
        notaParcial02.edad,
        notaParcial02.NotaParcial01, 
        notaParcial02.NotaParcial02,
        examen.nota as notaRecuperatorio01
    FROM notaParcial02
    LEFT OUTER JOIN examen
    ON examen.nombre = notaParcial02.nombre AND examen.instancia = 'Recuperatorio-01'
''').df()

notaRecuperatorio02 = dd.query('''
    SELECT DISTINCT 
        notaRecuperatorio01.nombre,
        notaRecuperatorio01.sexo,
        notaRecuperatorio01.edad,
        notaRecuperatorio01.NotaParcial01, 
        notaRecuperatorio01.NotaParcial02,
        notaRecuperatorio01.NotaRecuperatorio01,
        examen.nota as notaRecuperatorio02
    FROM notaRecuperatorio01
    LEFT OUTER JOIN examen
    ON examen.nombre = notaRecuperatorio01.nombre AND examen.instancia = 'Recuperatorio-02'
''').df()
resultado = notaRecuperatorio02
#%% -----------
# b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4.

consultaSQL = """
            SELECT *,
            CASE WHEN (
                (NotaParcial01 >=4 OR notaRecuperatorio01>=4) AND 
                (NotaParcial02 >=4 OR notaRecuperatorio02>= 4))
                THEN 'Aprobo'
                ELSE 'Desaprobo'
            END AS Estado
            FROM notaRecuperatorio02
             """

desafio_02 = dd.query(consultaSQL).df()
resultado2 = desafio_02

#%% -----------
# c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior.

consultaSQL = """
            SELECT nombre, 
                sexo, 
                edad, 
                'Parcial-01' AS Instancia,
                NotaParcial01 as Nota
            FROM desafio_02
            """
aux_01 = dd.query(consultaSQL).df()
consulta2 ="""
            SELECT nombre, 
                sexo, 
                edad, 
                'Parcial-02' AS Instancia,
                NotaParcial02 as Nota
            FROM desafio_02
            WHERE Nota IS NOT Null
            """

aux_02 = dd.query(consulta2).df()
consulta3 ="""
            SELECT nombre, 
                sexo, 
                edad, 
                'Recuperatorio-01' AS Instancia,
                NotaRecuperatorio01 as Nota
            FROM desafio_02
            WHERE Nota IS NOT Null
            """

aux_03 = dd.query(consulta3).df()
consulta4 ="""
            SELECT nombre, 
                sexo, 
                edad, 
                'Recuperatorio-02' AS Instancia,
                NotaRecuperatorio02 as Nota
            FROM desafio_02
            WHERE Nota IS NOT Null
            """
aux_04 = dd.query(consulta4).df()


consulta5 = """
            SELECT * FROM aux_01
            UNION
            SELECT * FROM aux_02
            UNION
            SELECT * FROM aux_03
            UNION
            SELECT * FROM aux_04
"""

aux_05 = dd.query(consulta5).df()
aux_05























