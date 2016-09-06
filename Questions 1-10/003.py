# Problem 3
# 5th Sep 2016
# Python 2

def compute(n):
  i = 2
  factors = []
  while i**2 <= n:
    if n%i:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n > 1:
    factors.append(n)
  return factors

print(compute(600851475143)[-1])
