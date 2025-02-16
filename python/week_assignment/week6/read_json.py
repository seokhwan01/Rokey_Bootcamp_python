import os
import json

json_file_path = os.path.join('c:/rokey/python/week_assignment/week6', 'config.json')

if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        print("JSON 파일의 내용을 출력합니다:")
        for key, value in data.items():
            print(f"{key}: {value}")
else:
    print(f"{json_file_path} 파일이 존재하지 않습니다.")
