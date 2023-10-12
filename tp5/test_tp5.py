import pytest
from tp5_fun import *

@pytest.mark.parametrize("a, res",[

    (2, True),
    (7, True),
    (13, True),
])

def test_prime(a, res):
    assert prime(a)==res

@pytest.mark.parametrize("a,res",[
    (123, 6),
    (111, 3),
    (121, 4),
])

def test_primadd(a, res):
    assert primadd(a)==res

@pytest.mark.parametrize("a, b,res",[
    (1,11,2),
    (2,22,2),
    (3,3331,3),
])    

def test_busdig(a,b,res):
    assert busdig(a,b)==res

@pytest.mark.parametrize("a,res",[
    (3, 6),
    (4, 24),
    (5, 120),
])

def test_factorial(a, res):
    assert factorial(a)==res

@pytest.mark.parametrize("a, b",[
    (12345,False),
    (123456,False),
    (1234567,True),
    (123456,False),
    ("asserta",False),
])




def test_dni_number(a,b):
    assert dni_number(str(a)) == b

@pytest.mark.parametrize("a, b",[
    ("thomas the ghost","ghost"),
    ("gianfranco liguori","liguori"),
    ("me extraña araña","araña"),
])




def test_surname(a,b):
    assert surname(a) == b


@pytest.mark.parametrize("a, b",[
    ("thomas the ghost","thomas"),
    ("gianfranco liguori","gianfranco"),
    ("me extraña araña","me"),
])




def test_first_name(a,b):
    assert first_name(a) == b


@pytest.mark.parametrize("a, b",[
    (12345,345),
    (123456,456),
    (3434689,689),
    (99090990,990),
])




def test_last_three(a,b):
    assert last_three(str(a)) == str(b)

@pytest.mark.parametrize("a, res",[
    ((2, 4),4.47213595499958),
    ((3, 4),5.0),
    ((3, 4, 5),7.0710678118654755),
])
def test_modulo_vector(a, res):
    assert modulo_vector(a)==res

@pytest.mark.parametrize("a, res",[
    ("hola que tal",{'hola': [4], 'que': [3], 'tal': [3]}),
    ("chau nos vemos",{'chau': [4], 'nos': [3], 'vemos': [5]}),
    ("mi nombre es",{'mi': [2], 'nombre': [6], 'es': [2]}),
])
def test_dictionary_phrase(a, res):
    assert dictionary_phrase(a)==res  

@pytest.mark.parametrize("a, b, res",[
    (5,5,True),
    (5,10,True),
    (4,40,True),
])

def test_multiple(a,b,res):
    assert multiple(a,b)==res


@pytest.mark.parametrize("a, b, res",[
    (1,10,5.5),
    (1,9,5),
    (1,19,10),
])

def test_average_temp(a,b,res):
    assert average_temp(a,b)==res


@pytest.mark.parametrize("a, res",[
    ("hola","h o l a"),
    ("muybien","m u y b i e n"),
    ("torta","t o r t a"),
])

def test_separate(a, res):
    assert separate(a)==res