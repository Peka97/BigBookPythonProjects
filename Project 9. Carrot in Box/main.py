import random
import time


def main():
	player_1 = input("Введите имя первого игрока\n >:")
	player_2 = input("Введите имя второго игрока\n >:")
	carrot = random.randint(0, 1)
	print(f"""
	HERE ARE TWO BOXES:
	  __________       __________
	 /         /|    /         /|
	+---------+ |   +---------+ |
	|   RED   | |   |  GOLD   | |
	|   BOX   | /   |   BOX   | /
	+---------+/    +---------+/
	   {player_1}            {player_2}
	""")
	peer = input("Заглядываем в коробку? Y\n >:").upper()
	if peer == "Y":
		print("carrot!") if carrot == 0 else print("empty!")
	input("Закрываем? Я спрячу текст выше. Y\n >:").upper()
	for _ in range(20):
		print()
	print(f"""
		HERE ARE TWO BOXES:
		  __________       __________
		 /         /|    /         /|
		+---------+ |   +---------+ |
		|   RED   | |   |  GOLD   | |
		|   BOX   | /   |   BOX   | /
		+---------+/    +---------+/
		   {player_1}            {player_2}
		""")
	choose = input("Меняемся? Y/N\n >:").upper()
	if choose == "Y":
		print("Меняем местами ящики...")
		time.sleep(2)
		print(f"""
		HERE ARE TWO BOXES:
		  __________       __________
		 /         /|    /         /|
		+---------+ |   +---------+ |
		|   GOLD  | |   |   RED   | |
		|   BOX   | /   |   BOX   | /
		+---------+/    +---------+/
		   {player_1}            {player_2}
		""")
	choose = input("Открываем? Y\n >:").upper()
	if choose == "Y":
		print("Открываем коробки...")
		time.sleep(2)
		print("Ух ты!")
		time.sleep(2)
		if carrot == 0:
			print(f"""
			   ___VV____
			  |   VV    | 
			  |   VV    |
			  |___||____|      __________
			 /    ||   /|     /         /|
			+---------+ |    +---------+ |
			|   RED   | |    |   GOLD  | |
			|   BOX   | /    |    BOX  | /
			+---------+/     +---------+/
			 (carrot!)
			   {player_1}            {player_2}
			""")
		elif carrot == 1:
			print(f"""
			                       ___VV____
			                      |   VV    | 
			                      |   VV    |
			 __________           |___||____|      
			/         /|         /    ||   /|     
			+---------+ |       +---------+ |    
			|   GOLD  | |		|   RED   | |    
			|    BOX  | /		|   BOX   | /    
			+---------+/		+---------+/     
								 (carrot!)
			   {player_1}            {player_2}
			""")


main()
