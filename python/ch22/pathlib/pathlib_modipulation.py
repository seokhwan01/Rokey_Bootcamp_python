from pathlib import Path  # pathlib 모듈의 Path 클래스 사용

# 1. 디렉토리 생성 및 삭제
# 새로운 디렉토리 생성 (이미 존재해도 에러 발생 안 함)
path = Path("new_folder")
path.mkdir(exist_ok=True)
print(f"{path} 디렉토리가 생성되었습니다.")

# 생성된 디렉토리를 삭제
if path.exists():
    path.rmdir()  # 디렉토리 삭제 (단, 비어 있어야 삭제 가능)
    print(f"{path} 디렉토리가 삭제되었습니다.")
else:
    print(f"{path} 디렉토리가 존재하지 않습니다.")

# 2. 파일 생성 및 삭제
file_path = Path("test.txt")

# 빈 파일 생성
file_path.touch()
print(f"{file_path} 파일이 생성되었습니다.")

# 파일 삭제
if file_path.exists():
    file_path.unlink()  # 파일 삭제
    print(f"{file_path} 파일이 삭제되었습니다.")
else:
    print(f"{file_path} 파일이 존재하지 않습니다.")

# 3. 파일 및 폴더 목록 조회
# 현재 작업 디렉토리에서 파일 및 폴더 목록 조회
current_dir = Path.cwd()
print(f"\n현재 작업 디렉토리의 파일 및 폴더 목록 ({current_dir}):")
for item in current_dir.iterdir():
    print("  -", item)  # 각 파일 및 폴더의 경로 출력
