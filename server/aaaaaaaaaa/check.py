def check(id, text):
    f = open('data/check.csv', 'r', encoding = 'cp949')
    data = csv.reader(f, delimiter = ',')
    next(data)
    for row in data:
        if id in row[1]:
            if text == row[2]:
                send = 'access' + row[0]
                return send
            return 'deny'
        return 'deny'
    return 'deny'