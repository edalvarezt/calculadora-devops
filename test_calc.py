import pytest
from calc import suma, resta, multiplicar, dividir


def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0


def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 5) == -5
    assert resta(-2, -3) == 1


def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 3) == -6
    assert multiplicar(0, 10) == 0


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(-6, 3) == -2
    assert dividir(5, 2) == 2.5

    # Verificar que lanza ValueError cuando b es 0
    with pytest.raises(ValueError, match="División por cero no permitida"):
        dividir(10, 0)
