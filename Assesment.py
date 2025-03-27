''' This program asks to figure which dugeons are safe to explore and if power level is less than 12 or equal to 12 its mean safe
and if the power level is more than 12 its mean its not safe'''

#List to store the results
results_list = []

#Start a loop to print dungeons names and levels 
while True:
    #Ask the user to write the dungeon name
    dugeon_name = input('Enter the dungeon name: ')
    
    if dugeon_name == 'Delfino Square':
        #Ask the user to write the dungeon level
        dugeon_level = int(input('Enter the dungeon level: '))
        
        #Check if the level is 12 or lower and store the results
        if dugeon_level <= 12:
            results_list.append(f'We can fearlessly explore {dugeon_name}')
        else:
            results_list.append(f'We cannot fearlessly explore {dugeon_name}')
        #Break the loop after Delfino Square     
        break
    #For other dungeons
    dugeon_level = int(input('Enter the dungeon level: '))
    
    #Check if the level is 12 or lower and store the results 
    if dugeon_level <= 12:
        results_list.append(f'We can fearlessly explore {dugeon_name}')
    else:
        results_list.append(f'We cannot fearlessly explore {dugeon_name}')
        
#After the loop ends print each results
for result in results_list:        
    print(result)







    