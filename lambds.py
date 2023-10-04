def f(x): return x
y = 1
f = lambda x: (x, y)
print(type(f))


def agree(): return True

agree = lambda: True

#return multiple arguments
def f(x): return x, x ** 2

f = lambda x: (x,x ** 2) # СКОБКИ В ТАКОМ СЛУЧАЕ ОБЯЗАТЕЛЬНЫ

#dot -> (x, y)
def sum_dots(dot_1: tuple, dot_2: tuple) -> tuple:
    return dot_1[0] + dot_2[0], dot_1[1] + dot_2[1]

#takes and returns multiple arguments
sum_dots = lambda dot_1, dot_2: (dot_1[0] + dot_2[0], dot_1[1] + dot_2[1])


def return_atgs(*args, **kwargs):
    return args, kwargs

return_args = lambda *args, **kwargs: (args, kwargs)

print(return_args(1,2,3, d = 5, e = 60))

# sorted
def get_len(word: str) -> int:
    return len(word)


words = ['python', 'is', 'great']
#1
print(sorted(words, key=get_len))
#2
print(sorted(words, key=lambda word: len(word)))
#3
print(sorted(words, key=len))


#filter
words = ['python', 'lkhm', 'great', 'lkjhg']
vowels = 'aeuioy'
def has_vowels(word: str) -> bool:
    return any(vowel in word for vowel in vowels)

#1 через включение
print([word for word in words if has_vowels(word)])
#2 filter
print(list(filter(has_vowels, words)))
#3 filter lambda
print(list(filter(lambda word: any(vowel in word for vowel in vowels), words)))

#map
def square(x: int|float) -> int|float:
    return x ** 2

nums = [1,2,3]
#1 comprehension
print([num ** 2 for num in nums])
#2 map
print(list(map(square, nums)))
for num in map(square ,nums):
    print(num)

#3 map lambda
print(list(map(lambda x:x ** 1, nums)))

from typing import Tuple
sales = {
    'нормальная парта': 0,
    'iphone3': 2,
    'iphoneSE': 5,
    'IPHONE 15 SUPER PRO MAX XL 512TB': 150,
    'кефир 3.5%': 999999,
}

def top_iphones(sales: dict) -> Tuple[str]:
    def is_

