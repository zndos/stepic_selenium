from selenium import webdriver
import time

import unittest

class TestFirstPage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def fill_form(self,link):
        """заполняет рег поля"""

        self.browser.get(link)
        input1 = self.browser.find_element_by_css_selector(".form-group:nth-child(1) input[required]")
        input1.send_keys("Petrov")

        input2 = self.browser.find_element_by_css_selector(".form-group:nth-child(2) input[required]")
        input2.send_keys("Petrov")

        input3 = self.browser.find_element_by_css_selector(".form-group:nth-child(3) input[required]")
        input3.send_keys("Petrov")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)  # TODO expected condition

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text


    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        result=self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", result,
                         f"Should be Congratilations,but got {result}")
        time.sleep(2)



    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", result,
                         f"Should be Congratilations,but got {result}")
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
