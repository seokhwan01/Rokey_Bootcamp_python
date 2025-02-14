import numpy as np
arr=np.array([1,2,3,4,5])
np.save(r'C:\rokey\ch19\numpy\array.npy',arr)
loaded_arr = np.load(r'C:\rokey\ch19\numpy\array.npy')
print(loaded_arr)