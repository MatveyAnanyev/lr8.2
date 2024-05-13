def check_query(query):
    elements = query.split(', ', 1)  # Разделяем запрос только один раз
    if len(elements) > 1:  # Проверяем, что было разделение
        return elements[1]  # Возвращаем только вторую часть запроса после имени
    else:
        return ''  # Если имя не найдено, возвращаем пустую строку

# Заранее заданные запросы
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Печать результата для каждого запроса
for q in queries:
    result = check_query(q)
    print(q, '—', result)