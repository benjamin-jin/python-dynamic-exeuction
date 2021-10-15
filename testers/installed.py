from dynamic_load import *
import inspect
# @tail_call_optimized
def factorial(n, acc=1):
  "calculate a factorial"
  if n == 0:
    return acc
  return factorial(n-1, n*acc)
print(inspect.getsource(factorial))