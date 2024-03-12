#!/usr/bin/env python
"""Imprime a tabuaa do 1 ao 10."""
__version__ = "0.1.0"
__author__ = "Alciliano da Silva Lima"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# range é não inclusivo, por isso tem de colocar até 11
numeros = list(range(1, 11))  

# iterable (percorríveis)
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        reultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {reultado}"))
    print("#" * 18 )
