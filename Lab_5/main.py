# Testowanie Automatyczne - Laboratorium nr 5
# 1. Wyszukanie/utworzenie rest api do testowania: https://github.com/toddmotto/public-apis
# 2.  W dowolnym języku podłączenie się do API
#     Napisać testy np.:
#     -niepoprawny request
#     -zawartość poprawnego requestu - czy istnieje
#     -zawartość konkretnych wartości (req -> /country=Poland res -> country: Poland)
#     -zwartość contentu -> klucze
# 3. (dodatkowe) - znaleźć api udostępniające możliwość dodawania danych, a nie tylko odczytywania i napisać testy dot. innej metody niż GET.
# Autor: Maciej Milewski


import requests
import unittest
import json


class RestApiTest(unittest.TestCase):
    URL_base = "https://www.breakingbadapi.com/api/"

    # Sprawdzenie konkretnej wartości
    def test_if_Walter_White_exsist(self):
        url = f"{self.URL_base}characters?name=Walter+White"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)
        self.assertEqual(json_response[0]['name'], "Walter White")

    # Sprawdzenie niepoprawnego request
    def test_incorrect_request(self):
        url = "https://covid-api.mmediagroup.fr/v1/aibshdbiabsdiasbdh?country={}".format("China")
        response = requests.request("GET", url)
        self.assertEqual(response.status_code, 403)

    # Sprawdzenie poprawnego request
    def test_correct_character_request(self):
        url = f"{self.URL_base}characters/1"
        response = requests.request("GET", url)
        self.assertEqual(response.status_code, 200)

    # Sprawdzenie wszystkich kluczy
    def test_all_keys(self):
        url = f"{self.URL_base}characters/1"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)

        expected = ['char_id', 'name', 'birthday', 'occupation', 'img',
                    'status', 'nickname', 'appearance', 'portrayed',
                    'category', 'better_call_saul_appearance']
        current = []

        for key in json_response[0]:
            if key in expected:
                current.append(key)

        assert expected == current

    # Sprawdzenie kluczy category i occupation
    def test_category_and_occupation_keys(self):
        url = f"{self.URL_base}characters/1"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)

        expected = ['occupation', 'category']
        current = []

        for key in json_response[0]:
            if key in expected:
                current.append(key)

        assert expected == current

    # Sprawdzenie konkretnej wartości
    def test_if_Jesse_Pinkman_YeahScience_quote_is_correct(self):
        url = f"{self.URL_base}quote?author=Jesse+Pinkman"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)
        self.assertEqual(json_response[12]['quote'], "Yeah, science!")

    # Sprawdzenie konkretnej wartości
    def test_if_death_count_is_correct(self):
        url = f"{self.URL_base}death-count?name=Gustavo+Fring"
        response = requests.request("GET", url)
        json_response = json.loads(response.text)
        self.assertEqual(json_response[0]['deathCount'], 22)

    # Sprawdzenie poprawnego request
    def test_correct_random_quote_request(self):
        url = f"{self.URL_base}quote/random"
        response = requests.request("GET", url)
        self.assertEqual(response.status_code, 200)

    # Sprawdzenie poprawnego request
    def test_correct_episodes_request(self):
        url = f"{self.URL_base}episodes"
        response = requests.request("GET", url)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()


