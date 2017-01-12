import math

testnum = input()
testnum = int(testnum)
for i in range(testnum):
    x1,y1,r1,x2,y2,r2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    r1 = int(r1)
    r2 = int(r2)
    cnt = 0
    for x in range(-10000,10000):
        for y in range(-10000,10000):
            if (x-x1)**2 + (y-y1)**2 == r1**2 and (x-x2)**2 + (y-y2)**2 == r2**2:
                cnt += 1
                # print('({},{})'.format(x,y))

    print(cnt)
