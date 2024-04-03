#    Author details for techsupport:
#        - Name: Joe Tan
#        - Email: joetkk@outlook.my
#        - Contact: 016-2010402
#        - Date: 2024-03-06
import datetime
import json
from typing import Dict

def write_json(json_obj: Dict, file_path_prefix: str = "output"):
    today = datetime.date.today().strftime("%Y%m%d")
    file_path = f"{file_path_prefix}/{today}.json"

    with open(file_path, 'a+') as json_file:
        json.dump(json_obj, json_file, indent=4)
        json_file.write(",")

    #print("writing file to: ", file_path)
    print("successfully logged to .json file")
    return file_path