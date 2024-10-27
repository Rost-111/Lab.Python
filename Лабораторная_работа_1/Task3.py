list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

split_index = len(list_players) // 2
team_one = list_players[:split_index]
team_two = list_players[split_index:]

# Вывод команд
print(team_one)
print(team_two)