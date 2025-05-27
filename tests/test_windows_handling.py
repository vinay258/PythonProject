import  pytest
import time
import pytest_html
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec
from conftest import get_driver_to_application



new_tab_button="//button[contains(text(),'New Tab')]"
new_window_button="//button[contains(text(),'New Window')]"

def test_windows(get_driver_to_application):
    driver=get_driver_to_application
    wait=WebDriverWait(driver,10)
    actions=ActionChains(driver)
    #new_tab_ele=wait.until(ec.visibility_of_element_located((By.XPATH,new_tab_button)))
    new_window_ele = wait.until(ec.visibility_of_element_located((By.XPATH, new_window_button)))
    print("we need to scroll down the page to find the element")
    driver.execute_script("arguments[0].scrollIntoView();",new_window_ele)
    main_window=driver.current_window_handle
    print("the current window title is",driver.title)
    print("click on new tab")
    new_window_ele.click()
    time.sleep(2)
    #get all the windows
    windows=driver.window_handles
    # print("count of windows is:",len(windows))
    # print("switching into child window(new window)with index")
    # driver.switch_to.window(windows[1])
    # driver.maximize_window()
    # time.sleep(4)
    # driver.switch_to.window(windows[0])
    # print("the title of the main window:",driver.title)
    # time.sleep(2)
    for each_window in windows:
       if each_window!=main_window:
           driver.switch_to.window(each_window)
           print("the child tab window title is",driver.title)
           time.sleep(5)
    print("switching back to main window")
    driver.switch_to.window(main_window)