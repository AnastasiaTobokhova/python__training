def generate_password(n):
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                pairs.append((i, j))

    password = ''.join(f'{i}{j}' for i, j in pairs)

    return password

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = generate_password(n)
    print("Нужный пароль:", result)
else:
    print("Число должно быть от 3 до 20.")
