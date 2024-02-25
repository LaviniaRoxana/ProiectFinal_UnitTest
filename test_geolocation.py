import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestGeolocation(TestCase):

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.find_element(By.LINK_TEXT, "Geolocation").click()

    def tearDown(self):
        self.chrome.quit()

    # test 1 - Verifică dacă noul url e corect

    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/geolocation"
        assert actual_url == expected_url, f"Invalid url: expected:{expected_url}, actual: {actual_url}"

    # test 2 - Verifică dacă page title e corect

    def test_titlu(self):
        titlu = self.chrome.title
        expected_titlu = "The Internet"
        assert titlu == expected_titlu, f"Titlul invalid, expected:{expected_titlu}, actual: {titlu}"

    # test 3 - Verifică textul de pe elementul xpath=//h3 e corect

    def test_verifica_element_h3(self):
        element_h3 = self.chrome.find_element(By.XPATH, "//h3")
        expected_element_h3 = "Geolocation"
        assert element_h3.text == expected_element_h3, (f"Elementul h 3 nu este valid, "
                                                        f"expected:{expected_element_h3}, actual:{element_h3}")


    # test 4 - Verifică textul de pe elementul demo

    def test_verifica_element_informatii_obtinere_GPS(self):
        element_demo = self.chrome.find_element(By.ID, "demo")
        expected_element_demo = "Click the button to get your current latitude and longitude"
        assert element_demo.text == expected_element_demo, \
            f"Elementul demo nu este valid, expected:{expected_element_demo}, actual:{element_demo}"

# test 5 - Verifică dacă butonul de geolocation este displayed
    def test_buton_obtinere_gps(self):
        buton_geolocation = self.chrome.find_element(By.XPATH, "//button")
        assert buton_geolocation.is_displayed() == True, f"Butonul nu este afisat"


# test 6 - Click pe butonul Where I AM si verifica daca apar coordonatele

    def test_obtinere_latitudine(self):
        self.chrome.find_element(By.XPATH, "//button").click()
        actual_url = self.chrome.current_url
        element_demo_gps = self.chrome.find_element(By.ID, "demo")
        assert element_demo_gps.text.__contains__("latitude") == True, f"Nu contine informatii despre latitudine"

    def test_obtinere_longitudine(self):
        self.chrome.find_element(By.XPATH, "//button").click()
        actual_url = self.chrome.current_url
        element_demo_gps = self.chrome.find_element(By.ID, "demo")
        assert element_demo_gps.text.__contains__("longitude") == True, f"Nu contine informatii despre longitudine"