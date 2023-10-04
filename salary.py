from typing import Tuple

TAX = 0.13


def hourly_salary(position: str, hours: float) -> Tuple[float]:
    """Calculate hourly salary based on actual hours and position in company.

    Args:
        position: str - position in company.
        hours: int - actual hours.

    Returns:
        tuple of 2 floats: salary after tax, tax itself.
    
    Raisers:
        Exception: position is not defined in rates
    """
    #used constans
    rates = {
        'junior': 70000,
        'middle': 120000,
        'senior': 180000,
        
    }
    normal_hours = 160

    #check if position defined in rates
    rate = rates.get(position)
    if not rate:
        raise Exception(f'Position <{position}> is not defined in rates.')
    
    #calculations
    half = rate / 2
    pretax = rates[position] / 2 + rates[position] / 2 * (hours / normal_hours)
    after_tax = round(pretax * (1 - TAX), 2)

    return  after_tax, pretax - after_tax  #salary after tax and tax itself


def coach_salary(trainings: Tuple[int]) -> Tuple[float]:
    """Calculate salary based on trainings number.

    Args:
        trainings: - tuple of int, each number refers to number of people.

    Returns:
        tuple of 2 floats: salary after tax, tax itself.
    """
    rate = 150
    
    pretax = sum(trainings) * rate
    after_tax = round(pretax * (1 - TAX), 2)

    return after_tax, pretax - after_tax
