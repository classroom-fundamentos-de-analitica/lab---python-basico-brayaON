"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from functools import reduce
from collections import Counter, defaultdict

file = open('./data.csv', 'r').readlines()
file = [ line.replace('\n', '').split('\t') for line in file ]
# print(file)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    L = [ int(row[1]) for row in file ]
    ans = reduce(lambda x1, x2 : x1 + x2, L)

    return ans

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    L = [ row[0] for row in file ]
    cnt = Counter(L)

    ans = sorted(list(cnt.items()))
    return ans


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    L = [ (row[0], int(row[1])) for row in file ]
    d = {}
    for k, v in L:
        d.setdefault(k, 0)
        d[k] += v
    
    ans = sorted(list(d.items()))
    return ans;


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    L = [ row[2].split('-')[1] for row in file ]
    cnt = Counter(L)

    ans = sorted(list(cnt.items()))
    return ans;



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    L = [ (row[0], int(row[1])) for row in file ]
    d = {}
    for k, v in L:
        d.setdefault(k, []).append(v)

    ans = sorted([ (k, max(v), min(v)) for k, v in d.items() ])
    return ans


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    L = [ row[4].split(',') for row in file ]
    L = [ (x.split(':')[0], int(x.split(':')[1])) for l in L for x in l ]

    d = {}
    for k, v in L:
        d.setdefault(k, []).append(v)

    ans = sorted([ (k, min(v), max(v)) for k, v in d.items() ])
    return ans

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    L = [ (row[0], int(row[1])) for row in file ]
    d = {}
    for k, v in L:
        d.setdefault(v, []).append(k)

    ans = sorted(list(d.items()))
    return ans


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    L = [ (row[0], int(row[1])) for row in file ]
    d = {}
    for k, v in L:
        d.setdefault(v, [])
        if k not in d[v]:
            d[v].append(k)

    ans = sorted(list(d.items()))
    return ans


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    L = [ row[4].split(',') for row in file ]
    L = [ v.split(':')[0] for row in L for v in row ]
   
    ans = Counter(L)
    ans = dict(sorted(ans.items()))
    return ans


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    L = [ (row[0], len(row[3].split(',')), len(row[4].split(','))) for row in file ]
    return L


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    L = [ (int(row[1]), row[3].split(',')) for row in file ]

    d = {}
    for k, v in L:
        for x in v:
            d.setdefault(x, 0)
            d[x] += k
    
    ans = dict(sorted(d.items()))
    return ans


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    L = [ (row[0], row[4].split(',')) for row in file ]
    L = [ (row[0], int(d.split(':')[1])) for row in L for d in row[1] ]

    d = {}
    for k, v in L:
        d.setdefault(k,0)
        d[k] += v
    
    ans = dict(sorted(d.items()))
    return ans
