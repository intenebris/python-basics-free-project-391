LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*"

def next_random(number):
    return (16807 * number) % 2147483647

def generate_password(length: int, seed: int, use_uppercase=True, use_digits=True, use_special=False) -> str:
    alphabet = LOWERCASE
    if use_uppercase:
        alphabet += UPPERCASE
    if use_digits:
        alphabet += DIGITS
    if use_special:
        alphabet += SPECIAL
    current = seed
    result = ""
    i = 0
    while i < length:
        current = next_random(current)
        index = current % len(alphabet)
        result += alphabet[index]
        i += 1
    return result

print(generate_password(length=8, seed=1))
print(generate_password(length=12, seed=123))
print(generate_password(length=12, seed=123, use_special=True))
print(generate_password(length=8, seed=1, use_uppercase=False, use_digits=False))
print(generate_password(length=-3, seed=42))
print(generate_password(length=18, seed=4, use_special=True))