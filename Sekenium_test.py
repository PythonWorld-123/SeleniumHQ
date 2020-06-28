import pytest
from selenium import webdriver
import time
import os
class Test:

   def test_one(self):
     global driver
     BASE_DIR=os.path.dirname(os.path.abspath(__file__))
     GECO_PATH=os.path.join(BASE_DIR,'Firefox_Geco_Driver\\geckodriver.exe')
     print("Hey..",GECO_PATH)
     driver=webdriver.Firefox(executable_path=GECO_PATH)
     driver.get("https://www.google.com/")
     driver.maximize_window()
     print(os.path.abspath(__file__))
     driver.find_element_by_name("q").send_keys("Hello")
     time.sleep(10)
     driver.close()
     
     