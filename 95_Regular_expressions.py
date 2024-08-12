# Regular Expressions
import re

# Define a regular expression pattern
pattern = r"el"

# Match the pattern against a string
text = "Hello, world!"

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")


# Searching for a pattern 
pattern = r"expression"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)