#!/usr/bin/env python
# coding: utf-8

# In[2]:


from enum import Enum

class RobotStatus(Enum):
    IDLE = "Idle" 
    WORKING = "Working"
    CHARGING = "Charging"
    
class LeggedRobotStatus(Enum):
    SIT = "Sitting down"
    STAND_UP = "Standing up and balancing"


# In[3]:


# 기본 Robot 클래스
class Robot:
    ALLOWED_STATUSES = {RobotStatus.IDLE, RobotStatus.WORKING}  # 기본 허용 상태

    def __init__(self, robot_id: str, name: str, model: str):
        self.robot_id = robot_id
        self.name = name
        self.model = model
        self.status = RobotStatus.IDLE

    def set_status(self, new_status: RobotStatus) -> None:
        """로봇의 상태를 안전하게 변경"""
        if new_status not in self.ALLOWED_STATUSES:
            print(f"[ERROR] {new_status.value} is not a valid status for {self.__class__.__name__}.")
            return
        self.status = new_status
        print(f"{self.name} status changed to {self.status.value}.")

    def operate(self) -> None:
        """기본 로봇은 작업 수행 기능이 없음"""
        print(f"{self.name} has no specific operation.")

    def get_info(self) -> str:
        return f"Robot<{self.robot_id}> [{self.name}] (Model={self.model}), Status={self.status.value}"


# In[4]:


class MobileRobot(Robot):
    ALLOWED_STATUSES = {RobotStatus.IDLE, RobotStatus.WORKING, RobotStatus.CHARGING}  # 모든 상태 허용

    def __init__(self, robot_id: str, name: str, model: str, x=0.0, y=0.0, speed=0.0):
        super().__init__(robot_id, name, model)
        self.battery = 100
        self.x, self.y, self.speed = x, y, speed

    def charge(self) -> None:
        self.set_status(RobotStatus.CHARGING)
        self.battery = 100
        print(f"{self.name} is fully charged.")
        self.set_status(RobotStatus.IDLE)

    def move(self, dx: float, dy: float) -> None:
        distance = abs(dx) + abs(dy)
        battery_cost = int(distance * 2)
        if self.battery < battery_cost:
            print(f"[WARN] {self.name} has insufficient battery ({self.battery}%).")
            return
        self.x += dx
        self.y += dy
        self.battery -= battery_cost
        print(f"{self.name} moved to ({self.x}, {self.y}). Battery={self.battery}%")

    def operate(self) -> None:
        """이동 로봇의 기본 동작: 이동"""
        print(f"{self.name} is patrolling its designated area.")

    def get_info(self) -> str:
        return f"{super().get_info()}, Battery={self.battery}%, Speed={self.speed}, Pos=({self.x}, {self.y})"

# 다리로 이동하는 로봇 (LeggedRobot)
class LeggedRobot(MobileRobot):
    def __init__(self, robot_id: str, name: str, model: str, legs: int):
        super().__init__(robot_id, name, model)
        self.legs = legs
        self.leg_status = LeggedRobotStatus.SIT  # 기본 상태

    def get_current_status(self) -> str:
        return f"{self.name} is currently {self.leg_status.value}."

    def set_leg_status(self, new_status: LeggedRobotStatus) -> None:
        if not isinstance(new_status, LeggedRobotStatus):
            print(f"[ERROR] Invalid status: {new_status}")
            return
        self.leg_status = new_status
        print(f"{self.name} status changed to {self.leg_status.value}.")

    def stand_up(self) -> None:
        self.set_leg_status(LeggedRobotStatus.STAND_UP)

    def sit_down(self) -> None:
        self.set_leg_status(LeggedRobotStatus.SIT)

    def operate(self) -> None:
        """legged 로봇은 장애물 넘기 같은 동작을 수행"""
        print(f"{self.name} is jumping over obstacles.")

    def get_info(self) -> str:
        return f"{super().get_info()}, Legs={self.legs}, LegStatus={self.leg_status.value}"

