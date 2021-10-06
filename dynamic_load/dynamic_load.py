import importlib
import sys
class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)

def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated

def dynamic_load(string : str) :
  @tail_recursive
  def load_module(target : str, remained : list = list()) :
    try:
      module = importlib.import_module(target)
      return (module, remained)
    except ModuleNotFoundError:
      recurse(target=".".join(target.split(".")[:-1]), remained=[target.split(".")[-1]] + remained)
    except ValueError:
      sys.exit("Cannot resolve any module from {}".format(string))
  module, last = load_module(string)
  for each in last:
    module = getattr(module, each)
  return module