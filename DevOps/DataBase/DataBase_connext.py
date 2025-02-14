import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",             # MySQL 서버 주소 (로컬 서버: 'localhost')
    user="root",                  # MySQL 사용자명
    password="0526",                 # MySQL 비밀번호
    database="causw",         # 사용할 데이터베이스 이름
    charset='utf8mb4',            # UTF-8 확장 버전 (이모지 등도 지원)
    cursorclass=pymysql.cursors.DictCursor  # SQL 결과를 딕셔너리 형태로 반환
)

# 커서 객체 생성
cursor = conn.cursor()

# 현재 선택된 데이터베이스 확인
cursor.execute("SELECT DATABASE()")
print("현재 데이터베이스:", cursor.fetchone())  # 조회된 데이터 출력
cursor.execute("SELECT * FROM room")
rooms = cursor.fetchall() #SQL 결과의 모든 행을 리스트 형태로 반환, 각 행은 딕셔너리 또는 튜플로 반환
for room in rooms:
    print(room)

# 연결 종료
conn.close()
