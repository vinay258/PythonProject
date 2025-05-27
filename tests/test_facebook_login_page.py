import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec
import pytest_html
from selenium.webdriver.common.action_chains import ActionChains
from conftest import get_driver_to_application



user_name_input="//input[@type='text']"
password_input="//input[@type='password']"
login_button="//button[@type='submit']"
forgot_account="//a[contains(text(),'Forgot')]"
sign_up_for_free="//a[contains(text(),'Sign')]"
first_name="//input[@name='firstname']"
last_name="//input[@name='lastname']"
birth_date="//select[@id='day']"
sign_up_for_free_female_radio="//input[@type='radio' and @value='1']"
def test_open_facebook_page(get_driver_to_application):
    """ open facebook home and enter the details username and password and click signup option and select the female
    radio button"""
    driver = get_driver_to_application
    actions=ActionChains(driver)
    # Wait for username field before finding it
    wait=WebDriverWait(driver,10)
    print("iam finding the web element")
    sign_up_ele=wait.until(ec.element_to_be_clickable((By.XPATH,sign_up_for_free)))
    sign_up_ele.click()
    first_name_ele=wait.until(ec.element_to_be_clickable((By.XPATH,first_name)))
    first_name_ele.send_keys("vinay")
    last_name_ele=wait.until(ec.element_to_be_clickable((By.XPATH,last_name)))
    last_name_ele.send_keys("kumar")
    dropdown=wait.until(ec.element_to_be_clickable((By.XPATH,birth_date)))
    #dropdown.select_by_value("7")
    # Hover and click Day
    actions.move_to_element(dropdown).click().perform()
    time.sleep(5)  # Optional delay
    driver.find_element(By.XPATH, "//option[@value='7']").click()


    female_radio_ele=driver.find_element(By.XPATH,sign_up_for_free_female_radio)
    female_radio_ele.click()
    #female_radio_ele=wait.until(ec.element_to_be_clickable((By.XPATH, sign_up_for_free_female_radio)))
    #female_radio_ele.click()
    #user_ele.send_keys("7975999524")
    #Wait for password field and type text
    #pass_ele=driver.find_element(By.XPATH,password_input)
    #wait.until(ec.element_to_be_clickable(pass_ele))
    #pass_ele.send_keys("Vinay@123")
    # Wait for Login button and click
    #login_ele=driver.find_element(By.XPATH,login_button)
    #wait.until(ec.element_to_be_clickable(login_ele))
    #login_ele.click()"""
    #print("Is password ele is enabled>>",female_radio_ele.is_enabled())
    #print("Is password ele id displayed",female_radio_ele.is_selected())
    print("first name ele is enabled>>",first_name_ele.is_enabled())
    print("last name ele is enabled",last_name_ele.is_enabled())
    if female_radio_ele.is_selected():
        print("Female radio button is already selected")
    else:
        female_radio_ele.click()
        print("Selected the female radio button")