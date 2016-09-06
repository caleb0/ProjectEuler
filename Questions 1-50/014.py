# Problem 14
# 6 Sep 2016
# Python 2 and hella slow
def iterate(n):
  ans = 0
  num = n
  while True:
    if num == 1:
      return ans+1
    
    elif num%2==0:
      num //= 2
    else:
      num = num*3 +1
    ans += 1
    
big = 0
ans = 0
for x in xrange(1, 1000000):
  a = iterate(x)
  if a > big:
    big = a
    ans = x
    
print(ans)
