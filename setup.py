from setuptools import setup, find_packages

setup(
    name='top-lists',
    version='1.0.0',
    description='top list scrappers',
    author='Jacek Jursza',
    author_email='jj@jursza.net',
    install_requires=[
        'requests==2.3.0',
        'lxml==3.4.0'
    ],
    packages=find_packages()
)
