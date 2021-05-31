# Laboratorium - Travis ![alt text](https://travis-ci.com/MaciejMilewski/TAU_1.svg?branch=main)
Użycie narzędzia Continuous Integration do testowania projektu z Lab 6.
  - [https://travis-ci.com/](https://travis-ci.com/)

# Projekt na travis-ci.com: 
![alt text](img/travis_project_page.png?raw=true "Project panel on travis-ci.com")

# Log z testu:
![alt text](img/result.png?raw=true "Output logs from travis website")

# Konfiguracja .travis.yml
```
language: python
before_install: cd Lab_6
script:
  - pytest tests/TestWindowsCommandsManual.py tests/TestLinuxCommandsManual.py tests/TestCommandsManual.py
install:
  - pip install -r requirements.txt
```