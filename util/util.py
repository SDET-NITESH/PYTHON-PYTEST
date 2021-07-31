"""
utility methods common across each module
"""

import os
import configparser
import pandas as pd
import json
import allure
import requests
import warnings
from ratelimit import limits, sleep_and_retry
from itertools import  zip_longest
from urllib3.exceptions import  InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
fileDir = os.path.dirname(os.path.realpath(__file__))
MAX_CALLS = 5
MAX_TIME = 60
MAX_CALLS_DAY = 500
MAX_TIME_DAY = 86400

ref_query_param = '["?","&","&","&"]'
ref_query_value = '["=","=","=","="]'

def get_config_value(param):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    CONFIG_PATH = os.path.join(fileDir,'../config.ini')
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    url = config.get('environment_config', param)
    return url



def sorted_collection_data(input_data_sorting,sorted_parameter):
    """
    :param input_data_sorting:
    :param sorted_parameter:
    :return:
    """
    sorted_data = sorted(input_data_sorting, key=lambda k: k[sorted_parameter])
    return sorted_data

@sleep_and_retry
@limits(calls=MAX_CALLS, period=MAX_TIME)
@limits(calls=MAX_CALLS_DAY, period=MAX_TIME_DAY)
def get_request(endpoint, cookie_value =None, headers=None, **kwargs):
    """
     method send the get request endpoint with multiple query parameters, it can include valid values or invalid values
    :param endpoint: end point of the get request of various apis
    :param kwargs: kwargs include the query parameter (example query_param=param_value, query_param_statuscode=statusCodeValue)
    :return: returns the response from the server
    """
    new_param = {}
    for key,value in kwargs.items():
        new_param.update({key:value})
    response = requests.get(endpoint, cookies=cookie_value, headers= headers, params=new_param, verify=False)
    return response



def capture_log(expected_value, *argv):
    """
    :param expected_value:
    :return:
    """
    for args in argv:
        allure.attach(str(expected_value), args)



def capture_log_pretty_json(expected_value, *argv):
    """
    :param expected_value:
    :return:
    """
    for args in argv:
        parsed = json.loads((expected_value))
        allure.attach(json.dumps(parsed,indent=4), args)




def generate_url_with_query_data(query_param, query_value):
    """

    :param query_param:List of query parameter names that needs to be used along with url converted to string .

    :type query_param: str

    :param query_value: List of query parameter values that needs to be used along with url converted to string .

    :type query_value: str

    :param ref_query_param: List of all reference  query parameter names  that needs to be used along with url converted to string .

    :type ref_query_param: str

    :param ref_query_value: List of all reference  query parameter values  that needs to be used along with url converted to string .

    :type ref_query_value: str

    :return: Concatenated string to be used along with url to search the get data with different query data
    """
    query_param_data  = query_param.strip("'[]'").replace('"', "").split(",")
    query_value_data = query_value.strip("'[]'").replace('"', "").split(",")
    ref_query_param_data = ref_query_param.strip("'[]'").replace('"', "").split(",")
    ref_query_value_data = ref_query_value.strip("'[]'").replace('"', "").split(",")
    return ''.join((z + x + w + y) for (x, y, z, w) in zip(query_param_data, query_value_data, ref_query_param_data, ref_query_value_data))

def generate_query_data(query_param, query_value):
  query_param_data = query_param.strip("'[]'").replace('"', "").split(",")
  query_param_value = query_value.strip("'[]'").replace('"', "").split(",")
  query_data = {}
  for (query_param, query_value) in zip_longest(query_param_data, query_param_value):
    query_data.update({query_param: query_value})
  return query_data

def convert_excel_dict(excel_file, collection_name, converters=None):
    """
    :param excel_file:
    :param collection_name:
    :return:
    """
    # data_set = (pd.read_excel(excel_file, sheet_name=collection_name, dtype=str, converters=converters))
    data_set = (pd.read_excel(excel_file, sheet_name=collection_name,  converters =converters))
    data_frame = data_set.set_index('Sl.no').T.to_dict('dict')
    return data_frame

def pick_required_data(conversion_data, unique_value, input_name):
    """

    :param unique_value:
    :param input_name:
    :return:
    """
    expected_list = []
    for key, value in conversion_data.items():
        if unique_value in value.values():
            value.pop(input_name)
            expected_list.append(value)
    consolidated_list = json.dumps(expected_list)
    return consolidated_list








