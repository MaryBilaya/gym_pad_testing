from pages.body_param_page import BodyParam
import allure
import pytest


@allure.feature('Body_parameters')
@pytest.mark.body_parameters
def test_add_weight_param_2_december(driver, login):
    body_param = BodyParam(driver)
    body_param.open_body_param_page()
    body_param.add_weight_param_2_december(value='74')
    assert body_param.check_pop_up_message_that_param_was_saved()
    assert body_param.check_that_weight_parameter_table_was_displayed()




