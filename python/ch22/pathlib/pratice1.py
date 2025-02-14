#1.특정 폴더 내 파일 확장자 별로 자동 분류
from pathlib import Path
def get_files(folder_path):
    folder=Path(folder_path)
    # for file in folder.iterdir():
    #     print(file)
    return [file for file in folder.iterdir() if file.is_file()]
        
#2. 특정 폴더 내의 파일을 확장자 별로 폴더를 생성하여 이동하는 함수를 작성하시오
def organize_files_by_extension(folder_path):
    folder=Path(folder_path)
    for file in get_files(folder):
        # print(file.suffix)
        extension=file.suffix[1:]# .제외하고 확장자만
        ext_folder=folder / extension
        ext_folder.mkdir(exist_ok=True) #확장자별 폴더 생성
        file.rename(ext_folder/file.name) #file.name = 이름만 추출
        print(f"파일 이동 완료 : {file.name} -> {ext_folder}")
if __name__=="__main__":
    source=r"C:\rokey\ch22\pathlib\files"
    organize_files_by_extension(source)