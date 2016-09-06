# Problem 12
# 6th Sep 2016
# Python 2

def getdivisors(n):
    ans = 0
    for i in xrange(1, int(n**0.5)+1):
        if n%i == 0:
          ans += 2
    if n**0.5**2 == n:
      ans -= 1
    return ans

ans = 0
triangle = 1
res = 2
while True:
  ans = getdivisors(triangle)
  if ans > 500:
    print(triangle)
    break
  triangle += res
  res += 1

