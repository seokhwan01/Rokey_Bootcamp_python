from collections import deque
dq = deque()
dq.append(1)
dq.append(2)
dq.appendleft(3)
print(dq)
dq.pop()
dq.popleft()
print(dq)