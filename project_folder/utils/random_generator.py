# random_generator.py

import random
import time

class RandomGenerator:
    def __init__(self):
        self.generated_numbers = set()
        self.token_count = 0

    def generate_random_numbers(self):
        while self.token_count < 500:
            new_number = random.randint(1, 1000)
            if new_number not in self.generated_numbers:
                self.generated_numbers.add(new_number)
                self.token_count += 1
                print(new_number)
            time.sleep(3)

# Instantiate the RandomGenerator class
random_gen = RandomGenerator()
random_gen.generate_random_numbers()