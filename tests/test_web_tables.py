import  pytest
import time
import pytest_html
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec
from conftest import get_driver_to_application




rows_xpath="//table[@id='table1']//tr"
columns_xpath="//table[@id='table1']//th"
cell_xpath="//table[@id='table1']//tr[{}]//td[{}]"

rows_t2="//table[@id='table2']//tr"
column_t2="//table[@id='table2']//th"
cell_xpath_t2="//table[@id='table2']//tr//td"


def test_web_tables(get_driver_to_application):
    driver=get_driver_to_application
    wait=WebDriverWait(driver,10)
    rows_ele=driver.find_elements(By.XPATH,rows_xpath)
    column_ele=driver.find_elements(By.XPATH,columns_xpath)
    no_of_rows=len(rows_ele)
    no_of_columns=len(column_ele)
    print("the no of rows in table1:",no_of_rows)
    print("the no of columns in table1:",no_of_columns)
    for row in range(1,no_of_rows):
        print("the {} row data is...".format(row))
        for col in range(1,no_of_columns+1):
            #here we are dynamically build the xpath to locate  the cell based in the current row and col
            required_cell_xpath=cell_xpath.format(row,col)
            cell_ele=driver.find_element(By.XPATH,required_cell_xpath)
            time.sleep(2)
            print(cell_ele.text,end=" ")
        print()
    print("iam done with reading the table1")

    print("now iam reading the second table")
    #Element-based iteration
    rows=driver.find_elements(By.XPATH,rows_t2)
    r=len(rows)
    print("the no of rows :",r)
    for Row in rows:
        cols=Row.find_elements(By.TAG_NAME,"td")
        for Col in cols:
            print(Col.text,end=" ")
        print()
    print("iam done reading the table2")
