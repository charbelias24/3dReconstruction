import os

def name_picture(prefix=''):
	try:
		with open('data/current_count.txt', 'r') as file:
			current_count = file.read()
			if current_count:
				current_count = int(current_count)
			else:
				return 0
		with open('data/current_count.txt', 'w') as file:
			file.write(str(current_count+1))

		return prefix + str(current_count) + '.jpg'

	except Exception as e:
		print (e.message)

print (name_picture("TEST"))