
from typing import Callable


# def info(func: Callable) -> Callable:
#     def new(*args, **kwargs):
#         print(f'Running function {func.__name__}')
#         print(f'Positional arguments: {args}')
#         print(f'Keyword arguments: {kwargs}')
#         # не меняет  поведение функции и результат 
#         result = func(*args, ** kwargs)
#         print(f'Result of {func.__name__}): {result}')
#         # новая функция возвращает не измененный результат
#         return result 
#     # декоратор возвращает новую функцию
#     return new


# def make_sentences(*args, sep: str = ', ', end: str = '!') -> str:
#     """Make a sentence using words(args), separator and end of sentence.
#     """
#     return sep.join(args) + end

# make_sentence_winfo = info (make_sentences)
# make_sentence_winfo('python', 'is', 'great', sep='***')




from time import time, monotonic

# def get_time(func: Callable) -> Callable:
#     def new(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'Функция {func.__name__} была выполнена за {time()-start} сек.')
#         return result
#     return new

# #1
# @get_time
# def sum_two(a, b):
#     return a + b

# print(sum_two(2, 2))

# #2
# def sum_two(a, b):
#     return a + b

# timed_sum_two = get_time(sum_two)
# print(timed_sum_two(2, 2))



def work_with_iterables

def calm_the_text(text: str) -> str:
    return text.lower().replace('!', '.')

print(calm_the_text('ршнывмрмывыРЫФргМ+_(800!!неАГПнгАЕН'))




def square(func: Callable) -> Callable:
    return (lambda *args: func(*args) ** 2)

@square
def sum_two(a, b):
    return a + b

print(sum_two(1,1))

# декодат ржденияратор котроый заставляет функцию возвращать только даты с високосным годом
from random import randint
from pprint import pprint

def only_leap_years(func: Callable) -> Callable:
    def is_leap(date: tuple):
        return date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0)
    def new(*args, **kwargs):
        dates = func(*args, **kwargs)
        return [date for date in dates if is_leap(date)]
    return new
#генерировать n дат рождения
@only_leap_years
def generate_birth_dates(n: int):
    return [
        ( 
            randint(1, 28),
            randint(1, 12),
            randint(-6000, 2023),

        ) for _ in range(n)
    ]

pprint(generate_birth_dates(20))




#декораторы генераторов
from typing import Generator
def enum_my_generator(gen_func: Callable) -> Callable:
    def new(*args, **kwargs) -> Generator:
        index = 0
        for value in gen_func(*args, **kwargs):
            yield index, value
            index += 1
    return new

enum_range = enum_my_generator(range)

for i, value in enum_range(5, 10):
    print(i, value)






def round_to_second(func: Callable) -> Callable:
    def new(*args, **kwargs):
        return round(func(*args, **kwargs), 2) 
    return new

@round_to_second
def sum_two(a: float, b: float) -> float:
    return a + b

print(sum_two(1.442, 1.234))


















































































































































