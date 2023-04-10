import re
import time
from pathlib import Path

import pyautogui
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from All_Test_Cases_Package.conftest import Base_Class
from Config_Package.Excel_Config_Files import XLUtils
from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from Config_Package.INI_Config_Files.Tags_Read_INI import Read_Tags_Components
from Config_Package.INI_Config_Files.Visitor_search_Read_INI import Read_Visitor_Search_Components

test_data = "D://FaceFirst Project All Files\FF_Automation_python\Current Python Framework\FF_Automation_Project_1.0\Test_Data\Data_From_Excel\Test_Data_XLSX.xlsx"

class Visitor_Search_Module_pom:

    def __init__(self):
        self.d = Base_Class.d

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(Base_Class.one_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(Base_Class.one_second)
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
            visitorsearchbtn = self.d.find_element(By.XPATH,
                                                   Read_Portal_Menu_Components().portal_menu_visitors_search_btn_by_xpath())
            visitorsearchbtn.click()

        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_faild_for_portal_menu_pg_03.png")
                return False

    def visitor_search_with_only_match_count_criteria(self):

        try:

            self.add_image_search()

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.compare_count_match(count_data)

            self.close_all_panel_one_by_one()

            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_only_match_count_criteria_failed.png")
                return False

    def visitor_search_with_only_thresh_hold_search_criteria(self):
        try:

            self.add_image_search()

            self.set_thresh_hold_slider()

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.compare_thresh_hold_value_with_score()

            self.close_all_panel_one_by_one()

            self.click_on_logout_button()

            return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_only_thresh_hold_search_criteria_failed.png")
                return False

    def visitor_search_with_only_thresh_hold_and_count_criteria(self):
        try:
            self.add_image_search()

            self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            self.refresh_icon_wait()
            self.compare_count_match(count_data)
            self.compare_thresh_hold_value_with_score()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_only_thresh_hold_and_count_criteria_failed.png")
                return False

    def visitor_search_with_gender_criteria(self):
        try:
            self.add_image_search()

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()
            self.verify_gender_match_list(gender_data)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_gender_criteria_failed.png")
                return False

    def visitor_search_with_gender_and_count_criteria(self):
        try:
            self.add_image_search()

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()

            self.refresh_icon_wait()

            self.compare_count_match(count_data)

            self.verify_gender_match_list(gender_data)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_gender_and_count_criteria_failed.png")
                return False

    def visitor_search_with_gender_and_score_criteria(self):
        try:
            self.add_image_search()

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            self.set_thresh_hold_slider()
            self.click_on_submit_search_button()
            self.refresh_icon_wait()
            self.verify_gender_match_list(gender_data)
            self.compare_thresh_hold_value_with_score()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_gender_and_score_criteria_failed.png")
                return False

    def visitor_search_with_gender_count_and_score_criteria(self):
        try:
            self.add_image_search()

            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)

            self.set_thresh_hold_slider()
            self.click_on_submit_search_button()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_gender_count_and_score_criteria_failed.png")
                return False

    def visitor_search_with_age_criteria(self):
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)
            self.click_on_submit_search_button()
            self.refresh_icon_wait()
            self.validate_age_matches_list(start_age, end_age)
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_age_criteria_failed.png")
                return False

    def calender_handle(self):
        try:
            self.add_image_search()
            start_date_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_checkbox_by_xpath())
            start_date_checkbox.click()
            start_date_checkbox_input = self.d.find_element(By.XPATH,
                                                      Read_Visitor_Search_Components().start_date_by_xpath())
            start_date_checkbox_input.click()
            start_date_checkbox_input.clear()
            start_date_checkbox_input.send_keys("05/12/2022 5:12 AM")
            self.click_on_submit_search_button()
            self.refresh_icon_wait()
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\visitor_search_with_age_criteria_failed.png")
                return False

    ################## All reused methods #####################

    def select_start_age(self, start_age):
        """
        This function is used to select the start age
        :param start_age:
        :return:
        """
        start_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_age_by_xpath())
        s = Select(start_age_ele)
        s.select_by_visible_text(start_age)

    def select_end_age(self, end_age):
        """
        This function is used to select the end age
        :param end_age:
        :return:
        """
        end_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_age_by_xpath())
        s = Select(end_age_ele)
        s.select_by_visible_text(end_age)

    def validate_age_matches_list(self, start_age, end_age):
        """
        This function is used to validate the age from the matches list
        :param start_age:
        :param end_age:
        :return:
        """
        matches_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().matches_gender_by_xpath())
        for ele in matches_list:
            age = int(ele.text.split(" ")[1])
            print(age)
            if not int(start_age) <= age <= int(end_age):
                assert False

    def compare_thresh_hold_value_with_score(self):
        """
        This function is used to compare the threshhold value with actual score
        :return:
        """
        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().slider_icon_by_xpath())
        slider_value_str = str(slider.get_attribute("style"))
        slider_value_text = slider_value_str.split(" ")[1].strip()
        slider_value_text = re.sub("[% ;]", "", slider_value_text)
        print("slider text is ====>>>> ", slider_value_text)

        match_list_score = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().score_by_xpath())
        for ele in match_list_score:
            score = ele.text
            score = int(score.split(".")[1][0:2])
            if not score >= int(slider_value_text):
                assert False



    def set_thresh_hold_slider(self):
        """
        This function is used to set the threshold value
        :return:
        """
        slider_pixel = Read_Visitor_Search_Components().slider_value_data_input()
        slider_pixel_value = int(slider_pixel)

        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().slider_icon_by_xpath())
        action = ActionChains(self.d)
        action.drag_and_drop_by_offset(slider, -200, 0).perform()
        time.sleep(2)
        action.drag_and_drop_by_offset(slider, slider_pixel_value, 0).perform()
        time.sleep(2)

    def select_count(self, count_data):
        """
        This function is used to select the count from the count dropdown
        :param count_data:
        :return:
        """
        max_match = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().max_of_matches_by_xpath())
        select = Select(max_match)

        select.select_by_visible_text(count_data)

    def click_on_submit_search_button(self):
        """
        This function is used to click on the submit search button
        :return:
        """
        submit_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().submit_search_button_by_xpath())
        submit_btn.click()

    def verify_gender_match_list(self, expected_gender):
        """
        This function is used to the verify te gender with the actual match list
        :param expected_gender:
        :return:
        """
        match_gender_list = self.d.find_elements(By.XPATH,
                                                 Read_Visitor_Search_Components().matches_gender_by_xpath())
        for ele in match_gender_list:
            gender = ele.text
            print(gender)
            if expected_gender.upper() not in gender:
                assert False

    def select_gender(self, gender_data):
        """
        This function helps us to select the gender dropdown
        :return:
        """
        gender_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().select_gender_by_xpath())

        s = Select(gender_ele)
        s.select_by_value(gender_data)

    def refresh_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the match has been found
        :return:
        """
        while True:
            try:
                refresh_icon = self.d.find_element(By.XPATH,
                                                   Read_Visitor_Search_Components().refresh_icon_by_xpath())
                if not (refresh_icon.is_displayed()):
                    break

            except Exception as e:
                time.sleep(10)

    def add_image_search(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        element = WebDriverWait(self.d, 3000)
        Visitor_Search_Module_pom().login_before()
        upload_photo = self.d.find_element(By.XPATH,
                                           Read_Visitor_Search_Components().photo_upload_container_by_xpath())
        upload_photo.click()
        time.sleep(2)
        file_path = 'D:\Chrome_Download\img1.png'
        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')

        configure_search = self.d.find_element(By.XPATH,
                                               Read_Visitor_Search_Components().configure_search_by_xpath())
        configure_search.click()

    def compare_count_match(self, count_data):
        """
        This function is used to compare the count provided with the actual no. of match count
        :param count_data:
        :return:
        """
        match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().matches_found_by_xpath())
        match_found_count = int(match_found.text)

        match_found_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().matches_list_by_xpath())
        match_found_list_count = len(match_found_list)
        match int(count_data):
            case 1:
                assert match_found_count == 1

            case 5:
                if 0 < match_found_count and match_found_list_count <= 5:
                    print("match found count ===> ", match_found_count)
                    assert True

                else:
                    print("match found count ===> ", match_found_count)
                    assert False
            case 10:
                if 0 < match_found_count and match_found_list_count <= 10:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case 15:
                if 0 < match_found_count and match_found_list_count <= 15:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case 20:
                if 0 < match_found_count and match_found_list_count <= 20:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case 25:
                if 0 < match_found_count and match_found_list_count <= 25:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case 30:
                if 0 < match_found_count and match_found_list_count <= 30:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case 35:
                if 0 < match_found_count and match_found_list_count <= 35:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case 40:
                if 0 < match_found_count and match_found_list_count <= 40:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case 45:
                if 0 < match_found_count and match_found_list_count <= 45:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case 50:
                if 0 < match_found_count and match_found_list_count <= 50:
                    print("match found count ===> ", match_found_count)
                    assert True
                else:
                    print("match found count ===> ", match_found_count)
                    assert False

            case _:
                print("enter a valid count====> ")
                assert False

    def click_on_logout_button(self):
        """
        This function is used to logout
        :return:
        """
        time.sleep(Base_Class.one_second)
        logout_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().logout_button())
        logout_button.click()

    def close_all_panel_one_by_one(self):
        """
        This function is used to close all panel one by one
        :return:
        """
        time.sleep(Base_Class.one_second)
        close_panel = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().close_all_panel_list_by_xpath())
        for i in close_panel :
            i.click()


