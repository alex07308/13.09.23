#1 цензура текста
from typing import List
def  get_word_case_mutations(word: str) -> List[str]:
    def fill_zeros(text: str) -> str:
         filler = (len(word) - len(text)) * '0'
         return filler + text 
    word = word.lower()
    result = []
    for i in range(2 ** len(word)):
        bits = fill_zeros(bin(i)[2:])
        new = ''
        for char, bit in zip(word, bits):
            new += char.upper() if bit == '1' else char
        result.append(new)
    return result    

def censor_the_file(source_file: str, banned_words: str = 'banned.txt') -> None:
    #прочитать файлы
    with open(banned_words) as banned:
        lines = banned.readlines()
    words = [word.replace('\n', '') for word in lines]
    all_words = []
    for word in words:
        all_words.extend(get_word_case_mutations(word))

    with open(source_file) as source:
        text = source.read()
    
    #цикл по словам и заменить через replace
    for word in all_words:
        filler = '*' * len(word)
        text = text.replace(word, filler)

    with open(f'censored_{source_file}', 'w') as output:
        output.write(text)

if __name__ == '_main_':
    censor_the_file('file.txt')


