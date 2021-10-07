from setuptools import setup, find_packages

setup(name='dymanic_load',
      version='0.0.1',
      url='https://github.com/benjamin-jin/python-dynamic-exeuction',
      author='Benjamin Jin',
      author_email='jinrudals135@naver.com',
      description='Load module, function from string',
      packages=find_packages(exclude=['']),
      long_description=open('REAMD.rst').read(),
      install_requires=[''],
)