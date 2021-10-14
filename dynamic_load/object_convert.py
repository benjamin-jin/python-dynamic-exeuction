import inspect

from .tail_recursive import *

def dynamic_string(f):
  if(inspect.isbuiltin(f)):
    name = f.__name__
    def helper(string : str) -> str:
      p = re.compile(f"[a-z|A-Z]*\((.*{name})\)")
      functionName = p.findall(string)[0]
      return functionName

    @tail_call_optimized
    def recurive(frame):
      if f".{name}" in inspect.getframeinfo(frame).code_context[0]:
        return helper(inspect.getframeinfo(frame).code_context[0].replace("\n",""))
      else:
        return recurive(frame.f_back)
    return recurive(inspect.currentframe())
  else:
    return f"{f.__module__}.{f.__name__}"
