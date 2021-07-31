
"""
This file follows the unittest approach used in the test scripts, for launching the browser and setting the browser sizes
"""

import unittest



class EnvironmentSetup(unittest.TestCase):
    """
   This class follows the unittest approach used for launching the browser and setting the browser sizes which would inherited in other test scripts
    """

    def setUp(self):
        """
        launch the browsers based on the config file
        """
        print("Inside Setup process")






    def tearDown(self):
        """

        :return:
        """
        print("Inside tearDown process")

