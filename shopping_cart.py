# first step function add item to list based on user input
# 2nd function need to delete items from list and function needs to take in agruement.
# 3rd display items in list 
# Main funcntion run shopping program

# From Oklahoma with love
# Helper function to add items to cart
def add(item, input_list, quantity=1):
  for i in range(quantity):
    input_list.append(item)
  input_list.sort()
  return input_list

#print(add('pizza', ['milk', 'pizza', 'pizza']))

#print(add('pizza',4,[]))

# Helper function to remove items from cart
def remove(item, input_list, quantity=1):
  for i in range(quantity):
    input_list.remove(item)
  input_list.sort()
  return input_list

#print(remove('pizza', ['milk', 'pizza', 'pizza'],2))

# Helper function to display items in cart

def show(input_list):
  print(f'Here is the input_list: {input_list}.')

#show(['milk', 'pizza', 'pizza'])

def theCart():
  myList = []
  while True:
    decision = input('Greetings! Type 1 to add items to your cart, 2 to remove items, 3 to show items, 4 to quit.')
    if decision == 1:
      the_item = input('What would you like to add?')
      the_amount = input('How much/many do you need?')
      add(the_item, myList, the_amount)
    elif decision == 2:

    elif decision == 3:

    elif decision == 4:

    else:
      print('Please specify a valid option.')