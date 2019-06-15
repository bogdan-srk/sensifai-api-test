from sensifai import SensifaiApi
from pprint import pprint

import json

token = 'E16A089A586A48418453B14787DF6F1C'
sensifai_api = SensifaiApi(token)
#
#
# files_list = ['/Users/bogdan/PycharmProjects/sensifai-test/10sec New York City .mp4']
# task_dict = sensifai_api.start_model(files=files_list)
#
#
# print(json.dumps(task_dict, indent = 4))
#
# for id in task_dict["succeed"]:
#     result = sensifai_api.get_result(id["taskId"])
#     pprint(id["file"])
#     JSON_FILE_PATH = "/Users/bogdan/PycharmProjects/sensifai-test/{}-result.json".format(id["file"])
#     json.dump(result, open(JSON_FILE_PATH, 'w'))
#     pprint(result)
#     pprint("_____________________________")

task_dict = {
    "succeed": [
        {
            "file": "10sec New York City .mp4",
            "taskId": "497eacfd-8431-4bea-8f19-50a435977777"
        }
    ],
    "cannotUpload": []
}
for id in task_dict["succeed"]:
    result = sensifai_api.get_result(id["taskId"])
    pprint(id["file"])
    JSON_FILE_PATH = "/Users/bogdan/PycharmProjects/sensifai-test/{}-result.json".format(id["file"])
    json.dump(result, open(JSON_FILE_PATH, 'w'))
    pprint(result)
    pprint("_____________________________")