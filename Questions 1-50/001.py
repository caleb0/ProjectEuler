# Problem 1
# 5th Sep 2016
# Python 2

ans = [x for x in xrange(1, 1000) if x % 3 == 0 or x % 5 == 0]
print(sum(ans))

