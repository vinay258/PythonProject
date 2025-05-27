import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec
import pytest_html
from conftest import get_driver_to_application




user_name_input="//input[@type='text']"
password_input="//input[@type='password']"
login_button="//button[@type='submit']"
forgot_account="//a[contains(text(),'Forgot')]"
sign_up_for_free="//a[contains(text(),'Sign')]"
first_name="//input[@name='firstname']"
last_name="//input[@name='lastname']"
birth_date="//select[@id='day']"
birth_month="//select[@id='month']"
birth_year="//select[@id='year']"
sign_up_for_free_female_radio="//input[@type='radio' and @value='1']"



def test_open_facebook_page(get_driver_to_application):
    """ open facebook home and enter the details username and password and click signup option and select the female
    radio button"""
    driver = get_driver_to_application
    # Wait for username field before finding it
    wait=WebDriverWait(driver,10)
    print("iam finding the web element")
    sign_up_ele=wait.until(ec.element_to_be_clickable((By.XPATH,sign_up_for_free)))
    sign_up_ele.click()
    first_name_ele=wait.until(ec.element_to_be_clickable((By.XPATH,first_name)))
    first_name_ele.send_keys("vinay")
    last_name_ele=wait.until(ec.element_to_be_clickable((By.XPATH,last_name)))
    last_name_ele.send_keys("kumar")

    # Click the dropdown to reveal options
    date=Select(wait.until(ec.element_to_be_clickable((By.XPATH,birth_date))))
    #select by value with the help of .select_by_value()
    date.select_by_value('7')
    print("iam selecting the value 7")

    month=Select(wait.until(ec.element_to_be_clickable((By.XPATH,birth_month))))
    #select by visible text with th help of .select_by_visible_text()
    month.select_by_visible_text('Oct')
    print("iam selecting the text oct")

    year=Select(wait.until(ec.element_to_be_clickable((By.XPATH,birth_year))))
    #select by index with the help of .select_by_index()
    year.select_by_index(2)
    print("iam selecting the index 2(year 2023)")

    radio=driver.find_element(By.XPATH,sign_up_for_free_female_radio)
    radio.click()
    print("iam clicking female radio button")

    for option in month.options:
        print(option.text)  # To get visible text
    for option in date.options:
        print(option.text)



