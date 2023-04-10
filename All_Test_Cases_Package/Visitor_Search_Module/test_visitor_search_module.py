from pathlib import Path

import pytest

from All_POM_Package.Portal_Menu_Module.Portal_Menu_POM import Portal_Menu_pom
from All_POM_Package.Tags_Module.Tags_Module_POM import Tags_Module_pom
from All_POM_Package.Visitor_Search_Module.Visitor_Search_Module_POM import Visitor_Search_Module_pom
from All_Test_Cases_Package.conftest import Base_Class


class Test_Tags_Module(Base_Class):
    user_list = None
    results = list()

    def setup_method(self):
        try:
            print("\n setup start")
            self.d = Base_Class.d
            self.d.maximize_window()
            self.d.set_page_load_timeout(50)
            self.d.set_script_timeout(30)
            self.d.implicitly_wait(30)
            self.logger = Base_Class.logger_object()
            self.screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"
            print("\nsetup end")

        except Exception as ex:
            print("\nException in Test_Deployment_Manager_Test_Cases/setup_method: ", ex)

    @pytest.mark.p2
    def test_TC_VS_001(self):
        self.logger.info("test_TC_VS_001 execution started..")
        if Visitor_Search_Module_pom().visitor_search_with_only_match_count_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_001.png")
            assert False

    @pytest.mark.p2
    def test_TC_VS_002(self):
        self.logger.info("test_TC_VS_002 execution started..")
        if Visitor_Search_Module_pom().visitor_search_with_only_thresh_hold_search_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_002.png")
            assert False

    @pytest.mark.p2
    def test_TC_VS_003(self):
        self.logger.info("test_TC_VS_003 execution started..")
        if Visitor_Search_Module_pom().visitor_search_with_only_thresh_hold_and_count_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_003.png")
            assert False

    @pytest.mark.p2
    def test_TC_VS_004(self):
        self.logger.info("test_TC_VS_004 execution started..")
        if Visitor_Search_Module_pom().visitor_search_with_gender_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_004.png")
            assert False

    @pytest.mark.p2
    def test_TC_VS_005(self):
        self.logger.info("test_TC_VS_005 execution started..")
        if Visitor_Search_Module_pom().visitor_search_with_gender_and_count_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_005.png")
            assert False

    def test_TC_VS_006(self):
        self.logger.info("test_TC_VS_006 execution started..")
        if Visitor_Search_Module_pom().visitor_search_with_gender_and_score_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_006.png")
            assert False

    def test_TC_VS_007(self):
        self.logger.info("test_TC_VS_007 execution started..")
        if Visitor_Search_Module_pom().visitor_search_with_gender_count_and_score_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_007.png")
            assert False

    def test_TC_VS_008(self):
        self.logger.info("test_TC_VS_008 execution started..")
        if Visitor_Search_Module_pom().visitor_search_with_age_criteria():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_008.png")
            assert False


    def test_TC_VS_009(self):
        self.logger.info("test_TC_VS_008 execution started..")
        if Visitor_Search_Module_pom().calender_handle():
            assert True
        else:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_009.png")
            assert False