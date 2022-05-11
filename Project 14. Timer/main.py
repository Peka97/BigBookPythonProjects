import datetime
import time

input_time = int(input("Введите число:"))

while input_time:
	seconds = input_time % 60
	minutes = input_time // 60
	hours = minutes // 60
	timer = datetime.time(hour=hours, minute=minutes, second=seconds)
	print(timer)
	input_time -= 1
	time.sleep(1)
