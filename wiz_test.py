from selenium import webdriver
import  time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

imie = 'Jan'
nazwisko = 'Nowak'
gender = 'male'
country_code = '+48'
phone_number = '123123123'
email = 'nowak.gmail.com'
password = 'brakhasla'


class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        """
        Warunki wstepne
        """
        #Przegladarka wlaczona na stronie wizzair.com/pl-pl
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl')



    def testWrongEmail(self):
        """
        TC 001: Niekompletny email brak @
        """
        driver=self.driver
        zalogu_btn = WebDriverWait(driver ,40).until(EC.element_to_be_clickable((By.XPATH, '// button[@data-test="navigation-menu-signin"]')))
        zalogu_btn.click()

        rejstracja_btn = WebDriverWait(driver , 40).until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Rejestracja "]')))
        rejstracja_btn.click()
        #wybierz imie
        fn = WebDriverWait(driver ,45).until(EC.element_to_be_clickable((By.NAME,'firstName')))
        fn.send_keys(imie)
        # imie_input = driver.find_element_by_name('firstName')
        # imie_input.send_keys(imie)
        #wybierz nazwisko
        WebDriverWait(driver , 45).until(EC.element_to_be_clickable((By.NAME, 'lastName'))).send_keys(nazwisko)
        #wybierz plec
        if gender == 'male':
            m = driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            fn.click()
            m.click()
        else:
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()
        #kod kraju
        cc = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')

        cc.click()
        cc2 = driver.find_element_by_xpath('//input[@name="phone-number-country-code"]')
        cc2.send_keys(country_code)

        country_to_choose = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-test='PL']")))
        country_to_choose.click()

        # wpisz numer telefonu
        pn = driver.find_element_by_xpath('//input[@data-test="check-in-step-contact-phone-number"]')
        pn.send_keys(phone_number)
        #podaj adres invalid_email
        ie = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        ie.send_keys(email)
        # podaj passswd
        pw = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        pw.send_keys(password)


        time.sleep(10)
    def tearDown(self):
            """
            sprzatamy po tescie
            """
            self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
