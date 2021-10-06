from setuptools import setup, find_packages

setup(name='dymanic_load',
      version='0.0.1',
      url='https://github.com/benjamin-jin/python-dynamic-exeuction', # 프로젝트 주소
      author='Benjamin Jin', # 작성자
      author_email='jinrudals135@naver.com', # 작성자 이메일
      description='Load module, function from string', # 간단한 설명
      packages=find_packages(exclude=['']),  # 기본 프로젝트 폴더 외에 추가로 입력할 폴더
      long_description=open('README.md').read(), # 프로젝트 설명, 보통 README.md로 관리
      install_requires=[''], # 설치시 설치할 라이브러리
)