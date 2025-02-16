from tqdm import tqdm
import time

for i in tqdm(range(0, 101, 10), desc="Charging Percentage", leave=True):
    time.sleep(0.5)  # 0.5초 대기
    if i == 100:
        print("\nCharging completed")
