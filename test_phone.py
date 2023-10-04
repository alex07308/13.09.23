from phones import is_phone
from random import randint
import pytest

def generate_phones(code: str, num: int = 10):
    start, end = 1000000000, 9999999999
    return ['{code}{num}'. format(code=code, num=randint(start, end)) for _ in range(num)]

valid_phones = generate_phones('+7') + generate_phones('8')

invalid_phones = (
    '+7 9998887766', '+7 999 8887766','+7 999 888 7766','+7 999 888 77 66','8 999 888 77 66',
    '8 999 8887766','8 999 888 7766', '8 999 888 77 66','+39998887766', '+139998887766',
    '79998887766','9998887766',
)
@pytest.mark.parametrize('phone', valid_phones)
def test_valid_phones(phone: str):
    assert is_phone(phone), f'<{phone}> should be a VALID phone'

@pytest.mark.parametrize('phone', invalid_phones)
def test_invalid_phones(phone: str):
    assert not is_phone(phone), f'<{phone}> should be an INVALID phone'

#1
def test_phone_type():
    with pytest.raises(Exception):
        is_phone(89997776655)

#2
@pytest.mark.xfail(raises=Exception)
def test_phone_invalid_type_2():
    is_phone(89997776655)

#3
def test_phone_invalid_type_3():
    pytest.raises(Exception, is_phone, (89997776655))
