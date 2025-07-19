import random
cards = ['ace', 'king', 'queen', 'jack', '10']
random.shuffle(cards)
print(cards)  # Output: The list `cards` is shuffled randomly

import random
rand_int = random.randint(1, 10)
print(rand_int)  # Output: A random integer between 1 and 10 (inclusive)

import random
numbers = [1, 2, 3, 4, 5, 6]
sample = random.sample(numbers, 4)
print(sample)  # Output: A random sample of 3 unique elements from the list

import random
rand_num = random.randrange(0, 10, 3)  # Randomly selects even numbers between 0 and 9
print(rand_num)  # Output: A random even number between 0 and 9



