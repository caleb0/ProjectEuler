# Problem 7
# 5th September 2016
# Python 2


def isPrime(n):
  for i in range(2, int(n**0.5)+1):
    if (n % i ) == 0:
      return False
  return True

index = 1
num = 1
while index != 10001:
  if isPrime(num):
    index += 1
  num += 2
print(num)
