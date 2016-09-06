# Problem 6
# 5th Sep 2016
# Python 2


def sum_of_squares(n):
  ans = 0
  for i in xrange(1, n+1):
    ans += i**2
  return ans

def square_of_sum(n):
  ans = sum(range(1, n+1))**2
  return ans

print(square_of_sum(100) - sum_of_squares(100))
