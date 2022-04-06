prompt = '\n What toppings would you like? '
prompt += '\n Enter "quit" to end Topping Selection.'
active = True
toppings = ''
while active:
    select_toppings = input(prompt)
    if select_toppings != 'quit':
        active = False
    else: 
        print(f'{select_toppings} will be added to your pizza.')
        