# import shutil

# # 1. 파일 복사 (기본 복사)
# shutil.copy("source.txt", "destination.txt")  
# # source.txt를 destination.txt로 복사합니다. (파일 내용만 복사)

# # 2. 메타데이터 유지하며 복사
# shutil.copy2("source.txt", "destination.txt")  
# # 메타데이터(생성 시간, 수정 시간 등)를 함께 복사합니다.

import shutil
# 디렉토리 전체 복사 (디렉토리 내부의 모든 파일 및 하위 디렉토리 포함)
shutil.copytree("source_dir", "destination_dir")
