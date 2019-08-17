from setuptools import setup, find_packages

setup(
    name='pycalc',
    description='pure line-command calculator',
    version='ver:0.9',
    author='kirill vackevich',
    author_email='kirill.vackevich@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['pycalc = calculator.pycalc:main']
    }
)
