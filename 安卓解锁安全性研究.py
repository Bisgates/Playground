from itertools import permutations
import time

t0 = time.time()

lis = []
p = [('13','2'),('17','4'),('19','5'),('28','5'),('31','2'),('37','5'),('39','6'),('46','5'),('64','5'),('71','4'),('73','5'),('79','8'),('82','5'),('97','8'),('91','5'),('93','6')]

for i in range(4,10):
    lis.append([''.join(x) for x in permutations('123456789',i)])

newList = []

for i in range(6):
  for ele in lis[i]:
    flag = True
    for pattern in p:
      if (pattern[0] in ele) and (ele.find(pattern[1],0,ele.find(pattern[0])) == -1):
        flag = False
    if flag == True:
      newList.append(ele)
        
print len(newList)

print time.time()-t0