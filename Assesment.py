''' This program asks to figure which dugeons are safe to explore and if power level is less than 12 or equal to 12 its mean safe
and if the power level is more than 12 its mean its not safe'''


def get_valid_dugeon_level():
    while True:
        try:
            level = int(input('Enter the dugeon level: '))
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
        dugeonus_name = input('Enter the dugeons name: ')
        dugeonus_level = get_valid_dugeouns_level()
        dugeonus.append((dugeonus_name, dugeonus_level))

        if dugeon_name == "Delfino Square":
             break

    for dugeonus, level in dugeonus:
        if level <= party_level:
            print(f'We can fearlessly explore {dugeonus}')
        else:
            (f'We cannot fearlessly explore {dugeonus}')

if __name__ == "__main__":
    main()


    