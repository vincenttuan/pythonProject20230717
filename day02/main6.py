# A點(10, 20) B點(-50, 30)
# 求二點間的距離 = ?
import math
print(math.pi)
print(math.e)
x1, y1 = 10, 20  # A 點
x2, y2 = -50, 30  # B 點
dx = math.pow(x1-x2, 2)
dy = math.pow(y1-y2, 2)
d = math.sqrt(dx + dy)
print("距離 %.1f" % d)

