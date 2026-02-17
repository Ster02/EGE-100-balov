from math import *

k = 1920 * 1080
i = 23

k2 = 1280 * 720
i2 = 21

e = (k * i) - (k2 * i2)
e2 = (e * 120) / (1024*8)
print(e2)