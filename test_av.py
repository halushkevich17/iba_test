import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


class Av(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_login(self):
        driver = self.driver
        driver.get("https://www.av.by")
        self.assertIn("av.by", driver.title)


    def test_error_password(self):
        driver = self.driver
        driver.get("https://www.av.by")
        self.assertIn("av.by", driver.title)
        # time.sleep(5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="nav__link js-open-auth-drawer"]')))
        driver.find_element_by_xpath('//a[@class="nav__link js-open-auth-drawer"]').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login"]')))
        driver.find_element_by_xpath('//input[@id="login"]').send_keys("test@gmail.com")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]')))
        driver.find_element_by_xpath('//input[@type="password"]').send_keys("Test1234")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '// div[text()="Неверный логин или пароль. Если забыли пароль, восстановите его"]')))
        self.assertIn("Неверный логин или пароль. Если забыли пароль, восстановите его", driver.page_source)

    def test_alfa_romeo2(self):
            driver = self.driver
            driver.get("https://www.av.by")
            self.assertIn("av.by", driver.title)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="nav__link js-open-auth-drawer"]')))
            driver.find_element_by_xpath('//a[@class="nav__link js-open-auth-drawer"]').click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login"]')))
            driver.find_element_by_xpath('//input[@id="login"]').send_keys("halushkevich911@gmail.com")
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]')))
            driver.find_element_by_xpath('//input[@type="password"]').send_keys("Test1234")
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
            driver.find_element_by_xpath('//button[@type="submit"]').click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://cars.av.by/alfa-romeo"]')))
            driver.find_element_by_xpath('//a[@href="https://cars.av.by/alfa-romeo"]').click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Купить Alfa Romeo"]')))
            self.assertIn("Купить Alfa Romeo", driver.page_source)



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
