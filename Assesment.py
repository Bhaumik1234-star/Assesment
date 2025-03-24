# Ask Enter the dugeon name 
adventurer = input('Enter the dungeon name: ')
# Ask Enter the dugeon level 
adventurer = float(input('Enter the dugeon level: '))

if adventurer <= 12: 
    print(f'We can fearlessly explore {adventurer}')
else:
     print(f'We cannot fearlessly explore {adventurer}')