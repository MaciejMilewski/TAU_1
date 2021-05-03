# Opis zadania na laboratorium nr 7:
#
# 1. Do istniejącego (np. z lab 6) projektu dopisać metodą którą da się przetestować w sposób umożliwiający
# parametryzację, czyli podanie różnych danych.
#
# 2. Dane zawarte jako parametry mają testować różne warunki brzegowe.
# Np. niepoprawny scenariusz: testuję przedział <-2;2>, czy podane liczby zawierają się w przedziale, dane to: [-1,0,1]
# - został przetestowany tylko jeden warunek brzegowy, poprawny scenariusz: testuję przedział <-2;2>, czy podane liczby
# zawierają się w przedziale, liczby to: [0,7, -30, “string do testów”] - przetestowano 4 warunki brzegowe.
#
# Autor: Maciej Milewski 17947


import os


if __name__ == '__main__':
    # Testy dla laboratorium nr 6
    # os.system("pytest tests/TestWindowsCommandsManual.py tests/TestLinuxCommandsManual.py tests/TestCommandsManual.py")

    # Testy dla laboratorium nr 7
    os.system("pytest tests/TestMaturaFunctions.py")
