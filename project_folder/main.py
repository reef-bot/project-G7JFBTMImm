# main.py

import time
from data_structures.number_tracker import NumberTracker
from utils.random_generator import generate_random_numbers

def main():
    number_tracker = NumberTracker()
    token_count = 0

    while token_count < 500:
        new_numbers = generate_random_numbers(number_tracker.get_used_numbers())
        
        if new_numbers:
            token_count += 1
            number_tracker.add_numbers(new_numbers)
            print(f"Set {token_count}: {new_numbers}")
        
        time.sleep(3)

if __name__ == "__main__":
    main()