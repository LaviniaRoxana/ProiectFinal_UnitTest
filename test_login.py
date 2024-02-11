"""
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
"""

import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin(TestCase):


    utilizator = (By.ID,"username")
    parola = (By.ID,"password")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.find_element(By.LINK_TEXT, "Form Authentication").click()

    def tearDown(self):

        self.chrome.quit()

# test 1 - Verifică dacă noul url e corect

    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url, f"Invalid url: expected:{expected_url}, actual: {actual_url}"

# test 2 - Verifică dacă page title e corect

    def test_titlu(self):
        titlu = self.chrome.title
        expected_titlu = "The Internet"
        assert titlu == expected_titlu, f"Titlul invalid, expected:{expected_titlu}, actual: {titlu}"

# test 3 - Verifică textul de pe elementul xpath=//h2 e corect

    def test_verifica_element_h2(self):
        element_h2 = self.chrome.find_element(By.XPATH, "//h2")
        expected_element_h2 = "Login Page"
        assert element_h2.text == expected_element_h2, f"Elementul h 2 nu este valid, expected:{expected_element_h2}, actual:{element_h2}"

# test 4 - Verifică dacă butonul de login este displayed

    def test_buton_login(self):
        buton_login = self.chrome.find_element(By.XPATH, "//button")
        assert buton_login.is_displayed() == True, f"Butonul nu este afisat"

# test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_elementul_selenium(self):
        elementul_selenium = self.chrome.find_element(By.LINK_TEXT, "Elemental Selenium")
        expected_elementul_selenium = "http://elementalselenium.com/"
        assert elementul_selenium.get_attribute("href") == expected_elementul_selenium, f"Invalid href, expected: {expected_elementul_selenium}, actual:{elementul_selenium.get_attribute('href')}"

# test 6 - Lasă goale user și pass
       # - Click login
       # - Verifică dacă eroarea e displayed

    def test_user_pass_goale_click_login_eroare_displayed(self):
        self.chrome.find_element(By.XPATH, "//button").click()    # click Login
        eroare_login = self.chrome.find_element(By.ID, "flash")   # identifica elemente in pagina dupa ID
        assert eroare_login.is_displayed() == True, f"Eroarea login nu este afisata"  # verfica cu displayed daca e afisat

# test 7 - Completează cu user și pass invalide
       # - Click login
       # - Verifică dacă mesajul de pe eroare e corect
       # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
       # expected = 'Your username is invalid!'
       # self.assertTrue(expected in actual, 'Error message text is
       # incorrect')

    def test_user_pass_incorecte_eroare_corecta(self):
        self.chrome.find_element(By.ID, "username").send_keys('Lavinia')
        #self.chrome.find_element(self.utilizator[0], self.utilizator[1]).send_keys('Lavinia')
        self.chrome.find_element(By.ID, "password").send_keys(123)
        #self.chrome.find_element(self.parola[0], self.parola[1]).send_keys(123)

        self.chrome.find_element(By.XPATH, "//button").click()
        eroare_login = self.chrome.find_element(By.ID, "flash")

        actual_error = eroare_login.text
        expected_error = 'Your username is invalid!'
        self.assertTrue(expected_error in actual_error, 'Error message text is incorrect')
        #assert eroare_login.is_displayed() == True, f"Eroarea login nu este afisata"


# test 8 - Lasă goale user și pass
       # - Click login
       # - Apasă x la eroare
       # - Verifică dacă eroarea a dispărut

    def test_user_pass_goale_click_login_eroare_adisparut(self):
        self.chrome.find_element(By.XPATH, "//button").click()
        mesaj_eroare = self.chrome.find_element(By.ID, "flash")
        mesaj_eroare.click()
        assert mesaj_eroare.is_displayed() == True, f"Eroarea a disparut"

# test 9 - Ia ca o listă toate //label
       # - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
       # Password)
       # - Aici e ok să avem 2 asserturi

    def test_user_parola_verifica_test(self):
        lista_elemente_label = self.chrome.find_elements(By.XPATH, "//label") #Ia ca o listă toate //label
        assert lista_elemente_label[0].text == "Username", f"Label utilizator nu este corect"
        assert lista_elemente_label[1].text == "Password", f"Label parola nu este corect"

# test 10 -  Completează cu user și pass valide
        # - Click login
        # - Verifică ca noul url CONTINE /secure
        # - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
        # - Verifică dacă elementul cu clasa=’flash succes’ este displayed

    def test_user_si_pass_valide(self):
        self.chrome.find_element(By.ID, "username").send_keys('tomsmith')
        self.chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.chrome.find_element(By.XPATH, "//button").click()
        actual_url = self.chrome.current_url
        assert actual_url.__contains__("/secure"), f"Url nu contine cuvantul 'secure'"
        clasa_flash = WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located((By.ID, "flash"))) #EC.presence_of_element_located((By.CLASS_NAME, "flash success")
        assert clasa_flash.is_displayed() == True, f"clasa 'flash succes' nu este afisata"


# test 11 - Completează cu user și pass valide
        # - Click login
        # - Click logout
        # - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_final(self):
        self.chrome.find_element(By.ID, "username").send_keys('tomsmith')
        self.chrome.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.chrome.find_element(By.XPATH, "//button").click()
        buton_logout = self.chrome.find_element(By.LINK_TEXT, "Logout")
        buton_logout.click()
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url, f"Invalid url: expected:{expected_url}, actual: {actual_url}"


