import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestForgotPassword(unittest.TestCase):
    email = (By.ID, "email")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.find_element(By.LINK_TEXT, "Forgot Password").click()

    def tearDown(self):
        self.chrome.quit()

    # test 1 - Verifică dacă noul url e corect

    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/forgot_password"
        assert actual_url == expected_url, f"Invalid url: expected:{expected_url}, actual: {actual_url}"

    # test 2 - Verifică dacă page title e corect

    def test_titlu(self):
        titlu = self.chrome.title
        expected_titlu = "The Internet"
        assert titlu == expected_titlu, f"Titlul invalid, expected:{expected_titlu}, actual: {titlu}"

    # test 3 - Verifică textul de pe elementul xpath=//h2 e corect

    def test_verifica_element_h2(self):
        element_h2 = self.chrome.find_element(By.XPATH, "//h2")
        expected_element_h2 = "Forgot Password"
        assert element_h2.text == expected_element_h2, f"Elementul h 2 nu este valid, expected:{expected_element_h2}, actual:{element_h2}"

# test 4 - Verifică dacă butonul de retrieve password este displayed

    def test_buton_retrieve_password(self):
        buton_retrieve_password = self.chrome.find_element(By.XPATH, "//button")
        assert buton_retrieve_password.is_displayed() == True, f"Butonul nu este afisat"

# test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_elementul_selenium(self):
        elementul_selenium = self.chrome.find_element(By.LINK_TEXT, "Elemental Selenium")
        expected_elementul_selenium = "http://elementalselenium.com/"
        assert elementul_selenium.get_attribute("href") == expected_elementul_selenium, f"Invalid href, expected: {expected_elementul_selenium}, actual:{elementul_selenium.get_attribute('href')}"

# test 6 - Lasă goale email
       # - Click login
       # - Verifică dacă eroarea e displayed

    def test_email_goale_click_login_eroare_displayed(self):
        self.chrome.find_element(By.XPATH, "//button").click()    # click Login
        eroare_email = self.chrome.find_element(By.XPATH, "//h1")   # identifica elemente in pagina dupa ID
        eroare_expected = "Internal Server Error"
        assert eroare_email.text == eroare_expected, f"Elementul h 2 nu este valid, expected:{eroare_expected}, actual:{eroare_email}"

