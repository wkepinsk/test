
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

firstname="Marcin"
lastname="Kowalski"
gender='male'
country_code="+48"
valid_phone_number="123123123"
invalid_email = 'jhsdhfjh.pl'
valid_country = "Chiny"
password = "Qwerty123@sjdjk"

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        """
        Warunki wstępne
        """
        # Przeglądarka włączona
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # na stronie wizzair.com/Pl-pl
        self.driver.get('https://wizzair.com/pl-pl#/')

    def tearDown(self):
        """
        Sprzątanie po teście
        """
        self.driver.quit()

    def testWrongEmail(self):
        """
        TC 001: Niekompletny email brak '@')
        """
        # KROKI:
        driver = self.driver
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        zaloguj_btn = WebDriverWait(driver, 45).\
            until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()
        #  2. Kliknij REJESTRACJA
        WebDriverWait(driver, 45).\
            until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Rejestracja "]'))).click()
        # 3. Wprowadź imię
        fn = WebDriverWait(driver, 45). \
            until(EC.element_to_be_clickable((By.NAME, 'firstName')))
        fn.send_keys(firstname)
        # 4. Wprowadź nazwisko
        driver.find_element_by_name('lastName').send_keys(lastname)
        # 5. Wybierz płeć
        if gender == 'male':
            m = driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            fn.click()
            m.click()
            # driver.execute_script('arguments[0].click()', m)
        else:
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()

        # 6. Wpisz kod kraju
        cc = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        cc.click()
        cc2 = driver.find_element_by_xpath('//input[@name="phone-number-country-code"]')
        cc2.send_keys(country_code)
        country_to_choose = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-test='PL']")))
        country_to_choose.click()
        # 7. Wpisz nr telefonu
        driver.find_element_by_name("phoneNumberValidDigits").send_keys(valid_phone_number)
        # 7. Wpisz niepoprawny e-mail (brak znaku '@')
        driver.find_element_by_name("email").send_keys(invalid_email)
        # 8. Wpisz hasło
        driver.find_element_by_name("password").send_keys(password)
        # 9. Wybierz narodowość
        country_field = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        # Wyszukaj kraje
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        # Poszukaj elementow "label" wewnatrz listy "countries"
        countries = country_to_choose.find_elements_by_tag_name("label")
        # Iteruj po kazdym elemencie w liscie "countries"
        for label in countries:
            # Wewnatrz "label" znajdz element "strong"
            option=label.find_element_by_tag_name('strong')
            # Jesli tekst elementu jest taki jak zadany w valid_country
            if option.get_attribute("innerText") == valid_country:
                # Przewin do tego elementu
                option.location_once_scrolled_into_view
                # Kliknij
                option.click()
                # Wyjdz z petli - juz znalazlem i kliknalem
                break

        time.sleep(4)

if __name__=='__main__':
    unittest.main(verbosity=2)
