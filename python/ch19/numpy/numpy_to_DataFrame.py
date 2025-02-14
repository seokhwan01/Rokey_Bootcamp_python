import numpy as np
import pandas as pd

# ✅ NumPy 배열 생성
arr = np.array([1, 2, 3, 4, 5])

# ✅ Pandas DataFrame으로 변환
df = pd.DataFrame(arr, columns=['Value'])

# ✅ 출력
print(df)
