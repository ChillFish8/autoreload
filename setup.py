from setuptools import setup

setup(
    name='autoreload',
    version='1.0',
    description='Auto reloading web browser.',
    author='ChillFish8',
    author_email='hburt2003@gmail.com',
    requirements=[
        'selenium',
        'watchdog',
        'click',
    ],
 )