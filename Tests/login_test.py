# from selenium import webdriver
import moment
import allure
import time
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", ".."))
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Utils import utils as utils
from selenium.common.exceptions import ElementClickInterceptedException



@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        loginPage = LoginPage(driver)
        loginPage.enter_username(utils.UserName)
        loginPage.enter_password(utils.PassWord)
        loginPage.click_login_btn()

    def test_tasks(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.click_container_tasks()
        # try:
        #     homePage.click_container_tasks()
        #     raise
        # except ElementClickInterceptedException:
        #     time.sleep(5)
        #     homePage = HomePage(driver)
        #     homePage.click_container_tasks()

    def test_reports(self):
        driver = self.driver
        time.sleep(5)
        homePage = HomePage(driver)
        homePage.click_container_reports()

    def test_logout(self):
        try:
            driver = self.driver
            time.sleep(5)

            homePage = HomePage(driver)
            homePage.click_logout_link()
            x = driver.title
            assert x == "abc"

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + " " + currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("/Users/dilip.chauhan/Desktop/ActitimeFramework/Screenshots/" + screenshotName + ".png")

            raise

        except:
            print("There was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + " " + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            raise
        else:
            print("No exception occurred")
        finally:
            print("I'm inside finally block")

