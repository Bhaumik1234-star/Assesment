''' This program asks to figure which dugeons are safe to explore and if power level is less than 12 or equal to 12 its mean safe
and if the power level is more than 12 its mean its not safe'''

# Ask Enter the dugeon name 
adventurer = input('Enter the dungeon name: ')
# Ask Enter the dugeon level 
adventurer = float(input('Enter the dugeon level: '))

if adventurer <= 12: 
    print(f'We can fearlessly explore {adventurer}')
else:
     print(f'We cannot fearlessly explore {adventurer}')