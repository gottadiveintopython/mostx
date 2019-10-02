from setuptools import setup
from codecs import open
from os import path
import re


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mostx',
    packages=['mostx', 'mostx.langs'],
    version='0.1.0',
    license='MIT',
    install_requires=[],
    tests_require=['pytest', ],
    author='Nattōsai Mitō',
    author_email='flow4re2c@gmail.com',
    url='https://github.com/gottadiveintopython/mostx',
    description='Quiz Generator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='Game, Quiz',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Education',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Education',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)