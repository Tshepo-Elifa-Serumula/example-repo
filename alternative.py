# Get input string from user
text = input("Enter a string: ")

# Task 1: Alternate character case
print("\nTask 1 - Alternate character case:")
alternate_chars = ""
for i, char in enumerate(text):
    if i % 2 == 0:  # Even index positions (0, 2, 4, ...)
        alternate_chars += char.upper()
    else:  # Odd index positions (1, 3, 5, ...)
        alternate_chars += char.lower()

print(f"Original: {text}")
print(f"Result: {alternate_chars}")

# Task 2: Alternate word case
print("\nTask 2 - Alternate word case:")
words = text.split()
alternate_words = []

for i, word in enumerate(words):
    if i % 2 == 0:  # Even index positions (0, 2, 4, ...)
        alternate_words.append(word.lower())
    else:  # Odd index positions (1, 3, 5, ...)
        alternate_words.append(word.upper())

result = " ".join(alternate_words)
print(f"Original: {text}")
print(f"Result: {result}")