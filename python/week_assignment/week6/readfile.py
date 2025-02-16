import os

config_file_path = os.path.join('c:/rokey/python/week_assignment/week6', 'config.ini')

config_data = {}
with open(config_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    if '=' in line:
        key, value = line.strip().split('=', 1)
        config_data[key.strip()] = value.strip()

for key, value in config_data.items():
    print(f"{key} = {value}")
