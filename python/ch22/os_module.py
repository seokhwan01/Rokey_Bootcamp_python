# import os  # os 모듈을 임포트 (운영 체제 관련 기능 사용)
# if os.path.exists("file.txt"): 
#     print("파일이 존재합니다.")

#os.rmdir("test_dir") 

#print("현재 작업 디렉토리:", os.getcwd())  # 현재 작업 디렉토리 출력
#print("디렉토리 목록:", os.listdir("."))

import os
folder = os.getcwd()  # 현재 작업 디렉토리 경로를 얻음
print("현재 작업 디렉토리:", folder)
os.chdir("./ch22")
print("현재 작업 디렉토리:", os.getcwd() )
# file_path = os.path.join(folder, "file.txt")
# print("파일 경로:", file_path)

# filename = os.path.basename(f"{folder}/file.txt")
# print("파일명:", filename)

# directory = os.path.dirname(f"{folder}/file.txt")
# print("디렉토리 경로:", directory)