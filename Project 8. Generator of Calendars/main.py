import datetime


def gen_calendar():
	result = []
	DAYS = ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')
	MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
	          'August', 'September', 'October', 'November', 'December')
	year = int(input("Enter year\n >:"))
	month = int(input("Enter month\n >:"))
	day = datetime.date(year, month, 2)
	cursor = 0
	print(f"        {MONTHS[month - 1]} {year}")
	print(*DAYS)
	while day.weekday() != 0:
		day -= datetime.timedelta(days=1)
	for _ in range(6):
		matrix = [[], [], [], [], [], [], []]
		for idx in range(7):
			matrix[idx] = f"{str(day).split('-')[-1]} "
			# print(matrix)
			day += datetime.timedelta(days=1)
		result.append(matrix)
	for row in result:
		print(*row)


gen_calendar()
