from sensifai import SensifaiApi
from pprint import pprint

import json

token = 'E16A089A586A48418453B14787DF6F1C'
sensifai_api = SensifaiApi(token)


# files_list = [
#     '/Users/bogdan/PycharmProjects/sensifai-test/videos/10 sec New York.mp4',
#     '/Users/bogdan/PycharmProjects/sensifai-test/videos/video-sample-2.mp4'
# ]
# task_dict = sensifai_api.start_model(files=files_list)
# print(json.dumps(task_dict, indent = 4))


task_dict = {
    "succeed": [
        {
            "file": "10 sec New York.mp4",
            "taskId": "81a3b8a7-4659-4865-b1b1-fe7fe05c4fb0"
        },
        {
            "file": "video-sample-2.mp4",
            "taskId": "ec896b66-a388-42e8-b5d8-c478f44b8245"
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