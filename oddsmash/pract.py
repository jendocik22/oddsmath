import datetime
from datetime import datetime
import pendulum
# now = datetime.datetime.now()
# datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
# print(now)
#
# date_object = datetime.date.tomorrow()
# print(date_object)


today = pendulum.today('Europe/Moscow').format('YYYY-MM-DD')
tomorrow = pendulum.tomorrow('Europe/Moscow').format('YYYY-MM-DD')
print(tomorrow)
print(today)

