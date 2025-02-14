from pathlib import Path  # pathlib 모듈의 Path 클래스 임포트

# 1. 현재 작업 디렉토리 확인
print("현재 작업 디렉토리:", Path.cwd())

# 2. 경로 생성 및 조작
folder = Path("example_folder")  # 경로 생성 (폴더 이름은 'example_folder')
file_path = folder / "file.txt"  # '/' 연산자를 사용해 경로 결합
print("결합된 경로:", file_path)

# 3. 디렉토리 및 파일 존재 여부 확인
# (1) 경로가 존재하는지 확인
print(f"{folder} 존재 여부:", folder.exists())  # 폴더 존재 여부 확인
print(f"{file_path} 존재 여부:", file_path.exists())  # 파일 존재 여부 확인

# (2) 해당 경로가 파일인지 확인
print(f"{file_path}은 파일인가요?:", file_path.is_file())

# (3) 해당 경로가 디렉토리인지 확인
print(f"{folder}은 디렉토리인가요?:", folder.is_dir())

# 4. 폴더가 존재하지 않으면 생성하기
if not folder.exists():
    folder.mkdir()  # 폴더 생성
    print(f"{folder} 폴더가 생성되었습니다.")
else:
    print(f"{folder} 폴더는 이미 존재합니다.")
