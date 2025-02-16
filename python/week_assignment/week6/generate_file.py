import os
config_file_path = os.path.join('c:/rokey/python/week_assignment/week6', 'config.ini')

try:
    if not os.path.exists(config_file_path):
        with open(config_file_path, 'w', encoding='utf-8') as file:
            file.write("1반 = \n")
            file.write("2반 = \n")
            file.write("3반 = \n")
            file.write("4반 = \n")
        print(f"{config_file_path} 파일이 없어서 새로 생성했습니다.")
    else:
        config_data = {}
        with open(config_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line in lines:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config_data[key.strip()] = value.strip()

        for key, value in config_data.items():
            print(f"{key} = {value}")

except Exception as e:
    print(f"예외가 발생했습니다: {e}")
