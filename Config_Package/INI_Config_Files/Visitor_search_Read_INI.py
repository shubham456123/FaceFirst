import configparser
from pathlib import Path


class Read_Visitor_Search_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI\\Visitor_Search.ini'
            print("dm url path: ", portal_menu_ini_file_path)
            print("File location: ", portal_menu_ini_file_path)
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def configure_search_by_xpath(self):
        try:
            configure_search_by_xpath = self.config.get("LOCATORS", "configure_search_by_xpath")
            print("configure_search_by_xpath: ", configure_search_by_xpath)
            return configure_search_by_xpath
        except Exception as ex:
            print("configure_search_by_xpath : ", ex)

    def re_select_photo_by_xpath(self):
        try:
            re_select_photo_by_xpath = self.config.get("LOCATORS", "re_select_photo_by_xpath")
            print("re_select_photo_by_xpath: ", re_select_photo_by_xpath)
            return re_select_photo_by_xpath
        except Exception as ex:
            print("re_select_photo_by_xpath : ", ex)

    def crop_photo_by_xpath(self):
        try:
            crop_photo_by_xpath = self.config.get("LOCATORS", "crop_photo_by_xpath")
            print("crop_photo_by_xpath: ", crop_photo_by_xpath)
            return crop_photo_by_xpath
        except Exception as ex:
            print("crop_photo_by_xpath : ", ex)

    def rotate_image_by_xpath(self):
        try:
            rotate_image_by_xpath = self.config.get("LOCATORS", "rotate_image_by_xpath")
            print("rotate_image_by_xpath: ", rotate_image_by_xpath)
            return rotate_image_by_xpath
        except Exception as ex:
            print("rotate_image_by_xpath : ", ex)

    def select_a_photo_validation_by_xpath(self):
        try:
            select_a_photo_validation_by_xpath = self.config.get("LOCATORS", "select_a_photo_validation_by_xpath")
            print("select_a_photo_validation_by_xpath: ", select_a_photo_validation_by_xpath)
            return select_a_photo_validation_by_xpath
        except Exception as ex:
            print("select_a_photo_validation_by_xpath : ", ex)

    def select_photo_instructions_by_xpath(self):
        try:
            select_photo_instructions_by_xpath = self.config.get("LOCATORS", "select_photo_instructions_by_xpath")
            print("select_photo_instructions_by_xpath: ", select_photo_instructions_by_xpath)
            return select_photo_instructions_by_xpath
        except Exception as ex:
            print("select_photo_instructions_by_xpath : ", ex)

    def photo_upload_container_by_xpath(self):
        try:
            photo_upload_container_by_xpath = self.config.get("LOCATORS", "photo_upload_container_by_xpath")
            print("photo_upload_container_by_xpath: ", photo_upload_container_by_xpath)
            return photo_upload_container_by_xpath
        except Exception as ex:
            print("photo_upload_container_by_xpath : ", ex)

    def search_button_panel_photo_validation_by_xpath(self):
        try:
            search_button_panel_photo_validation_by_xpath = self.config.get("LOCATORS", "search_button_panel_photo_validation_by_xpath")
            print("search_button_panel_photo_validation_by_xpath: ", search_button_panel_photo_validation_by_xpath)
            return search_button_panel_photo_validation_by_xpath
        except Exception as ex:
            print("search_button_panel_photo_validation_by_xpath : ", ex)

    def optional_constraints_to_narrow_search_text_validation_by_xpath(self):
        try:
            optional_constraints_to_narrow_search_text_validation_by_xpath = self.config.get("LOCATORS", "optional_constraints_to_narrow_search_text_validation_by_xpath")
            print("optional_constraints_to_narrow_search_text_validation_by_xpath: ", optional_constraints_to_narrow_search_text_validation_by_xpath)
            return optional_constraints_to_narrow_search_text_validation_by_xpath
        except Exception as ex:
            print("optional_constraints_to_narrow_search_text_validation_by_xpath : ", ex)

    def start_date_by_xpath(self):
        try:
            start_date_by_xpath = self.config.get("LOCATORS", "start_date_by_xpath")
            print("start_date_by_xpath: ", start_date_by_xpath)
            return start_date_by_xpath
        except Exception as ex:
            print("start_date_by_xpath : ", ex)

    def start_date_checkbox_by_xpath(self):
        try:
            start_date_checkbox_by_xpath = self.config.get("LOCATORS", "start_date_checkbox_by_xpath")
            print("start_date_checkbox_by_xpath: ", start_date_checkbox_by_xpath)
            return start_date_checkbox_by_xpath
        except Exception as ex:
            print("start_date_checkbox_by_xpath : ", ex)

    def end_date_by_xpath(self):
        try:
            end_date_by_xpath = self.config.get("LOCATORS", "end_date_by_xpath")
            print("end_date_by_xpath: ", end_date_by_xpath)
            return end_date_by_xpath
        except Exception as ex:
            print("end_date_by_xpath : ", ex)

    def end_date_checkbox_by_xpath(self):
        try:
            end_date_checkbox_by_xpath = self.config.get("LOCATORS", "end_date_checkbox_by_xpath")
            print("end_date_checkbox_by_xpath: ", end_date_checkbox_by_xpath)
            return end_date_checkbox_by_xpath
        except Exception as ex:
            print("end_date_checkbox_by_xpath : ", ex)

    def age_range_text_validation_by_xpath(self):
        try:
            age_range_text_validation_by_xpath = self.config.get("LOCATORS", "age_range_text_validation_by_xpath")
            print("age_range_text_validation_by_xpath: ", age_range_text_validation_by_xpath)
            return age_range_text_validation_by_xpath
        except Exception as ex:
            print("age_range_text_validation_by_xpath : ", ex)

    def start_age_by_xpath(self):
        try:
            start_age_by_xpath = self.config.get("LOCATORS", "start_age_by_xpath")
            print("start_age_by_xpath: ", start_age_by_xpath)
            return start_age_by_xpath
        except Exception as ex:
            print("start_age_by_xpath : ", ex)

    def end_age_by_xpath(self):
        try:
            end_age_by_xpath = self.config.get("LOCATORS", "end_age_by_xpath")
            print("end_age_by_xpath: ", end_age_by_xpath)
            return end_age_by_xpath
        except Exception as ex:
            print("end_age_by_xpath : ", ex)

    def select_gender_by_xpath(self):
        try:
            select_gender_by_xpath = self.config.get("LOCATORS", "select_gender_by_xpath")
            print("select_gender_by_xpath: ", select_gender_by_xpath)
            return select_gender_by_xpath
        except Exception as ex:
            print("select_gender_by_xpath : ", ex)

    def zone_by_xpath(self):
        try:
            zone_by_xpath = self.config.get("LOCATORS", "zone_by_xpath")
            print("zone_by_xpath: ", zone_by_xpath)
            return zone_by_xpath
        except Exception as ex:
            print("zone_by_xpath : ", ex)

    def threshold_slider_by_xpath(self):
        try:
            threshold_slider_by_xpath = self.config.get("LOCATORS", "threshold_slider_by_xpath")
            print("threshold_slider_by_xpath: ", threshold_slider_by_xpath)
            return threshold_slider_by_xpath
        except Exception as ex:
            print("threshold_slider_by_xpath : ", ex)

    def max_of_matches_by_xpath(self):
        try:
            max_of_matches_by_xpath = self.config.get("LOCATORS", "max_of_matches_by_xpath")
            print("max_of_matches_by_xpath: ", max_of_matches_by_xpath)
            return max_of_matches_by_xpath
        except Exception as ex:
            print("max_of_matches_by_xpath : ", ex)

    def sort_A_to_Z_by_xpath(self):
        try:
            sort_A_to_Z_by_xpath = self.config.get("LOCATORS", "sort_A_to_Z_by_xpath")
            print("sort_A_to_Z_by_xpath: ", sort_A_to_Z_by_xpath)
            return sort_A_to_Z_by_xpath
        except Exception as ex:
            print("sort_A_to_Z_by_xpath : ", ex)

    def sort_Z_to_A_by_xpath(self):
        try:
            sort_Z_to_A_by_xpath = self.config.get("LOCATORS", "sort_Z_to_A_by_xpath")
            print("sort_Z_to_A_by_xpath: ", sort_Z_to_A_by_xpath)
            return sort_Z_to_A_by_xpath
        except Exception as ex:
            print("sort_Z_to_A_by_xpath : ", ex)

    def clear_by_xpath(self):
        try:
            clear_by_xpath = self.config.get("LOCATORS", "clear_by_xpath")
            print("clear_by_xpath: ", clear_by_xpath)
            return clear_by_xpath
        except Exception as ex:
            print("clear_by_xpath : ", ex)

    def submit_search_button_by_xpath(self):
        try:
            submit_search_button_by_xpath_by_xpath = self.config.get("LOCATORS", "submit_search_button_by_xpath_by_xpath")
            print("submit_search_button_by_xpath_by_xpath: ", submit_search_button_by_xpath_by_xpath)
            return submit_search_button_by_xpath_by_xpath
        except Exception as ex:
            print("submit_search_button_by_xpath_by_xpath : ", ex)

    def search_result_validation_by_xpath(self):
        try:
            search_result_validation_by_xpath = self.config.get("LOCATORS", "search_result_validation_by_xpath")
            print("search_result_validation_by_xpath: ", search_result_validation_by_xpath)
            return search_result_validation_by_xpath
        except Exception as ex:
            print("search_result_validation_by_xpath : ", ex)

    def close_visitor_search_panel_by_xpath(self):
        try:
            close_visitor_search_panel_by_xpath = self.config.get("LOCATORS", "close_visitor_search_panel_by_xpath")
            print("close_visitor_search_panel_by_xpath: ", close_visitor_search_panel_by_xpath)
            return close_visitor_search_panel_by_xpath
        except Exception as ex:
            print("close_visitor_search_panel_by_xpath : ", ex)

    def submit_search_button_panel_by_xpath(self):
        try:
            submit_search_button_panel_by_xpath = self.config.get("LOCATORS", "submit_search_button_panel_by_xpath")
            print("submit_search_button_panel_by_xpath: ", submit_search_button_panel_by_xpath)
            return submit_search_button_panel_by_xpath
        except Exception as ex:
            print("submit_search_button_panel_by_xpath : ", ex)

    def visitor_search_result_panel_by_xpath(self):
        try:
            visitor_search_result_panel_by_xpath = self.config.get("LOCATORS", "visitor_search_result_panel_by_xpath")
            print("visitor_search_result_panel_by_xpath: ", visitor_search_result_panel_by_xpath)
            return visitor_search_result_panel_by_xpath
        except Exception as ex:
            print("visitor_search_result_panel_by_xpath : ", ex)

    def visitor_search_result_by_xpath(self):
        try:
            visitor_search_result_by_xpath = self.config.get("LOCATORS", "visitor_search_result_by_xpath")
            print("visitor_search_result_by_xpath: ", visitor_search_result_by_xpath)
            return visitor_search_result_by_xpath
        except Exception as ex:
            print("visitor_search_result_by_xpath : ", ex)

    def view_dropdown_by_xpath(self):
        try:
            view_dropdown_by_xpath = self.config.get("LOCATORS", "view_dropdown_by_xpath")
            print("view_dropdown_by_xpath: ", view_dropdown_by_xpath)
            return view_dropdown_by_xpath
        except Exception as ex:
            print("view_dropdown_by_xpath : ", ex)

    def view_drop_down_list_by_xpath(self):
        try:
            view_drop_down_list_by_xpath = self.config.get("LOCATORS", "view_drop_down_list_by_xpath")
            print("view_drop_down_list_by_xpath: ", view_drop_down_list_by_xpath)
            return view_drop_down_list_by_xpath
        except Exception as ex:
            print("view_drop_down_list_by_xpath : ", ex)

    def action_drop_down_by_xpath(self):
        try:
            action_drop_down_by_xpath = self.config.get("LOCATORS", "action_drop_down_by_xpath")
            print("action_drop_down_by_xpath: ", action_drop_down_by_xpath)
            return action_drop_down_by_xpath
        except Exception as ex:
            print("action_drop_down_by_xpath : ", ex)

    def action_drop_down_list_by_xpath(self):
        try:
            action_drop_down_list_by_xpath = self.config.get("LOCATORS", "action_drop_down_list_by_xpath")
            print("action_drop_down_list_by_xpath: ", action_drop_down_list_by_xpath)
            return action_drop_down_list_by_xpath
        except Exception as ex:
            print("action_drop_down_list_by_xpath : ", ex)

    def visitor_search_result_photo_by_xpath(self):
        try:
            visitor_search_result_photo_by_xpath = self.config.get("LOCATORS", "visitor_search_result_photo_by_xpath")
            print("visitor_search_result_photo_by_xpath: ", visitor_search_result_photo_by_xpath)
            return visitor_search_result_photo_by_xpath
        except Exception as ex:
            print("visitor_search_result_photo_by_xpath : ", ex)

    def visitor_search_complete_title_by_xpath(self):
        try:
            visitor_search_complete_title_by_xpath = self.config.get("LOCATORS", "visitor_search_complete_title_by_xpath")
            print("visitor_search_complete_title_by_xpath: ", visitor_search_complete_title_by_xpath)
            return visitor_search_complete_title_by_xpath
        except Exception as ex:
            print("visitor_search_complete_title_by_xpath : ", ex)

    def visitor_jobs_processed_heading_by_xpath(self):
        try:
            visitor_jobs_processed_heading_by_xpath = self.config.get("LOCATORS", "visitor_jobs_processed_heading_by_xpath")
            print("visitor_jobs_processed_heading_by_xpath: ", visitor_jobs_processed_heading_by_xpath)
            return visitor_jobs_processed_heading_by_xpath
        except Exception as ex:
            print("visitor_jobs_processed_heading_by_xpath : ", ex)

    def search_constraints_by_xpath(self):
        try:
            search_constraints_by_xpath = self.config.get("LOCATORS", "search_constraints_by_xpath")
            print("search_constraints_by_xpath: ", search_constraints_by_xpath)
            return search_constraints_by_xpath
        except Exception as ex:
            print("search_constraints_by_xpath : ", ex)

    def matches_found_by_xpath(self):
        try:
            matches_found_by_xpath = self.config.get("LOCATORS", "matches_found_by_xpath")
            print("matches_found_by_xpath: ", matches_found_by_xpath)
            return matches_found_by_xpath
        except Exception as ex:
            print("matches_found_by_xpath : ", ex)

    def matches_list_by_xpath(self):
        try:
            matches_list_by_xpath = self.config.get("LOCATORS", "matches_list_by_xpath")
            print("matches_list_by_xpath: ", matches_list_by_xpath)
            return matches_list_by_xpath
        except Exception as ex:
            print("matches_list_by_xpath : ", ex)

    def matches_count_data_input(self):
        try:
            matches_count_data_input = self.config.get("DATA", "matches_count_data_input")
            print("matches_count_data_input: ", matches_count_data_input)
            return matches_count_data_input
        except Exception as ex:
            print("matches_count_data_input : ", ex)

    def refresh_icon_by_xpath(self):
        try:
            refresh_icon_by_xpath = self.config.get("LOCATORS", "refresh_icon_by_xpath")
            print("refresh_icon_by_xpath: ", refresh_icon_by_xpath)
            return refresh_icon_by_xpath
        except Exception as ex:
            print("refresh_icon_by_xpath : ", ex)

    def slider_value_data_input(self):
        try:
            slider_value_data_input = self.config.get("DATA", "slider_value_data_input")
            print("slider_value_data_input: ", slider_value_data_input)
            return slider_value_data_input
        except Exception as ex:
            print("slider_value_data_input : ", ex)

    def score_by_xpath(self):
        try:
            score_by_xpath = self.config.get("LOCATORS", "score_by_xpath")
            print("score_by_xpath: ", score_by_xpath)
            return score_by_xpath
        except Exception as ex:
            print("score_by_xpath : ", ex)

    def matches_gender_by_xpath(self):
        try:
            matches_gender_by_xpath = self.config.get("LOCATORS", "matches_gender_by_xpath")
            print("matches_gender_by_xpath: ", matches_gender_by_xpath)
            return matches_gender_by_xpath
        except Exception as ex:
            print("matches_gender_by_xpath : ", ex)

    def gender_data_input(self):
        try:
            gender_data_input = self.config.get("DATA", "gender_data_input")
            print("gender_data_input: ", gender_data_input)
            return gender_data_input
        except Exception as ex:
            print("gender_data_input : ", ex)

    def slider_icon_by_xpath(self):
        try:
            slider_icon_by_xpath = self.config.get("LOCATORS", "slider_icon_by_xpath")
            print("slider_icon_by_xpath: ", slider_icon_by_xpath)
            return slider_icon_by_xpath
        except Exception as ex:
            print("slider_icon_by_xpath : ", ex)

    def start_age_data_input(self):
        try:
            start_age_data_input = self.config.get("DATA", "start_age_data_input")
            print("start_age_data_input: ", start_age_data_input)
            return start_age_data_input
        except Exception as ex:
            print("start_age_data_input : ", ex)

    def end_age_data_input(self):
        try:
            end_age_data_input = self.config.get("DATA", "end_age_data_input")
            print("end_age_data_input: ", end_age_data_input)
            return end_age_data_input
        except Exception as ex:
            print("end_age_data_input : ", ex)

    def logout_button(self):
        try:
            logout_btn_by_xpath = self.config.get("LOCATORS", "logout_btn_by_xpath")
            print("logout_btn_by_xpath: ", logout_btn_by_xpath)
            return logout_btn_by_xpath
        except Exception as ex:
            print("logout_btn_by_xpath : ", ex)

    def close_all_panel_list_by_xpath(self):
        try:
            close_all_panel_list_by_xpath = self.config.get("LOCATORS", "close_all_panel_list_by_xpath")
            print("close_all_panel_list_by_xpath: ", close_all_panel_list_by_xpath)
            return close_all_panel_list_by_xpath
        except Exception as ex:
            print("close_all_panel_list_by_xpath : ", ex)
