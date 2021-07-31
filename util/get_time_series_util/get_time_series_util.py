""" Parameters and method related to Time Series Module"""
import os
fileDir = os.path.dirname(os.path.realpath(__file__))



"""Excel Sheet Data"""
time_series_test_data_sheet= os.path.join(fileDir, '../../test_data/excel_template/GET_TIME_SERIES.xlsx')
TIME_SERIES_ERROR_MESSAGE_SHEET_NAME= 'TIME_SERIES_ERROR_MESSAGE'


"""Actual Json Path"""
actual_error_message_json_path = '$..Error'


"""Expected Json Path"""
expected_error_message_json_path = '$..message'