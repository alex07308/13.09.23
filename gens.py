# range_ten = range(10)

# for i in range_ten:
#     print(i)




#from sys import getsizeof
# nums = [i for i in range(10**7)]
# memory =getsizeof(nums) +  sum([getsizeof(item) for item in nums])
# print('Размер списка (nums) в битах: {0}'.format(memory))




# range_ten_mil = range(10**7)
# print('Размер списка (nums) в битах: {0}'.format(getsizeof(range_ten_mil)))




from typing import Generator
# def range_(end: int, start: int = 0, step: int = 1) -> Generator:
#     while step > 0 and start < end or step < 0 and start > end:
#         yield start
#         start += step




# for i in range_(start = 5,  end = 10, step = 2):
#     print(i)




# for i in range_(10):
#     print(i)
#     if i == 7:
#         break




# range_ten = range_(10)
# for i in range_ten:  
#     if i == 7:
#         range_ten.throw(Exception('генератор выдал значение больше 7'))
#     print(i)




# def gen():
#     while True:
#         x = yield
#         yield x + 1

# generator = gen()

# num = 0
# for i in generator:
#     if num > 10:
#         break
#     print(generator.send(1))
#     num += 1



#fibonacci
# def fibonacci() -> Generator:
#     fst, snd = 0, 1
#     yield fst
#     while True:
#         yield snd
#         fst, snd = snd, fst + snd

# for index, value in enumerate(fibonacci()):
#     print(f'Фибоначчи №{index} равен {value}')
#     if index == 10:
#         break




# def fibonacci(n: int) -> Generator:
#     fst, snd = 0, 1
#     if n > 0:
#         yield fst
#     while n > 1:
#         yield snd
#         fst, snd = snd, fst + snd
#         n -= 1

# for index, value in enumerate(fibonacci(5)):
#     print(f'Фибоначчи №{index} равен {value}')




# def half_life(years: float) -> Generator:
#     start, time = 1, 0
#     while True:
#         yield start, time
#         start /= 2
#         time += years

# i = 0
# for amount, years in half_life(1000):
#     if i == 10:
#         break
#     print(f'Через {years} лет останется {amount * 100} % вещества')
#     i += 1



#generate leap years
# from datetime import date
# def leap_yaers() -> Generator:
#     year = date.today().year
#     while year % 4 != 0 and (year % 100 == 0 or year % 400 != 0):
#         year += 1
#     while True:
#         if year % 100 != 0  or year % 400 == 0:
#             yield year 
#         year += 4

# i = 0
# for year in leap_yaers():
#     if i > 20:
#         break
#     print(year)
#     i += 1
    




def power_of_numbers(n: int, power: int) -> Generator:
    i = 0
    while i < n:
        yield i ** power
        i += 1

for i in power_of_numbers(7, 2):
    print(i)
