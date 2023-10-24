cities = [
    'Москва',
    'Токио',
    'Париж',
    'Нью-Йорк',
    'Лондон',
    'Берлин',
    'Сингапур',
    'Копенгаген',
    'Амстердам',
    'Сидней'
]
# TODO с помощью цикла for и команды enumerate распечатайте рейтинг городов
citi_enumerate = enumerate(cities)
for citi in citi_enumerate:
    print(f"{citi[0]+1:2}-е место: {citi[1]:2}")

