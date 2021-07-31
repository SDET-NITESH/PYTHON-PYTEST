"""Global variables defibed"""

ITERATE_USER_LIST = [("API_GTS_Valid_001", "Demonstrate that Get time Resource api returns data for given valid set of required data","200",
                      '["function","symbol","apikey"]','["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36"]'),
                     ("API_GTS_Valid_002",
                      "Demonstrate that Get time Resource api returns data for required and optional data", "200",
                      '["function","symbol","apikey","outputsize"]', '["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36","full"]'),
                    ("API_GTS_InValid_001",
                      "Validate get time series api returns error for invalid function value", "200",
                      '["function","symbol","apikey"]', '["TIME_SERIES","IBM","LVDWZYDOWUB07C36"]'),
                    ("API_GTS_InValid_002",
                      "Validate get time series api returns error for invalid function key", "200",
                      '["functi","symbol","apikey"]', '["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36"]'),
("API_GTS_InValid_003",
                      "Validate get time series api returns error for invalid symbol key", "200",
                      '["function","symb","apikey"]', '["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36"]'),
("API_GTS_InValid_004",
                      "Validate get time series api returns error for invalid apiKey key", "200",
                      '["function","symbol","apik"]', '["TIME_SERIES_DAILY","IBM","LVDWZYDOWUB07C36"]')

                     ]