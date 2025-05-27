import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec
import pytest_html
from conftest import get_driver_to_application



frame1_text1_xpath="//input[@placeholder='Name']"
frame1_text2_xpath="//input[@placeholder='Role']"

frame2_alert_button_xpath="//button[@name='confirmalertbox']"

frame3_male_radio_button="//input[@type='radio' and @value='Male']"



frame1="//iframe[@name='employeetable']"
frame2="//iframe[@name='popuppage']"
frame3="//iframe[@name='registeruser']"

def test_frame_handling(get_driver_to_application):
    driver=get_driver_to_application
    wait=WebDriverWait(driver,10)
    # Frame 1
    # Scroll to middle of page
    total_height = driver.execute_script("return document.body.scrollHeight")
    middle = total_height // 2
    driver.execute_script(f"window.scrollTo(0, {middle});")
    time.sleep(5)
    print("switching to frame1")
    driver.switch_to.frame("employeetable")
    driver.find_element(By.XPATH,frame1_text1_xpath).send_keys("Text in Frame 1")
    driver.find_element(By.XPATH,frame1_text2_xpath).send_keys("software")
    time.sleep(5)
    driver.switch_to.default_content()
    print("iam switching frame1 to frame2")
    driver.switch_to.frame("popuppage")
    #here we can see the Confirm alert box and click it
    alert=driver.find_element(By.XPATH,frame2_alert_button_xpath).click()
    #now you can see the popup window which is showing ok or cancel, we need to select any one
    driver.switch_to.alert.accept()
    time.sleep(5)
    driver.switch_to.default_content()
    print("iam switching frame2 to frame3")
    driver.switch_to.frame("registeruser")
    #here iam clicking the male radio after swatching to frame3
    radio=driver.find_element(By.XPATH,frame3_male_radio_button)
    radio.click()
    time.sleep(5)


