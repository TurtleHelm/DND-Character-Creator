from data import Character

def main() -> None:
    char = Character()
    isTrue = True
    
    print(f'Welcome to the D&D Random Character Generator ({char.data.version})')
    
    while isTrue:
        print('===============================================================')
        isTrue = bool(int(input('Create a new character? (1/0): ')))
        
        if isTrue:
            char = Character()
            print('===============================================================')
            print(char.details)
            
        else: print('Exiting Character Generator...')

main()