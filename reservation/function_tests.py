import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
class NewVisitorTest(unittest.TestCase) :
    def setUp(self) :
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Users\alkad\Desktop\chromedriver_win32\chromedriver.exe", )

    def tearDown(self) :
        self.driver.quit()
    def test_can_start_a_list_and_retrieve_it_later(self) :
        self.driver.get("http://localhost:8000")

        self.assertIn('Galpung', self.driver.title)
        self.fail('테스트 종료')

if __name__ == '__main__' :
    unittest.main(warnings='ignore')