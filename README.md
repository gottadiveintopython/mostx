# Mostx : Quiz Generator

Generates the following quiz.

```text
B is slower than A
A is faster than C
B is faster than C
Which is the slowest one?
```

Supports multiple languages.  
(Japanese, Korean, Traditional-Chinese, English, )

## Installation

```
pip install --pre mostx
```

## Usage

```python
import mostx

print(sorted(mostx.get_available_langs()))
# => ['chinese', 'english', 'japanese', 'korean', ]

qgen = mostx.QuizGenerator(lang='english')
quiz = qgen(choices='ABC', n_adjs=1)
print(quiz)
# Quiz(
#     statements=[
#         'C is larger than A',
#         'A is smaller than B',
#         'C is larger than B',
#     ],
#     question='Which is the smallest?',
#     choices=('A', 'B', 'C'),
#     answer='A'
# )
```

## etc

[Google App](https://play.google.com/store/apps/details?id=jp.gottadiveintopython.mostx) (Mostx + Kivy)
