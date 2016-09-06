# Problem 4
# 5th Sep 2016
# Python 2


ans = 0
for i in xrange(100, 1000):
  for j in xrange(100, 1000):
    num = i*j
    if str(num) == str(num)[::-1]:
      if num > ans:
        ans = num

print(ans)

