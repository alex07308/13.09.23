from os import remove
import pytest

from censor import censor_the_file

test_data = (
    ('abc hello hEllo heLlo','abc ***** ***** *****'),
    ('hell o abcd HELLO abcd', 'hell o abcd **** abcd'),
)

@pytest.mark.parametrize('source_text, expected', test_data)
def test_censor(source_text: str, expected: str):
    source_file = 'test_censorship.txt'
    banned_file = 'test_banned.txt'
    output_file = f'censored_{source_file}'

    banned_words = ['hello','hola']
    with open(banned_file, 'w') as banned:
        banned.writelines([f'{word}\n' for word in banned_words])
    with open(source_file, 'w') as source:
        source.write(source_text)

    censor_the_file(source_file, banned_file)

    with open(output_file) as output:
        assert output.read() == expected

    for path in [source_file, banned_file, output_file]:
        remove(path)
