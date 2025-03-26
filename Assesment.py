''' This program asks to figure which dugeons are safe to explore and if power level is less than 12 or equal to 12 its mean safe
and if the power level is more than 12 its mean its not safe'''

# Ask Enter the dugeon name 
adventurer = input('Enter the dungeon name: ')
# Ask Enter the dugeon level 
level = float(input('Enter the dugeon level: '))
if level > 0:
    return level
else:
    print('"Invalid input. The dungeon level must be a positive integer.')

except ValueError:
            print("Invalid input. Please enter a positive integer.")

if level <= 12: 
    print(f'We can fearlessly explore {adventurer}')
else:
     print(f'We cannot fearlessly explore {adventurer}')

    