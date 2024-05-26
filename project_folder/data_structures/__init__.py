# __init__.py

from .number_tracker import NumberTracker

def generate_random_numbers():
    number_tracker = NumberTracker()
    numbers = set()
    
    while len(numbers) < 500:
        new_number = number_tracker.generate_unique_number()
        numbers.add(new_number)
    
    return numbers