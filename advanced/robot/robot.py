#!/usr/bin/env python
# coding: utf-8

# In[254]:


#물류창고
# #1000*1000 좌표 
#물류창고 충전소 : [[0,0],[100,100],[0,100],[100,0],[50,50]]
charging_station = [[0,0],[1000,1000],[0,1000],[1000,0],[500,500]]

#물류창고 재고
product={"apple" : [[15],[200,200]],#[수량 , 위치]
         "cup" : [[5],[200,205]],
         "laptop":[[2],[200,300]]
}

#물류창고 출고지
shipping_area={"A":[500,0],"B":[500,1000]}

####################################################
#드론 최대 반경 [1000,1000,1000] 왕복 6000 배터리 100환산 /65 6000/65 = 92
#드론 시작점
dron_home_base=[0,0,0]
# 객체들
objects = [
    {"name": "Car", "coordinates": (10, 10, 0)},
    {"name": "Person", "coordinates": (50, 50, 40)},
    {"name": "Dog", "coordinates": (200, 200, 200)}
]


# In[255]:


print(product.get("apple")[0][0])


# In[256]:


def close_Charging_Station(x,y):
    station_x=0
    station_y=0
    min=abs(x-charging_station[0][0])+abs(y-charging_station[0][1])
    for i in charging_station:
        if abs(x-i[0])+abs(y-i[1])<min:
            min=abs(x-i[0])+abs(y-i[1])
            station_x=i[0]
            station_y=i[1]
    return min/20,station_x,station_y


# In[257]:


print(close_Charging_Station(1,60))


# In[258]:


import numpy as np

def point_to_line_distance(A, B, P):
    """점 P와 직선 AB 사이의 최단 거리 계산 및 P가 구간 내에 있는지 확인"""
    A, B, P = np.array(A), np.array(B), np.array(P)
    AB = B - A
    AP = P - A

    # 점 P가 직선 AB의 구간 내에 있는지 확인
    t = np.dot(AP, AB) / np.dot(AB, AB)
    if 0 <= t <= 1:  # t가 0과 1 사이일 때만 유효
        cross_product = np.cross(AP, AB)
        distance = np.linalg.norm(cross_product) / np.linalg.norm(AB)
        return distance
    else:
        return None  # 구간 밖에 있는 경우

# 드론의 이동 경로 (시작점 A, 종료점 B)
# A = (0, 0, 0)
# B = (100, 100, 100)

# 객체들
objects = [
    {"name": "Car", "coordinates": (10, 10, 0)},
    {"name": "Person", "coordinates": (50, 50, 40)},
    {"name": "Dog", "coordinates": (200, 200, 200)}
]

def object_detect(A,B)->None:
    # 탐지 거리 임계값
    threshold_distance = 15.0
    # 각 객체와 직선 사이의 거리 측정 및 구간 내 확인
    for obj in objects:
        distance = point_to_line_distance(A, B, obj["coordinates"])
        if distance is not None and distance <= threshold_distance:
            print(f"{obj['name']} detected at {obj['coordinates']} (Distance: {distance:.2f})")
        else:
            print(f"{obj['name']} not detected.")
object_detect(A,B)


# In[259]:


from enum import Enum

class RobotStatus(Enum): #열거형 ex)status = RobotStatus.WORKING
    IDLE = "Idle" #대기 상태
    WORKING = "Working" #일 중
    CHARGING = "Charging" #충전 중
    MALFUNCTION="Malfunction" #고장
    LOW_BATTERY="Low_Battery" #배터리 10% 이하일 때는 배터리 부족 상태
    
class LeggedRobotStatus(Enum):
    SIT = "Sitting down"
    STAND_UP = "Standing up and balancing"
    LOW_BATTERY="Low_Battery" #배터리 10% 이하일 때는 배터리 부족 상태
    


# In[260]:


class Robot:
    ALLOWED_STATUSES = {RobotStatus.IDLE,RobotStatus.WORKING} #기본 허용 상태
    
    def __init__(self,robot_id:str, name : str, model : str):
        self.robot_id = robot_id
        self.name=name
        self.model=model
        self.status=RobotStatus.IDLE
    
    def set_status(self,new_status:RobotStatus) -> None:
        if new_status not in self.ALLOWED_STATUSES:
            print(f'"[ERROR] {new_status} is not valid status for {self.__class__.__name__}')
            #self.__class__.__name__를 사용하면 상속된 클래스에서도 올바른 클래스 이름 반환 가능
        self.status=new_status
        print(f"{self.name} status changed to {self.status.value}")
    
    def operate(self) -> None:
        """기본 로봇은 수행 작업 X"""
        print(f"{self.name} has no specific operation")
        
    def get_info(self)->str:
        return f"Robot<{self.robot_id}> [{self.name}] (Model = {self.model}) , Status={self.status.value}"
        


# In[261]:


r1=Robot("AB-123","KAI","car")
r1.set_status(RobotStatus.WORKING)
r1.operate()
print(r1.get_info())


