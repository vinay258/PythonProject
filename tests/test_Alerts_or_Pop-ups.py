import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec
import pytest_html
from conftest import get_driver_to_application
from selenium.webdriver import ActionChains


click_button="//button[@id='confirmButton']"
prompt_button="//button[@id='promtButton']"


def test_alert_and_popup_action(get_driver_to_application):
    driver = get_driver_to_application
    wait=WebDriverWait(driver,10)
    actions=ActionChains(driver)
    alert_ele=driver.find_element(By.XPATH,click_button)
    # Scroll into view using execute script
    driver.execute_script("arguments[0].scrollIntoView();",alert_ele)
    print("click the button ")
    alert_ele.click()
    time.sleep(2)
    print("pop up window will appear")
    confirmation_alert=driver.switch_to.alert
    print("confirmation text",confirmation_alert.text)
    confirmation_alert.dismiss()
    print("Cancel")
    time.sleep(2)
    prompt_button_ele=driver.find_element(By.XPATH,prompt_button)
    print("clicking on prompt button")
    prompt_button_ele.click()
    print("prompt pop up window will appear")
    alert_window=driver.switch_to.alert
    print("prompt message",alert_window.text)
    alert_window.send_keys('vinay')
    alert_window.accept()
