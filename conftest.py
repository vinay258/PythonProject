import time
import pytest
from selenium import webdriver




#url="https://www.facebook.com/login/"
#amazon_url_for_action_chains="https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=11054797545127890368&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9197649&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1"
#click_and_hold_url="https://testkru.com/Interactions/DragAndDrop"
#drag_and_drop_url="http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
#double_click_button_url="https://testpages.herokuapp.com/styled/events/javascript-events.html"
#Alerts_url="http://demoqa.com/alerts"
windows_handling_url="https://demoqa.com/browser-windows"
#web_tables_url="https://the-internet.herokuapp.com/tables"
#iframes_url="https://vinothqaacademy.com/iframe/"


@pytest.fixture(scope='function')
def get_driver_to_application():
    """Fixture to initialize and quit the Chrome WebDriver per test function."""
    driver = webdriver.Chrome()  # initialize the webdriver
    time.sleep(5)
    driver.maximize_window()  # maximize the window
    print("i am opening url")
    time.sleep(5)
    driver.get(windows_handling_url)
    yield driver
    time.sleep(5)
    driver.close()



@pytest.fixture(scope="class")
def common_fix():
    print("iam the common fixture")
    yield
    print("this is the last line i have printed after test case execution ")