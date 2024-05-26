# project_folder/data_structures/number_tracker.py

import random

class NumberTracker:
    def __init__(self):
        self.generated_numbers = set()
        self.token_count = 0

    def generate_random_numbers(self):
        while self.token_count < 500:
            new_number = random.randint(1, 1000)
            if new_number not in self.generated_numbers:
                self.generated_numbers.add(new_number)
                self.token_count += 1
                print(f"Generated Number: {new_number}")
            else:
                continue

if __name__ == "__main__":
    number_tracker = NumberTracker()
    number_tracker.generate_random_numbers()