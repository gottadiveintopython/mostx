# Mostx : Quiz Generator

以下のような問題を作るmodule。


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

print(sorted(mostx.get_available_langs()))
# => ['chinese', 'english', 'japanese', 'korean', ]

qgen = mostx.QuizGenerator(lang='english')
q = qgen.generate(choices='ABC', n_adjectives=1)

for s in q.statements:
    print(s)
# B is quieter than A
# C is quieter than A
# B is quieter than C
print(q.question)  # => Which is the noisiest?
print(tuple(q.choices))  # => ('A', 'B', 'C')
print(q.answer)  # => A
```