# In[ ]:


class MobileRobot(Robot):
    ALLOWED_STATUSES = {RobotStatus.IDLE, RobotStatus.WORKING, RobotStatus.CHARGING,RobotStatus.LOW_BATTERY,RobotStatus.MALFUNCTION}  # 모든 상태 허용
    
    def __init__(self, robot_id: str, name: str, model: str, x=0.0, y=0.0, speed=0.0):
        super().__init__(robot_id,name,model)
        self.battery=100
        self.x, self.y, self.speed = x, y, speed
        
    def charge(self)-> None:
        self.set_status(RobotStatus.CHARGING)
        #배터리 1%당 충전 퍼센트 보여줌
        for i in range(int(self.battery),101):
            print(f"Charging Percentage : {i}")
            if i==100:
                print("Charging completed")
        self.battery=100
        self.set_status(RobotStatus.IDLE)
        
    def after_status_move(self)->str:
        """이동 후 상태"""
        return f"{self.name} moved to ({self.x}, {self.y}). Battery={self.battery}%"
    

    def calculator_cost(self,*args)->float: #언패킹 사용
        """배터리 코스트 계산"""
        distance=0
        for i in args:
            distance+=i
        battery_cost=distance/20
        return battery_cost

    def move(self, dx: float, dy: float)->None: #dx는 앞으로 몇, 좌표 아님
        self.x += dx
        self.y += dy
        self.battery -= self.calculator_cost(dx,dy)
        print(self.after_status_move())#이동 완료
        
        if self.status != RobotStatus.LOW_BATTERY and self.battery<=10:
            self.low_battery_action()
            return
        
    def low_battery_action(self):
        """물류창고 로봇만 적용, 드론은 적용 X"""
        self.set_status(RobotStatus.LOW_BATTERY)
        self.go_to_charging_station()
        
    def go_to_charging_station(self)->None:
        """충전소 이동 후 충전"""
        buffer,close_station_x,close_station_y=close_Charging_Station(self.x,self.y)    
        print(f"[WARN] {self.name} is LOW_BATTERY.")
        print(f"{self.name} moves to Charging_station : [{close_station_x},{close_station_y}]")
        battery_cost=int(abs(close_station_x-self.x)+abs(close_station_y-self.y))/20
        self.move(close_station_x-self.x,close_station_y-self.y)
        self.charge()
        
        
    def operate(self) -> None:
        """이동 로봇의 기본 동작: 이동"""
        self.set_status(RobotStatus.WORKING)
        print(f"{self.name} is patrolling its designated area.")
        self.set_status(RobotStatus.IDLE)
        
    def get_info(self) -> str:
        return f"{super().get_info()}, Battery={self.battery}%, Speed={self.speed}, Pos=({self.x}, {self.y})"


# In[263]:


m=MobileRobot("K190","HI-119","car",0,0,10)
print(m.get_info())
m.move(100,100)
m.move(100,100)
m.move(100,100)
m.move(100,100)
m.move(100,100)
m.move(100,100)
m.move(100,100)
m.move(100,100)
m.move(100,100)


# In[264]:


class WarehouseRobot(MobileRobot):#물류 창고 로봇
    def __init__(self, robot_id: str, name: str, model: str, x=0.0, y=0.0, speed=0.0):
        super().__init__(robot_id, name, model, x, y, speed)
        self.carrying_item = None  # 현재 운반 중인 물건
        
    def move(self, dx: float, dy: float)->None:#오버라이딩으로 조건 추가
        #이동 명령 + 제일 가까운 충전소까지 못가면 이동하면 안됨
        battery_cost=self.calculator_cost(abs(dx),abs(dy))
        if self.battery < battery_cost+close_Charging_Station(self.x+dx,self.y+dy)[0]: 
            print(close_Charging_Station(self.x,self.y))
            print(f"[WARN] {self.name} has insufficient battery ({self.battery}%).")
            return
        super().move(dx,dy)
        
        
    def pick_item(self,item:str)->None:
        print(product)
        if self.carrying_item is not None: #현재 들고 있는 물건이 있으면 
            print(f"[WARN] {self.name} is holding {self.carrying_item}")
            return
            
        if item in product:
            if product.get(item)[0][0]<=0: #재고가 없으면
                print(f"{item} is is out of stock.")
            else:
                self.carrying_item=item
                #product={"apple" : [[15],[200,200]],
                self.move(product[item][1][0]-self.x,product[item][1][1]-self.y)
                product[item][0][0] -= 1 #로봇이 픽업하면 재고 하나 제거
                print(f"{self.name} picked up {item}")
                print(product)
            
        else:
            print(f"{item} is not valid.")
        
    def move_to_shipping_area(self,target_shipping_area):
        if target_shipping_area in shipping_area: #유효한 출고지이면
            target_x,target_y=shipping_area.get(target_shipping_area)
            self.move(target_x-self.x,target_y-self.y)
            self.carrying_item=None
        else:
            print(f"{target_shipping_area} is not valid")
        
    def set_item_and_area(self, item: str, target_shipping_area: str)->None:
        """아이템과 배송지를 설정"""
        self.item = item
        self.target_shipping_area = target_shipping_area
        print(f"{self.name}: Item set to '{self.item}', Shipping area set to '{self.target_shipping_area}'.")

    def operate(self)->None:
        """물류창고 로봇 동작 : 물건 옮기기""" ##출고지 shipping_area=[[500,0],[500,1000]]
        self.set_status(RobotStatus.WORKING)
        self.pick_item(self.item)
        self.move_to_shipping_area(self.target_shipping_area)
        self.set_status(RobotStatus.IDLE)
        
    def get_info(self):
        return f"{super().get_info()} carring_item = {self.carrying_item}"
        



