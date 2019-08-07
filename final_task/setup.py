from setuptools import setup, find_packages

setup(
    name='calculator',
    description='pure line-command calculator',
    version='build_ver:0.1',
    author='kirill vackevich',
    author_email='kirill.vackevich@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calc = pycalc:main',
        ]
    }
)