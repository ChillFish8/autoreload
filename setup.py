from setuptools import setup

setup(
    name='autoreload',
    packages=['autoreload'],
    version='0.1.2',
    license='MIT',
    description='Watch your code live reload in the browser',
    author='CF8',
    author_email='hburt2003@gmail.com',
    url='https://github.com/ChillFish8/autoreload',
    download_url='https://github.com/ChillFish8/autoreload/archive/0.1.2.tar.gz',
    keywords=['live', 'auto', 'reloading', 'web development', 'web'],
    install_requires=[
        'selenium',
        'click',
        'watchdog'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
