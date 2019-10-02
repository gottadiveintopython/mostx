# Mostx : Quiz Generator

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
