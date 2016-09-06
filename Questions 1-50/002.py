# Problem 2
# 5th Sep 2016
# Python 2

x = 0 # The previous number
y = 1 # The current number

ans = []

while x <= 4000000:
  if x % 2 == 0:
    ans.append(x)
  x, y = y, y + x

print(sum(ans))
    
