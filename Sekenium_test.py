import pytest
from selenium import webdriver
import time

class Test:

   def test_one(self):
     global driver
     driver=webdriver.Firefox(executable_path='C:\\Users\\Anil\\Desktop\\HQ\\Firefox_Geco_Driver\\geckodriver.exe')
     driver.get("https://www.google.com/")
     driver.maximize_window()
     driver.find_element_by_name("q").send_keys("Hello")
     time.sleep(10)
     driver.close()
     
     