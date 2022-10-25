import random
user_name = input('Введите ваше имя\n')
scores = 0

with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]

for word in words:
    word_random = ''.join(random.sample(word, len(word)))
    answer = input(f'Угадайте слово: {word_random}\n')
    if answer == word:
        print('Верно! Вы получаете 10 очков')
        scores += 10
    else:
        print('Неверно! Верный ответ – ', word)

with open('history.txt', 'a') as file:
    file.write(user_name + ' ' + str(scores) + '\n')

with open('history.txt', 'r') as file:

    games = [line.strip().split() for line in file]

    record = games[0][1]

    for i in range(len(games)):
        if games[i][1] > record:
            record = games[i][1]

    print(f'Всего игр сыграно {len(games)}')
    print(f'максимальный рекорд {record}')