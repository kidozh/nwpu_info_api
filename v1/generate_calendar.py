# it's generating calendar python script
import json

with open("calendar.json","w") as file:
    jsonDict = dict()
    jsonDict = {
        "result":"ok",
        "calendar":[{
            "2017-2018":{
                "spring":{
                    "start":"20180226",
                    "end":"20180715"
                }
            },
            "2018-2019":{
                "fall":{
                    "start": "20180903",
                    "end":"20190120"
                },
                "spring":{
                    "start":"20190225",
                    "end":"20190714"
                }

            }
        }]
    }
    jsonDict["holiday"] = dict()
    # since this file was edit after 2018-6-12 there is no meaning to add other festival before
    jsonDict["holiday"] = {
        2018:{
            "festival":{
                "dragon_boat_festival":["20180618"],
                "mid_fall_festival":["20180924"],
                "national_day":["20181001","20181002","20181003","20181004","20181005","20181006","20181007"]
            },
            "workday":{
                "national_day":["20180929","20180930"]
            }
        }
    }
    json.dump(jsonDict,file)
    print(json.dumps(jsonDict))
