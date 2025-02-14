from pathlib import Path  # pathlib 모듈의 Path 클래스 사용

# 1. 파일 확장자 가져오기
file = "example.txt"
path = Path(file)
print("파일 확장자:", path.suffix)  # 출력: .txt

# 2. 파일 이름 변경 및 이동하기
# (1) 파일 생성 (만약 파일이 없으면 생성)
path.touch()
print(f"{path} 파일이 생성되었습니다.")

# (2) 이동할 위치와 새 이름 지정
destination = Path("new_folder/example.txt")

# (3) 이동할 폴더가 없으면 생성
destination.parent.mkdir(exist_ok=True)  # new_folder 폴더 생성 (이미 존재하면 무시)

# (4) 파일 이름 변경 및 이동
path.rename(destination)
print(f"{path} 파일이 {destination}로 이동 및 이름 변경되었습니다.")
