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

def check_password(password: str = "") -> str:
    result = ""
    score = 0
    isnum = False
    issymbol = False
    if len(password) >= 8:
        score += 1
    if password.lower() != password:
        score += 1
    if password.upper() != password:
        score += 1
    for char in password:
        if char.isdigit():
            isnum = True
        if not (char.isalnum() or char.isspace()) and char != "_":
            issymbol = True
    if isnum:
        score += 1
    if issymbol:
        score +=1
    if score == 5:
        return f"Очень надёжный пароль (оценка {score} из 5)"
    elif score == 4:
        return f"Надёжный пароль (оценка {score} из 5)"
    elif score == 3:
        return f"Средний пароль (оценка {score} из 5)"
    elif score < 3 and score > 0:
        return f"Слабый пароль (оценка {score} из 5)"
    else:
        return f"Некорректные данные"
    
# print(generate_password(length=8, seed=1))
# print(generate_password(length=12, seed=123))
# print(generate_password(length=12, seed=123, use_special=True))
# print(generate_password(length=8, seed=1, use_uppercase=False, use_digits=False))
# print(generate_password(length=-3, seed=42))
# print(generate_password(length=18, seed=4, use_special=True))

print(check_password("abc"))
print(check_password("abcdefgh"))
print(check_password("abcdef1234"))
print(check_password("Abcdef1234"))
print(check_password("Abcdef123!"))
print(check_password("Abcdef123_"))
print(check_password(""))
print(check_password())