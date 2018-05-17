# Mostx : Quiz Generator

以下のようなQuizを自動で作るModuleです。


日本語の例

```text
AはBより大きい
AはCより大きい
BはCより小さい
最も小さいのは？
```

中國語の例

```
B比A熱
B比C冷
A比C冷
哪個最冷?
```

韓國語の例

```
B는 A보다 크다
C는 B보다 작다
C는 A보다 작다
어느 것이 가장 작다?
```

英語の例

```text
B is slower than A
A is faster than C
B is faster than C
Which is the slowest one?
```

## 使用法(Usage)

```python
import mostx

available_langs = sorted(mostx.langs())
print(available_langs)  # => ['chinese', 'english', 'japanese', 'korean', ]

quiz = mostx.generate_quiz(
    choices='ABC',
    n_adjectives=1,
    lang='english')
print(quiz)
# {
#   'statements': (
#     'B is slower than A',
#     'A is faster than C',
#     'B is faster than C',
#     Which is the slowest?,
#   ),
#   'choices': ('A', 'B', 'C', )
#   'answer': 'C',
# }

quiz = mostx.generate_quiz(
    choices=('Onion', 'Cabbage', 'Cucumber', ),
    n_adjectives=2,
    lang='english')
print(quiz)
# {
#   'statements': (
#     'Onion is newer and quieter than Cucumber',
#     'Cabbage is quieter and newer than Cucumber',
#     'Cabbage is noisier and older than Onion',
#     'Which is the noisiest?',
#   ),
#   'choices': ('Onion', 'Cabbage', 'Cucumber', ),
#   'answer': 'Cucumber',
# }

quiz = mostx.generate_quiz(
    choices='ABC',
    n_adjectives=mostx.max_n_adjectives() + 1,
    lang='english')
#  !Exception
```
