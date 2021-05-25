# Mostx : Quiz Generator

Generates the following types of quiz.

```text
# type-A
B is slower than A
A is faster than C
B is faster than C
Which is the slowest?

# type-B
B is slower than A
A is faster than C
B is faster than C
Put from slowest to fastest
```

Supports multiple languages.  
(Japanese, Korean, Traditional-Chinese, English, )

## Installation

```
pip install mostx
```

## Usage

```python
import mostx

print(sorted(mostx.get_available_langs()))
# => ['chinese', 'english', 'japanese', 'korean', ]

qgen = mostx.QuizGenerator(lang='english')
quiz = qgen.gen_mostx_quiz(choices='ABC', n_adjs=1)
print(quiz)
# MostxQuiz(
#     statements=[
#         'C is larger than A',
#         'A is smaller than B',
#         'C is larger than B',
#     ],
#     question='Which is the smallest?',
#     choices=('A', 'B', 'C'),
#     answer='A'
# )
quiz = qgen.gen_sort_quiz(choices='ABC', n_adjs=1)
print(quiz)
# SortQuiz(
#     statements=[
#         'A is sadder than B',
#         'B is happier than C',
#         'C is happier than A',
#     ],
#     request='Put from saddest to happiest',
#     choices=('A', 'B', 'C'),
#     answer=['A', 'C', 'B'],
# )

```

## etc

[Google App](https://play.google.com/store/apps/details?id=jp.gottadiveintopython.mostx) (Mostx + Kivy)
