import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    time.sleep(2)


    lol = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    print("lol")
    button.click()
    # button1 = browser.find_element_by_css_selector("[type='submit']")
    # button1.click()
    #
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    #
    x=browser.find_element_by_id("input_value").text
    #
    print(x)
    ans=str(math.log(abs(12 * math.sin(int(x)))))
    # print(ans)
    res=browser.find_element_by_xpath("//*[@id='answer']")
    #
    res.send_keys(ans)
    #
    button1 = browser.find_element_by_css_selector("[type='submit']")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций

