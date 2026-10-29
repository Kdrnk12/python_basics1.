import random
secret_number = random.randint(1, 100)
print("Я загадал число от 1 до 100. Попробуй угадаь!")
while True:
    guess = int(input("Евой вариант: "))
    if guess < secret_number:
        print("Больше!")
    elif guess > secret_number:
        print("Меньше!")
    else:
        print(f"Бинго! Ты угадал число {secret_number}!")
        break 
