# from pynput.keyboard import Key, Controller
# keyboard = Controller()
prompt = '\n Tell me you age to find out your Ticket price. '
prompt += '\n or "quit" to end. '
active = True
age = ''

while active:
    age = int(input(prompt))
    # if age != 'quit':
    #     active = True
    if age < 3:
        print(f'You are FREE!')
    elif age > 12:
        print(f'{age} and over pay $15.00 a Ticket')
    else:
        print(f'{age} year old Tickets cost $10')
    # elif Key == keyboard.Key.enter:
    #     active = False
 