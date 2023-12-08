from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from .models import Census
from base.tests import BaseTestCase

class CensusTestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.census = Census()
        self.census.save()

    def tearDown(self):
        super().tearDown()
        self.census = None

    #def test_list_census(self):
     #   response = self.client.get('census//search//?census_id=5')
      #  self.assertEqual(response.status_code, 404)

       # response = self.client.get('search//?census_id=1')
        #self.assertEqual(response.status_code, 200)

class CensusTest(StaticLiveServerTestCase):
    def setUp(self):
        #Load base test functionality for decide
        self.base = BaseTestCase()
        self.base.setUp()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()
    
    def createCensusSuccess(self):
        self.cleaner.get(self.live_server_url+"/admin/login/?next=/admin/")
        self.cleaner.set_window_size(1280, 720)

        self.cleaner.find_element(By.ID, "id_username").click()
        self.cleaner.find_element(By.ID, "id_username").send_keys("decide")

        self.cleaner.find_element(By.ID, "id_password").click()
        self.cleaner.find_element(By.ID, "id_password").send_keys("decide")

        self.cleaner.find_element(By.ID, "id_password").send_keys("Keys.ENTER")

        self.cleaner.get(self.live_server_url+"/admin/census/census/add")
        self.cleaner.find_element(By.ID, "id_name").click()
        self.cleaner.find_element(By.ID, "id_name").send_keys("CensoTest")
        self.cleaner.find_element(By.ID, "id_user_id").click()
        self.cleaner.find_element(By.ID, "id_user_id").send_keys("Keys.ENTER")
        self.cleaner.find_element(By.NAME, "_save").click()

        self.assertTrue(self.cleaner.current_url == self.live_server_url+"/admin/census/census")

    def createCensusNoNameError(self):
        self.cleaner.get(self.live_server_url+"/admin/login/?next=/admin/")
        self.cleaner.set_window_size(1280, 720)

        self.cleaner.find_element(By.ID, "id_username").click()
        self.cleaner.find_element(By.ID, "id_username").send_keys("decide")

        self.cleaner.find_element(By.ID, "id_password").click()
        self.cleaner.find_element(By.ID, "id_password").send_keys("decide")

        self.cleaner.find_element(By.ID, "id_password").send_keys("Keys.ENTER")

        self.cleaner.get(self.live_server_url+"/admin/census/census/add")

        self.cleaner.find_element(By.ID, "id_user_id").click()
        self.cleaner.find_element(By.ID, "id_user_id").send_keys("Keys.ENTER")
        self.cleaner.find_element(By.NAME, "_save").click()

        self.assertTrue(self.cleaner.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/form/div/p').text == 'Please correct the errors below.')
        self.assertTrue(self.cleaner.current_url == self.live_server_url+"/admin/census/census/add")

    def createCensusNoUserError(self):
        self.cleaner.get(self.live_server_url+"/admin/login/?next=/admin/")
        self.cleaner.set_window_size(1280, 720)

        self.cleaner.find_element(By.ID, "id_username").click()
        self.cleaner.find_element(By.ID, "id_username").send_keys("decide")

        self.cleaner.find_element(By.ID, "id_password").click()
        self.cleaner.find_element(By.ID, "id_password").send_keys("decide")

        self.cleaner.find_element(By.ID, "id_password").send_keys("Keys.ENTER")

        self.cleaner.get(self.live_server_url+"/admin/census/census/add")

        self.cleaner.find_element(By.ID, "id_name").click()
        self.cleaner.find_element(By.ID, "id_name").send_keys("CensoTest")
        self.cleaner.find_element(By.NAME, "_save").click()

        self.assertTrue(self.cleaner.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/form/div/p').text == 'Please correct the errors below.')
        self.assertTrue(self.cleaner.current_url == self.live_server_url+"/admin/census/census/add")

def listCensusFilter(self):
        self.cleaner.get(self.live_server_url+"/census")
        current = self.cleaner.current_url
        idNum = current.replace(self.live_server_url+'/census/search/?census_id=', '')
        self.assertTrue(current == self.live_server_url+"/census/search/?census_id="+ idNum)

        self.cleaner.find_element(By.XPATH, '/html/body/article/table[2]/tbody/tr/td/a[1]').click()
        current = self.cleaner.current_url
        idNum = current.replace(self.live_server_url+'/booth/', '')
        self.assertTrue(current == self.live_server_url+"/booth/"+ idNum)

