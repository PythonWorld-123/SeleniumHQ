import os
print(__file__)
print(os.path.abspath(__file__))
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
GECO_PATH=os.path.join(BASE_DIR,'Firefox_Geco_Driver\\geckodriver.exe')
print(GECO_PATH)