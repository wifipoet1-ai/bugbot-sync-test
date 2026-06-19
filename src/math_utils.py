def clamp(value, low, high):
    """Return value constrained to the inclusive [low, high] range."""
    if low > high:
        raise ValueError("low must not exceed high")
    return max(low, min(value, high))


def average(numbers):
    """Return the arithmetic mean of a non-empty sequence of numbers."""
    if len(numbers) == 0:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)
