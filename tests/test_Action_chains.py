import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec
import pytest_html
from conftest import get_driver_to_application
from selenium.webdriver import ActionChains



indian_flag="//span[@class='icp-nav-link-inner']"
sign_in_link="//span[contains(text(),'Hello')]"
click_and_hold="//div[@id='box1']"
source_xpath="//div[@id='box1']"
target_xpath="//div[contains(text(),'Italy')]"
source1_xpath="//div[@id='box3']"
target1_xpath="//div[contains(text(),'Spain')]"
double_click_button="//button[@id='ondoubleclick']"
right_click_button="//button[@id='oncontextmenu']"



@pytest.mark.skip(reason="iam not using this")
def test_mouse_hover_action(get_driver_to_application):
    driver = get_driver_to_application
    wait=WebDriverWait(driver,10)
    actions=ActionChains(driver)
    indian_flag_ele=wait.until(ec.visibility_of_element_located((By.XPATH,indian_flag)))
    print("the indian flag ele is ",indian_flag_ele.is_enabled())
    actions.move_to_element(indian_flag_ele).perform()
@pytest.mark.skip(reason="iam not using this")
def test_mouse_over_action2(get_driver_to_application):
    driver = get_driver_to_application
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    sing_in_ele=wait.until(ec.visibility_of_element_located((By.XPATH,sign_in_link)))
    actions.move_to_element(sing_in_ele).perform()
@pytest.mark.skip(reason="iam not using this")
def test_click_and_hold(get_driver_to_application):
    driver = get_driver_to_application
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    box_c_ele=wait.until(ec.visibility_of_element_located((By.XPATH,click_and_hold)))
    actions.move_to_element(box_c_ele)
    # Perform click and hold on the element
    actions.click_and_hold(box_c_ele).perform()
    print("the element is ", box_c_ele.is_enabled())
    # Hold for 3 seconds to observe the effect
    time.sleep(5)
    # Release the mouse button
    actions.release().perform()
    time.sleep(4)
@pytest.mark.skip(reason="currently iam not using this")
def test_drag_and_drop(get_driver_to_application):
    driver = get_driver_to_application
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    source_ele=wait.until(ec.visibility_of_element_located((By.XPATH,source_xpath)))
    target_ele=wait.until(ec.visibility_of_element_located((By.XPATH,target_xpath)))
    source1_ele=wait.until(ec.visibility_of_element_located((By.XPATH,source1_xpath)))
    target1_ele=wait.until(ec.visibility_of_element_located((By.XPATH,target1_xpath)))
    #using drag and drop method
    actions.drag_and_drop(source_ele,target_ele).perform()
    time.sleep(2)
    #using click and hold method
    actions.click_and_hold(source1_ele).move_to_element(target1_ele).release().perform()
    time.sleep(2)
def test_double_click(get_driver_to_application):
    driver = get_driver_to_application
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    double_click_ele=wait.until(ec.visibility_of_element_located((By.XPATH,double_click_button)))
    actions.double_click(double_click_ele).perform()
    print("the double click button is ",double_click_ele.is_enabled())
    right_click_button_ele=wait.until(ec.visibility_of_element_located((By.XPATH,right_click_button)))
    actions.context_click(right_click_button_ele).perform()
    print("the context click button is",right_click_button_ele.is_enabled())

