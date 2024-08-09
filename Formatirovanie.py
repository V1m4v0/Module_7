team1_num = 8
team2_num = 6
score1 = 49
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

def result(score1, score2, team1_time, team2_time):
    if score1 > score2 or score1 == score2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score1 < score2 or score1 == score2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'ничья'
    return result

challenge_result = result(score1, score2, team1_time, team2_time)

print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': team1_num})
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': team1_num, 'team2_num': team2_num})
print('Команда Волшебники данных решила задач: {}'.format(score2))
print('Волшебники данных решили задачи за: {} c!'.format(team1_time))
print(f'Команды решили {score1} и {score2} задач.')
print(f'{challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')