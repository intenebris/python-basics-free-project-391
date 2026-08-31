LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*"

def generate_password(length: int, use_uppercase=True, use_digits=True, use_special=False) -> str:
    alphabet = LOWERCASE
    if use_uppercase:
        alphabet += UPPERCASE
    if use_digits:
        alphabet += DIGITS
    if use_special:
        alphabet += SPECIAL
    result = ""
    for i in range(0, length - 1):
        index = i % len(alphabet)
        result += alphabet[index]
    return result

print(generate_password(5))  # => "abcde"
print(generate_password(30))  # => "abcdefghijklmnopqrstuvwxyzabcd"
print(generate_password(0))  # => ""
print(generate_password(length=30, use_uppercase=False, use_digits=False))
# набор = строчные + ПРОПИСНЫЕ + цифры + спецсимволы (70 символов)
print(generate_password(length=70, use_special=True))
# => "...0123456789!@#$%^&*"