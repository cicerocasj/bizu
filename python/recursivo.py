import sys
sys.setrecursionlimit(10000000)
import datetime as dt


def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper


@memoize
def fatorial(x):
    if x == 1:
        return x * 1
    return x * fatorial(x - 1)


@memoize
def fibonacci(x):
    if x < 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

print dt.datetime.now()
print fatorial(100)
print dt.datetime.now()
print fibonacci(100)
print dt.datetime.now()

# teste com o @memoize e sem!
