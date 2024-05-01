import time

from selenium.webdriver.common.by import By

from profiles.prodprofile import ProdProfile
from utilities.element_interactions import ElementInteractions
from pages.user import PageUser
from pages.test_sequence import PageTestSequence
from pages.user_yoga_sequence import PageUserYogaSequence
from keywords.login import LogIn
from test_data.sequence_data import SequenceData


class TestSequenceFlow:
    def test_login(self, driver):
        sequence_name = 'Test Sequence'

        # Steps to log in
        LogIn.log_in(driver, ProdProfile.username, ProdProfile.password)

        # Click on builder tab
        ElementInteractions.click_object(driver, PageUser.a_builder)

        # Enter sequence name
        ElementInteractions.input_text(driver, PageUser.input_sequence_title, sequence_name)

        # Select 'Acro' from Yoga Type drop-down
        ElementInteractions.select_by_option_text(driver, PageUser.select_yoga_type, '1. Acro')

        # Click on Create Sequence button
        ElementInteractions.click_object(driver, PageUser.btn_create_sequence)

        # Select yoga poses as per data ( Excel can be used, but I have used dictionary due to time constraint)
        for pose in SequenceData.sequence1:
            img_pose = (By.XPATH, '//ul[@id="selectYogaSequencePoses"]//img[contains(@title,"(' + pose + ')")]')

            ElementInteractions.click_object(driver, img_pose)

        # Click on Save & Continue button
        ElementInteractions.click_object(driver, PageTestSequence.btn_save_and_continue)

        # verify the sequence name
        assert sequence_name == ElementInteractions.get_text(driver, PageUserYogaSequence.h1_sequence_title).strip()

        # verify the sequence
        for i in range(1, len(SequenceData.sequence1) + 1):
            p_pose_name = (By.XPATH, '(//*[@id="yogaSequenceList"]//p)[' + str(i) + ']')

            assert ElementInteractions.get_text(driver, p_pose_name).strip() == SequenceData.sequence1[i - 1]

