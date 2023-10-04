import math

def degree(a: float, t: float, r: float, V: float) -> float:
    """Calculating the angular displacement

    Args:
        a (float): acceleration
        t (float): time
        r (float): radius
        V (float): initial_velocity

    Returns:
        float: the angular displacement
    """
    S = V * t + (a * t ** 2) / 2
    C = 2 * math.pi * r
    radians = S / C
    degrees = math.degrees(radians)
    return degrees

a = 5
t = 7
r = 2
V = 9
result = degree(a, t, r, V)
print(result)