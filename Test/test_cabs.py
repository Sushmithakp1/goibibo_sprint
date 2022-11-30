# import datetime
import time

import pytest
from Library import excel_lib
from POM.cabs_module import CabsModule
from Library import config

class TestCabsModule:

    data = excel_lib.read_data()

    @pytest.mark.parametrize("enter_from_textfield, enter_to_textfield, enter_pickup_location, enter_full_name, enter_mobile_number, enter_email", data)
    def test_valid_credentil(self, enter_from_textfield, enter_to_textfield, enter_pickup_location, enter_full_name, enter_mobile_number, enter_email, init_driver):
        driver = init_driver

        # try:
        cm = CabsModule(init_driver)
        cm.outstation_oneway_radio_button()
        cm.from_textfield(enter_from_textfield)
        cm.from_autosuggestion()
        cm.to_textfield(enter_to_textfield)
        cm.to_autosuggestion()
        cm.pickup_date()
        cm.select_date()
        cm.pickup_time()
        cm.select_time()
        cm.search_button()
        cm.select_cab()
        cm.pickup_location(enter_pickup_location)
        cm.location_autosuggestion()
        cm.full_name(enter_full_name)
        cm.mobile_number(enter_mobile_number)
        cm.email(enter_email)
        cm.paynow_radiobutton()
        cm.payment_button()

        # except BaseException as error_msg:
        #     td = datetime.datetime.now()
        #     name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        #     driver.save_screenshot(config.Config.SCREENSHOT_PATH + name)
        #     raise error_msg
