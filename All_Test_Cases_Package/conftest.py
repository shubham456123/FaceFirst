import os
import time

from datetime import date
from datetime import datetime

import pytest as pytest
# from _pytest.mark import param
from selenium import webdriver

# from All_POM_Package.LoginPage import Login
# from utilities import XLUtils
from pathlib import Path
resultPath = f"{Path(__file__).parent.parent}\\Test_Data\\Data_From_Excel\\Test_Cases.xlsx"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


from selenium import webdriver
import pytest
import logging
from logging import Logger
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import numpy as np

from Other_Utilities.Read_Excel import Read_excel

driver = None


@pytest.fixture(scope="class")
def setup1(request):
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        d = webdriver.Chrome(options=chrome_options)
        df = Read_excel.get_registration_form_data_df()
        df = df.replace(np.nan, '', regex=True)
        name = [i for i in df['Name']]
        email = [i for i in df['Email']]
        password = [i for i in df['new_password']]
        zip_list = zip(name, email, password)
        user_list = list(zip_list)
        one_second = 1
        two_second = 2
        three_second = 3
    except Exception as ex:
        print("init constructor in base class has an err: ", ex)

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = d
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        # driver = driver

    elif browser_name == "firefox":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    elif browser_name == "edge":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    '''
        driver.get("https://localhost/")
        # https: // rahulshettyacademy.com / angularpractice /
        driver.maximize_window()
        request.cls.driver = driver
    '''
    yield
    #driver.close()


@pytest.fixture(scope="class")
def setup(request):

    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        d = webdriver.Chrome(options=chrome_options)
        df = Read_excel.get_registration_form_data_df()
        df = df.replace(np.nan, '', regex=True)
        name = [i for i in df['Name']]
        email = [i for i in df['Email']]
        password = [i for i in df['new_password']]
        zip_list = zip(name, email, password)
        user_list = list(zip_list)
        one_second = 1
        two_second = 2
        three_second = 3
    except Exception as ex:
        print("init constructor in base class has an err: ", ex)



    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    elif browser_name == "firefox":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    elif browser_name == "edge":
        # driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        driver = d

    '''
    driver.get("https://localhost/")
    driver.maximize_window()
    login = Login(driver)
    login.setUser().clear()
    login.setUser().send_keys("shubham")
    login.setPass().send_keys("Shubham@123")
    time.sleep(2)
    login.driver.execute_script("arguments[0].click();", login.loginbtn())
    request.cls.driver = driver'''
    yield





def Implicit_wait(seconds):
    driver.implicitly_wait(seconds)


"""set Explicit wait function to be used by all the web elements where ever it is needed"""


def Explicit_wait(seconds, element):
    wait = WebDriverWait(driver, seconds)
    ele = wait.until(expected_conditions.element_to_be_clickable(element))



class Base_Class:

    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        d = webdriver.Chrome(options=chrome_options)
        df = Read_excel.get_registration_form_data_df()
        df = df.replace(np.nan, '', regex=True)
        name = [i for i in df['Name']]
        email = [i for i in df['Email']]
        password = [i for i in df['new_password']]
        zip_list = zip(name, email, password)
        user_list = list(zip_list)
        one_second = 1
        two_second = 2
        three_second = 3
    except Exception as ex:
        print("init constructor in base class has an err: ", ex)

    @staticmethod
    def logger_object():
        log_file_path = f'{Path(__file__).parent.parent}\\Application_Logs\\'
        formatter = logging.Formatter("%(asctime)s : %(name)-12s : %(levelname)-8s : %(message)s",
                                      datefmt='%d/%m/%Y %r')
        handler = logging.FileHandler(filename=f'{log_file_path}\\Application_Logs.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        return logger
