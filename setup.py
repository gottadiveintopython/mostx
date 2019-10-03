from setuptools import setup
from codecs import open
from os import path
import re


LONG_DESCRIPTION = r'''
```python
import mostx

print(sorted(mostx.get_available_langs()))
# => ['chinese', 'english', 'japanese', 'korean', ]

qgen = mostx.QuizGenerator(lang='english')
quiz = qgen.generate(choices='ABC', n_adjectives=1)
print(quiz)
# Quiz(
#     statements=[
#         'C is larger than A',
#         'A is smaller than B',
#         'C is larger than B'
#     ],
#     question='Which is the smallest?',
#     choices=('A', 'B', 'C'),
#     answer='A'
# )
```
'''


setup(
    name='mostx',
    packages=['mostx', 'mostx.langs'],
    version='0.1.1dev',
    license='MIT',
    install_requires=[],
    tests_require=['pytest', ],
    author='Nattōsai Mitō',
    author_email='flow4re2c@gmail.com',
    url='https://github.com/gottadiveintopython/mostx',
    description='Quiz Generator',
    long_description=LONG_DESCRIPTION,
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