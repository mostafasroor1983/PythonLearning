import random

# Generating random integers
rand_int1 = random.randint(1, 10)
rand_int2 = random.randint(20, 30)
print(f"Random Integer 1: {rand_int1}")
print(f"Random Integer 2: {rand_int2}")
print("#"*50)

# Generating random floating-point numbers
rand_float1 = random.uniform(1.0, 10.0)
rand_float2 = random.uniform(20.0, 30.0)
rand_float3 = random.random()  # Between 0.0 and 1.0

print(f"Random Float 1: {rand_float1}")
print(f"Random Float 2: {rand_float2}")
print(f"Random Float 3: {rand_float3}")
print("#"*50)

# Generating random complex numbers
real_part1 = random.uniform(1.0, 10.0)
imag_part1 = random.uniform(1.0, 10.0)
rand_complex1 = complex(real_part1, imag_part1)
real_part2 = random.uniform(20.0, 30.0)
imag_part2 = random.uniform(20.0, 30.0)
rand_complex2 = complex(real_part2, imag_part2)
print(f"Random Complex 1: {rand_complex1}")
print(f"Random Complex 2: {rand_complex2}")
print("#"*50)

# Generating random numbers with specific steps
rand_step1 = random.randrange(0, 100, 5)
rand_step2 = random.randrange(50, 150, 4)
print(f"Random Number with Step 5: {rand_step1}")
print(f"Random Number with Step 10: {rand_step2}")
print("#"*50)

# Generating random numbers from a normal distribution
mean = 0
std_dev = 1
rand_normal1 = random.gauss(mean, std_dev)
rand_normal2 = random.gauss(mean, std_dev)
print(f"Random Normal 1: {rand_normal1}")
print(f"Random Normal 2: {rand_normal2}")
print("#"*50)

# Generating random choices from a list
choices = ['apple', 'banana', 'cherry', 'date']
rand_choice1 = random.choice(choices)
rand_choice2 = random.choice(choices)
print(f"Random Choice 1: {rand_choice1}")
print(f"Random Choice 2: {rand_choice2}")
print("#"*50)

# Shuffling a list randomly
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"Shuffled List: {items}")
print("#"*50)

# Generating random samples from a list
sample_size = 3
rand_sample = random.sample(choices, sample_size)
print(f"Random Sample of size {sample_size}: {rand_sample}")
print("#"*50)

