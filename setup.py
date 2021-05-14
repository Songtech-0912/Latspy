from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='latspy',
    version='0.1.0',
    description='Latex to Sympy conversion',
    long_description=long_description,
    maintainer='Songtech-0912',
    url='https://github.com/Songtech-0912/Latspy',
    packages=find_packages(),
    license='MIT',
    install_requires=['antlr4-python3-runtime', 'sympy']
)
