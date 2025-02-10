# import time

# def longtime_job():
#     print("job start")
#     time.sleep(1)  # 1초 지연
#     return "done"

# list_job = [longtime_job() for i in range(5)]  # 리스트 컴프리헨션 사용
# print(list_job[0])

import time

def longtime_job():
    print("job start")
    time.sleep(1)  # 1초 지연
    return "done"

list_job = (longtime_job() for i in range(5))  # ✅ 제너레이터 표현식 사용
for job in list_job:
    print(job)  # "job start"가 1초마다 출력됨 (총 5초 소요)
# print(next(list_job))  # 첫 번째 호출
# print(next(list_job))  # 두 번째 호출
#longtime_job()이 즉시 실행되지 않음 → next()를 호출할 때만 실행됨.
#시간이 오래 걸리는 작업을 한꺼번에 
#처리하기보다는 필요한 경우에만 호출하여 사용할 때 제너레이터가 유용