# 드론 (Drone)
class Drone(MobileRobot):
    def __init__(self, robot_id: str, name: str, model: str, altitude=0.0):
        super().__init__(robot_id, name, model)
        self.altitude = altitude

    def move_3d(self, dx: float, dy: float, dz: float) -> None:
        """드론은 3D 이동이 가능 (x, y, z 축 이동)"""
        self.move(dx, dy)
        if dz and self.battery >= abs(dz) * 3:
            self.altitude += dz
            self.battery -= abs(dz) * 3
            print(f"{self.name} altitude changed to {self.altitude} m. Battery={self.battery}%")
        else:
            print(f"[WARN] {self.name} has insufficient battery for altitude change.")

    def operate(self) -> None:
        """드론의 기본 동작: 공중 정찰"""
        print(f"{self.name} is performing an aerial survey.")

    def get_info(self) -> str:
        return f"{super().get_info()}, Altitude={self.altitude}m"



# In[5]:


# 조작 가능한 로봇 (ManipulatorRobot)
class ManipulatorRobot(Robot):
    ALLOWED_STATUSES = {RobotStatus.IDLE, RobotStatus.WORKING}  # CHARGING 제외

    def __init__(self, robot_id: str, name: str, model: str):
        super().__init__(robot_id, name, model)
        self.power_on = False

    def power_up(self) -> None:
        self.power_on = True
        print(f"{self.name} power ON.")

    def power_down(self) -> None:
        self.power_on = False
        print(f"{self.name} power OFF.")

    def operate(self) -> None:
        """조작 로봇의 기본 동작: 조립 작업"""
        if self.power_on:
            print(f"{self.name} is assembling components.")
        else:
            print(f"[ERROR] {self.name} is OFF.")

    def get_info(self) -> str:
        return f"{super().get_info()}, PowerOn={self.power_on}"

# 협동 로봇 (Cobot)
class Cobot(ManipulatorRobot):
    def __init__(self, robot_id: str, name: str, model: str, joint_count=4):
        super().__init__(robot_id, name, model)
        self.joint_angles = [0.0] * joint_count

    def move_joint(self, joint_idx: int, angle: float) -> None: 
        if 0 <= joint_idx < len(self.joint_angles):
            self.joint_angles[joint_idx] = angle
            print(f"{self.name} joint[{joint_idx}] moved to {angle}°.")
        else:
            print(f"[ERROR] Invalid joint index {joint_idx}.")

    def operate(self) -> None:
        """협동 로봇의 동작: 작업자 지원"""
        if self.power_on:
            print(f"{self.name} assisting human workers.")
        else:
            print(f"[ERROR] {self.name} is OFF.")

# 직교 좌표계 로봇 (CartesianRobot)
class CartesianRobot(ManipulatorRobot):
    def __init__(self, robot_id: str, name: str, model: str):
        super().__init__(robot_id, name, model)
        self.head_position = [0.0, 0.0, 0.0]  # x, y, z

    def move_head(self, dx: float, dy: float, dz: float) -> None:
        if self.power_on:
            self.head_position = [self.head_position[i] + d for i, d in enumerate([dx, dy, dz])]
            print(f"{self.name} head moved to {self.head_position}.")
        else:
            print(f"[ERROR] {self.name} is OFF.")

    def operate(self) -> None:
        """직교 로봇의 동작: 정밀 위치 작업"""
        if self.power_on:
            print(f"{self.name} precisely positioning objects.")
        else:
            print(f"[ERROR] {self.name} is OFF.")


# In[11]:


drone = Drone("D001", "SkyBot", "X200", altitude=10.0)
print(drone.get_info())  
# SkyBot is at Altitude=10m



# In[12]:


drone.move_3d(5, 5, 2)
# SkyBot moved to (5, 5). Battery=90%
# SkyBot altitude changed to 12 m. Battery=84%



# In[13]:


drone.operate()
# SkyBot is performing an aerial survey.

