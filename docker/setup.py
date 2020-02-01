#!/usr/local/bin/python3
from setuptools import setup

VERSION = '1.0'

install_requires = [
    'selenium==3.141.0',
    'pytest>=3.5.1',
    'pytest-rerunfailures>=4.1',
    'allure-pytest>=2.5.0',
    'allure-python-commons>=2.5.0'
]

def main():
    setup(
        name='selenium-docker-sample',
        version=VERSION,
        description='selenium + docker + python',
        author='yuta kuroki',
        url='https://github.com/ybkuroki/selenium-docker-sample',
        install_requires=install_requires
    )

if __name__ == '__main__':
    main()