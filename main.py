from data import Character, isBool

char = Character()

print(f'Welcome to the D&D Random Character Generator ({char.data.version})')

isTrue = True

while isTrue:
	print('===============================================================')
	userInput = input('Create a new character? (y/n): ').lower()
	isTrue = isBool(userInput)

	if isTrue:
		char = Character()
		print('===============================================================')
		print(char.details)

	else: print('Exiting Character Generator...')