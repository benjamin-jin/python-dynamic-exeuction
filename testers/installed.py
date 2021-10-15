#!/bin/env python3
from dynamic_load import *
import inspect
@tail_call_optimized
def factorial(n, acc=1):
  "calculate a factorial"
  if n == 0:
    return acc
  return factorial(n-1, n*acc)

factorial(4)

try:
  @tail_call_optimized
  def fibo(n : int) -> int:
    if (n < 2):
      return 1
    else:
      return fibo(n-1) + fibo(n+2)
except NotTailRecursive:
  print("Expected Exception for non-tail-recursive function")