# In[265]:


r2=WarehouseRobot("ID-197","Ka1","H-1",speed=10)
r2.set_item_and_area("apple","A")
r2.operate()
r2.pick_item("cup")
print(r2.get_info())


# In[266]:


r2.move_to_shipping_area("B")
print(r2.get_info())


# In[267]:


r2.go_to_charging_station()


# In[268]:


class Drone(MobileRobot):#정찰 드론
    """정찰 임무 수행"""
    #충전은 거점에서만 가능
    
    def __init__(self, robot_id: str, name: str, model: str,x=0.0, y=0.0, speed=0.0,altitude=0.0):
        super().__init__(robot_id, name, model,x,y,speed)
        self.altitude = altitude
        
    def after_status_move(self)->str:
        #오버라이딩
        return f"{self.name} moved to ({self.x}, {self.y}, {self.altitude}). Battery={self.battery}%"
    
    def low_battery_action(self): #오버라이딩으로 충전소 안감
        #move메소드에서 self.low_BAttery_action 충전소 안가고 경고 출력만
        """드론일때는 배터리 경고만"""
        print(f"[WARN] {self.name} is LOW_BATTERY. Battery={self.battery}%")
        return 
    
    def move_3d(self, dx: float, dy: float, dz: float) -> None:
        #이동 거리 + 집까지 복귀 가능일때
        battery_cost=self.calculator_cost(abs(dx),abs(dy),abs(dz))
        if self.battery < battery_cost+self.calculator_cost(abs(self.x+dx),abs(self.y+dy),abs(self.altitude+dz)): #이동 후 복귀 불가
            print(f"[WARN] {self.name} has insufficient battery ({self.battery}%).")
            return
        self.altitude+=dz
        self.battery-=self.calculator_cost(abs(dz))
        self.move(dx,dy) 
        
    def target_location(self,target_x:float,target_y:float,target_z=float)->None:
        """정찰 목적지 설정""" 
        self.target_x=target_x
        self.target_y=target_y
        self.target_z=target_z

    def operate(self)->None:
        """"
        정찰 임무 수행
        3차원 직선 그려서 탐지 객체랑 거리 재서 일정 거리 미만 이면 탐지 성공
        직선그리기, 거리 재기 함수 필요 
        """
        self.set_status(RobotStatus.WORKING)
        A=[self.x,self.y,self.altitude]
        B=[self.target_x,self.target_y,self.target_z]
        self.move_3d(self.target_x-self.x,self.target_y-self.y,self.target_z-self.altitude)
        object_detect(A,B)
        print(f"{self.name} mission completed. return home")
        self.move_3d(0-self.x,0-self.y,0-self.altitude)
        self.set_status(RobotStatus.IDLE)
    
    def go_to_charging_station(self)->None:
        """충전소 이동 후 충전"""    
        print(f"{self.name} moves to Charging_station at home : [0,0,0]")
        self.move_3d(0-self.x,0-self.y,0-self.altitude)
        self.charge()

    
    def get_info(self)->str:
        return f"{super().get_info()}, Altitude = {self.altitude}"


# In[269]:


drone1=Drone("A123","my_Drone","DH-111",speed=10)
drone1.get_info()
drone1.target_location(200,200,500)
drone1.operate()
drone1.charge()


# In[270]:


print(r2.get_info())


# In[271]:


# 조작 가능한 로봇 (ManipulatorRobot)
class ManipulatorRobot(Robot):
    ALLOWED_STATUSES = {RobotStatus.IDLE, RobotStatus.WORKING}  # CHARGING 제외
    
    def __init__(self, robot_id : str, name : str, model : str):
        super().__init__(robot_id, name, model)
        self.power_on = False
    
    def power_up(self)->None:
        self.power_on=True
        print(f"{self.name} power ON.")
    
    def power_down(self)->None:
        self.power_on=False
        print(f"{self.name} power OFF.")
    
    def operate(self):
        if self.power_on:
            print(f"{self.name} is assembling components")
        else:
            print(f"[ERROR] {self.name} is OFF.")
    def get_info(self):
        return f"{super().get_info()}, PowerOn={self.power_on} "


# In[272]:


a=ManipulatorRobot("AB-123","KAI","H1")
a.power_up()
print(a.get_info())

