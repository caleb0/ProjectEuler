# Problem 5
# 5th Sep 2016
# Python 2

div = range(1, 21)
i = 20

def canDivide(n):
  for i in div:
    if n % i != 0:
      return False
  return True
ans = 0

while True:
  if canDivide(i):
    ans = i
    break
  i += 20
print(ans)
