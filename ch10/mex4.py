class Cvalue:
    def __init__(self):
        self.lista = []  # ① 리스트 초기화

    def add(self, num):
        self.lista.append(num)  # ② 리스트에 숫자 추가

    def fprint(self):
        print(self.lista)  # 리스트 출력
def plus(a,b):
    print("mex4")
    print(__name__)
    c=a+b
    return c
if __name__=="__main__":
    p1 = Cvalue()  # ③ 객체 생성
    p1.add(4)  # ④ 리스트에 1 추가
    p1.add(5)  # 리스트에 2 추가
    p1.add(6)  # 리스트에 3 추가
    p1.fprint()  # 최종 리스트 출력
