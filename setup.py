from setuptools import find_packages, setup

APP_NAME = 'CarPrice'

def get_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith(('#','-'))]

setup(
    name=APP_NAME, 
    author='DeadlyHarbor', 
    author_email='aman07112006@gmail.com',
    version='1.0.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
