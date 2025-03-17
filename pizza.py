''' This program asks how many of each type of pizza should be ordered and then prints out the orders, skipping any pizzas that weren't ordered '''


# Create list of pizza types
pizzas = ['cheese', 'chicken', 'pepperoni', 'veggie']
# Create list to store how many of each pizza
quantities = []

# go through list of pizzas in order 
for pizza in pizzas:
    # Ask how many of each pizza 
    howmany = input(f'How many {pizza} pizzas do we want? ')
    quantities.append(howmany)

# Loop through all the pizzas
for pizza, quantity in zip(pizzas, quantities):
    print(pizza, quantity)