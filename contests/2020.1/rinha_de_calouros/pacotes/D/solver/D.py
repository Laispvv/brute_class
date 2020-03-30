import math

mmc=4
for i in range(a):
    mmc=(mmc*v[i])//(math.gcd(mmc,v[i]))
res = 2020+mmc
minimo = 2020+b

while(res<minimo):
    res+=mmc
print(res)