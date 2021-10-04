import importlib
import sys
def execute(string : str) :
  def load_module(x : str, y1 : list = list()) :
    y = x.split(".")
    z0  = ".".join(y [:-1])
    z1 = y[-1]
    try:
      module = importlib.import_module(x)
      return (module, y1)
    except ModuleNotFoundError:
      return load_module(z0, [z1] + y1)
    except ValueError:
      sys.exit("Cannot resolve any module from {}".format(string))
  module, last = load_module(string)
  for each in last:
    module = getattr(module, each)
  return module
