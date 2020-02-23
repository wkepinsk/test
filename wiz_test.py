from selenium import webdriver
import  time
import unittest

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        """
        Warunki wstepne
        """
        #Przegladarka wlaczona na stronie wizzair.com/pl-pl
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl')
    def tearDown(self):
        """
        sprzatamy po tescie
        """
        self.driver.quit()

    def testWrongEmail(self):
        """
        TC 001: Niekompletny email brak @
        """

        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
