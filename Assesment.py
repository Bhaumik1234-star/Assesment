''' This program asks to figure which dugeons are safe to explore and if power level is less than 12 or equal to 12 its mean safe
and if the power level is more than 12 its mean its not safe'''

# Ask Enter the dugeon level 
level = float(input('Enter the dugeon level: '))
if level > 0:
    return level
else:
    print('Invalid input. The dungeon level must be a positive integer.')

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

def main():
    party_level = 12 
    dugeonus = []

    while True:
        dugeonus_name = input('Enter the dugeon name: ')
        dugeonus_level = get_valid_dugeouns_level()
        dugeonus.append((dugeonus_name, dugeonus_level))
        if dugeon level == 'Delfino Square':
            break
        

    