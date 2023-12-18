from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class HomeTestCase(StaticLiveServerTestCase):
    def setUp(self):
        #Opciones de Chrome
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        super().setUp()
    
    def tearDown(self):
        super().tearDown()
        self.driver.quit()
    
    def test_traduccion_español(self):
        #Abre la ruta del navegador
        self.driver.get(f'{self.live_server_url}/esp/')
        # Obtén el texto completo de la página
        texto_pagina = self.driver.find_element(By.TAG_NAME, 'body').text
        # Lista de palabras en español que puedes verificar en el texto de la página
        palabras_en_espanol = ['Bienvenido']
        # Verifica si al menos una palabra en español está presente en el texto
        alguna_palabra_en_espanol_presente = any(palabra in texto_pagina for palabra in palabras_en_espanol)
        # Realiza una aserción para verificar si al menos una palabra en español está presente
        self.assertTrue(alguna_palabra_en_espanol_presente, "La URL /esp/ no contiene ninguna palabra en español")

    def test_traduccion_ingles(self):
        self.driver.get(f'{self.live_server_url}/home/')
        texto_pagina = self.driver.find_element(By.TAG_NAME, 'body').text
        palabras_en_ingles = ['Welcome']
        alguna_palabra_en_ingles_presente = any(palabra in texto_pagina for palabra in palabras_en_ingles)
        self.assertTrue(alguna_palabra_en_ingles_presente, "La URL /home/ no contiene ninguna palabra en ingles")

    def test_traduccion_frances(self):
        self.driver.get(f'{self.live_server_url}/fra/')
        texto_pagina = self.driver.find_element(By.TAG_NAME, 'body').text
        palabras_en_frances = ['Bienvenue']
        alguna_palabra_en_frances_presente = any(palabra in texto_pagina for palabra in palabras_en_frances)
        self.assertTrue(alguna_palabra_en_frances_presente, "La URL /fra/ no contiene ninguna palabra en frances")

    def test_traduccion_aleman(self):
        self.driver.get(f'{self.live_server_url}/alm')
        texto_pagina = self.driver.find_element(By.TAG_NAME, 'body').text
        palabras_en_aleman = ['Willkommen']
        alguna_palabra_en_aleman_presente = any(palabra in texto_pagina for palabra in palabras_en_aleman)
        self.assertTrue(alguna_palabra_en_aleman_presente, "La URL /alm/ no contiene ninguna palabra en aleman")

    def test_traduccion_español_fail(self):
        self.driver.get(f'{self.live_server_url}/esp/')
        texto_pagina = self.driver.find_element(By.TAG_NAME, 'body').text
        palabras_en_espanol = ['Bienvenue']
        alguna_palabra_en_espanol_presente = any(palabra in texto_pagina for palabra in palabras_en_espanol)
        self.assertTrue(alguna_palabra_en_espanol_presente, f"La URL /esp/ no contiene {palabras_en_espanol}")
    
    def test_traduccion_ingles_fail(self):
        self.driver.get(f'{self.live_server_url}/home/')
        texto_pagina = self.driver.find_element(By.TAG_NAME, 'body').text
        palabras_en_ingles = ['Bienvenido']
        alguna_palabra_en_ingles_presente = any(palabra in texto_pagina for palabra in palabras_en_ingles)
        self.assertTrue(alguna_palabra_en_ingles_presente, f"La URL /home/ no contiene {palabras_en_ingles}")

    def test_traduccion_frances_fail(self):
        self.driver.get(f'{self.live_server_url}/fra/')
        texto_pagina = self.driver.find_element(By.TAG_NAME, 'body').text
        palabras_en_frances = ['Willkommen']
        alguna_palabra_en_frances_presente = any(palabra in texto_pagina for palabra in palabras_en_frances)
        self.assertTrue(alguna_palabra_en_frances_presente, f"La URL /fra/ no contiene {palabras_en_frances}")

    def test_traduccion_aleman_fail(self):
        self.driver.get(f'{self.live_server_url}/alm')
        texto_pagina = self.driver.find_element(By.TAG_NAME, 'body').text
        palabras_en_aleman = ['Bienvenido']
        alguna_palabra_en_aleman_presente = any(palabra in texto_pagina for palabra in palabras_en_aleman)
        self.assertTrue(alguna_palabra_en_aleman_presente, f"La URL /alm/ no contiene {palabras_en_aleman}")
