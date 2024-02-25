import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestLinkuri(TestCase):

    utilizator = (By.ID,"username")
    parola = (By.ID,"password")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://the-internet.herokuapp.com/")

    def tearDown(self):

        self.chrome.quit()

# test 1 - V# testeaza ca linkurile de Login, Forgot Password si Geolocatie exista pe pagina

    def test_textul_linkurilor_exista(self):
        html_links_list = self.chrome.find_element(By.TAG_NAME, "ul")
        items = html_links_list.find_elements(By.TAG_NAME, "li")

         # extragem lista de texte de pe linkuri si verificam ca textele pt linkurile de 'Form Authentication', 'Forgot Password', 'Geolocation' exista in lista
        lista_texte_linkuri = []
        for item in items:
            lista_texte_linkuri.append(item.text)

        texte_linkuri_cautate = ['Form Authentication', 'Forgot Password', 'Geolocation']
        assert 'Forgot Password' in lista_texte_linkuri and 'Form Authentication' in lista_texte_linkuri and 'Geolocation' in lista_texte_linkuri, 'Unul dintre sau toate linkurile: Forgot Password, Login sau Geolocatie nu este prezente in pagina'
        for item in texte_linkuri_cautate:
            assert item in lista_texte_linkuri

    # numaram numarul de linkuri de pe pagina, trebuie sa fie 44
    def test_numarul_de_linkuri(self):
        html_links_list = self.chrome.find_element(By.TAG_NAME, "ul")
        items = html_links_list.find_elements(By.TAG_NAME, "li")

        # extragem lista de texte de pe linkuri si verificam ca textele pt linkurile de 'Form Authentication', 'Forgot Password', 'Geolocation' exista in lista
        lista_texte_linkuri = []
        for item in items:
            lista_texte_linkuri.append(item.text)

        assert len(lista_texte_linkuri) == 44, 'Numarul de linkuri de pe pagina trebuie sa fie egal cu 44'













