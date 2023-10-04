
"""Module for checking phone numbers."""

PHONE_LENGTH = 10
CODES = ['8', '+7']

def is_phone(phone: str) -> bool:

    """Check if string is a valid phone number.

    Args:
        phone: str - a phone number to be checked.

    Returns:
        bool - validity of a phone number.
    """
    # if phone.startswith('+7'):
    #     return len(phone) == 12 and phone[2:].isdigit()
    # elif phone.startswith('8'):
    #     return len(phone) == 11 and phone[1:].isdigit()
    # return False

    for code in CODES:
        code_len = len(code)
        if phone.startswith(code):
            valid_length = len(phone) - code_len == PHONE_LENGTH
            all_digits = phone[code_len:].isdigit()
            return valid_length and all_digits
    
    return False
    
def get_local_number(phone: str):
    for code in CODES:
        if phone.startswith(code):
            return phone[len(code):]



def get_region(phone: str, db_filename: str = 'regions.txt'):
    """Get RU region name from database based on phone number.
    Args:
        phone: str - a phone number to be checked.
        db filename: str - a path to local file with phones and regions, defaults to 'regions.txt'
    Returns:
        str - a name of a RU region.
    Raises:
        Exception - a phone is not a valid phone number or not a string.
    """
    if not is_phone(phone):
        raise Exception(f'<{phone}> is not a valid number, cannot get region.')
    
    with open(db_filename, 'r') as db_file:
        lines = [line.replace('\n', '') for line in db_file.readlines()]

    codes_regions = {code: region for code, region in [line.split('|') for line in lines]}
    phone = get_local_number(phone)
    phone_region = phone[:3]

    if phone_region in codes_regions.keys():
        return codes_regions[phone_region]
    return f'region {phone_region} not found in database {db_filename}'
