import pendulum


today = pendulum.today('Europe/Moscow').format('YYYY-MM-DD')
tomorrow = pendulum.tomorrow('Europe/Moscow').format('YYYY-MM-DD')
print(today)
