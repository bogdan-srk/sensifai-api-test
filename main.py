from sensifai import SensifaiApi
from pprint import pprint

import json

token = 'E16A089A586A48418453B14787DF6F1C'
sensifai_api = SensifaiApi(token)


# files_list = ['/Users/bogdan/PycharmProjects/sensifai-test/video-sample-2.mp4']
# task_dict = sensifai_api.start_model(files=files_list)
#
#
# print(json.dumps(task_dict, indent = 4))
#
# # for id in task_dict["succeed"]:
# #     result = sensifai_api.get_result(id["taskId"])
# #     pprint(id["file"])
# #     JSON_FILE_PATH = "/Users/bogdan/PycharmProjects/sensifai-test/{}-result.json".format(id["file"])
# #     json.dump(result, open(JSON_FILE_PATH, 'w'))
# #     pprint(result)
# #     pprint("_____________________________")

task_dict = {
    "succeed": [
        {

            "file": "video-sample-2.mp4",
            "taskId": "85abc56c-4d57-408b-99cd-7845bd65bca8"
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