def get_numbers():
    for i in range(100):
        yield i


gens = get_numbers()

# Generate and returns the next value
print(next(gens))

# Print generator in sequence
# for i in gens:
#     print(i)