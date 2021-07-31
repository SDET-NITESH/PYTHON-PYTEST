"""Get Time Series Step Files"""

from proboscis import  asserts
import json
import jsonpath_rw_ext as jp
from jsoncompare import jsoncompare as json_comp
from parameterized import parameterized
from test_data.config import ITERATE_USER_LIST
from test_base.enviornment_setup import EnvironmentSetup
import allure
from util.util import get_request, get_config_value,generate_query_data,generate_url_with_query_data, capture_log, capture_log_pretty_json, convert_excel_dict,pick_required_data
from util.get_time_series_util import get_time_series_util as gtsu


"""URL for application"""
TIME_SERIES_DAILY_ENDPOINT = get_config_value('get_time_series_endpoint')


"""Test Data for application"""
TIME_SERIES_ERROR_MESSAGE = convert_excel_dict(gtsu.time_series_test_data_sheet, gtsu.TIME_SERIES_ERROR_MESSAGE_SHEET_NAME)


@allure.feature('GET-TIME_SERIES-API')
class TestRequest(EnvironmentSetup):


    @parameterized.expand(ITERATE_USER_LIST)
    def test_get_time_request(self, test_case_id, test_type, response_code, query_param, query_value):
        """

        :param test_case_id:
        :param test_type:
        :param response_code:
        :param query_param:
        :param query_value:
        :return:
        """
        allure.description(test_type)
        self.end_point = TIME_SERIES_DAILY_ENDPOINT
        self.query_param = query_param
        self.query_value = query_value
        self.log_endpoint = self.end_point + generate_url_with_query_data(query_param, query_value)
        capture_log(self.log_endpoint, "End point of the time series api with query data is")
        query_data = generate_query_data(self.query_param, self.query_value)
        try:
            self.response = get_request(self.end_point, **query_data)
        except Exception as e:
            print("Exception Occured ", e)
        capture_log_pretty_json(self.response.text, "Response messages of the request for ")
        capture_log(self.response.status_code,"Expected response code " + str(response_code) + " and actual response code " + str(self.response.status_code))
        asserts.assert_equal(self.response.status_code, int(response_code), "Expected and actual code should match")
        self.response = json.loads(self.response.text)
        for key, value in self.response.items():
            if key == "Error Message":
                self.response["Error"] = self.response.pop("Error Message")
                break
        actual_error_message = jp.match(gtsu.actual_error_message_json_path, self.response)
        if actual_error_message != "":
            self.expected_data = json.loads(
                pick_required_data(TIME_SERIES_ERROR_MESSAGE, test_case_id, "Test_Data_Reference"))
            self.expected_error_message = jp.match(gtsu.expected_error_message_json_path, self.expected_data)
            comp_result_error_message = json_comp._is_list_same(actual_error_message, self.expected_error_message, True)
            if comp_result_error_message is False:
                capture_log(comp_result_error_message, "Compare the Error message ")
                assert False
        else:
            pass



