from setuptools import setup, find_packages

setup(
    name='top_lists',
    version='1.0.0',
    description='workers to be used with celeryproject.org',
    author='Wikia Engineering',
    author_email='techteam-l@wikia-inc.com',
    install_requires=[
        'boto==2.28.0',
        'celery==3.1.10',
        'gevent==1.0',
        'hiredis==0.1.2',
        'librabbitmq==1.5.0',
        'paramiko==1.13.0',
        'PyMySQL==0.6.1',
        'pysolr==3.2.0',
        'PyYAML==3.11',
        'redis==2.9.1',
        'requests==2.3.0',
        'wikia.common.configparser==1.0.0'
    ],
    packages=find_packages()
)
