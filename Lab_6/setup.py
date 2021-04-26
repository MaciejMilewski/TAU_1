# Opis zadania na laboratorium nr 6:
# 1. Utworzyć 3 klasy w pythonie:
#     a)klasę, która będzie przyjmowała jako parametr sterownik (“Windows” lub “Linux”), w niej metody:
#         1.1 generowanie help’a - słownik, którego kluczem będzie polecenie shellowe dla odpowiedniego systemu,
#         wartości to parametry w postaci kolejnego słownika, gdzie kluczem będzie parametr, a wartością jego opis (minimum 5 poleceń)
#         {
#             'ls': {
#                 '-l': 'wyświetlanie  szczegółowe',
#                 '-la': 'asd asd'
#             }
#         }
#         1.2 wyświetlanie opisu danej komendy, funkcja przyjmuje komendę, zwraca jej opis
#     b) klasę testową, która testować będzie Windowsowe polecenia
#     c) klasę testową, która testować będzie Linuxowe polecenia
#
# UWAGA: Celowo nie podaję tego ile i jakie testy mają się pojawić, by obudzili Państwo kreatywność i sami przemyśleli przypadki warte przetestowania.
# Autor: Maciej Milewski 17947


import os


if __name__ == '__main__':
    os.system("pytest tests/TestWindowsCommandsManual.py tests/TestLinuxCommandsManual.py tests/TestCommandsManual.py")

