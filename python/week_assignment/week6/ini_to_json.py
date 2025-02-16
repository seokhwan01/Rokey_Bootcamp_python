import os
import json

config_file_path = os.path.join('c:/rokey/python/week_assignment/week6', 'config.ini')
json_file_path = os.path.join('c:/rokey/python/week_assignment/week6', 'config.json')

config_dict = {}
if os.path.exists(config_file_path):
    with open(config_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config_dict[key.strip()] = value.strip()
else:
    print(f"{config_file_path} 파일이 존재하지 않습니다.")

with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(config_dict, json_file, ensure_ascii=False, indent=4)

print(f"config.ini의 내용이 {json_file_path}로 저장되었습니다.")
