# Dodane dependencje:
  - [Joda Time](https://mvnrepository.com/artifact/joda-time/joda-time/2.10.10)
  - [Apache Commons Math](https://mvnrepository.com/artifact/org.apache.commons/commons-math3)

# Nowe testy:
 1) Dla nowych funkcji: 
 
    - sprawdzenie błędnego dodawania
    - sprawdzenie błędnego odejmowania
    - sprawdzenie błędnego mnożenia
    - czy liczba jest dodatnia z poprawny wynikiem
    - czy liczba jest dodatnia z niepoprawny wynikiem
    - poprawna konwersja tablicy do String
    - niepoprawna konwersja tablicy do String
    
 2) Dla funkcji korzystających z nowych dependencji:
 
    - sprawdzenie funkcji podającej obecny rok (Joda Time)
    - znalezienie mediany w tablicy z poprawnym wynikiem (Apache Commons Math)
    - znalezienie mediany w tablicy z niepoprawnym wynikiem (Apache Commons Math)