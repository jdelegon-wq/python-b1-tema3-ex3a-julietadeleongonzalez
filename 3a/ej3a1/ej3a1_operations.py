# archivo ej3a1_operations.py


def add(num_1: float, num_2: float) -> float:
    # Write here your code
    """Devuelve la suma de dos números"""
    return num_1 + num_2


def subtract(num_1: float, num_2: float) -> float:
    # Write here your code
    """Devuelve la resta de dos números"""
    return num_1 - num_2


def multiply(num_1: float, num_2: float) -> float:
    # Write here your code
    """Devuelve el producto de dos números"""
    return num_1 * num_2


def divide(num_1: float, num_2: float) -> float:
    # Write here your code
    """Devuelve la división de dos números"""
    """Maneja división entre 0"""
    if num_2 == 0:
        raise ValueError("No se puede dividir entre 0"""
    return num_1 / num_2
