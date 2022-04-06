# Prompt the user to enter a positive number. 
prompt = 'Enter a positive Number: '

active = True

def count():
    for x in range(0,int(num),2):
        print(x)

while active:
    user_input = input(prompt)
    int_check = user_input.isdigit()
    num = user_input
    if int_check == True:
        print(count())
        active = False
    else: print(f'Invalid Entry...\n')
    
        
        
    
        
        
    
    
        
        
        
#         if int_check != False:
#             while int_check == True:
#                 break
#         elif int_check == False:
#             print(f"Only Positive Numbers \n {prompt}")
# print(count())

#     
# num = user_input.isdigit()
# while int_check == True:
#     x = range(0, num, 2)
#     if num == True:
#         for x in x:
#             print(x)
#     elif user_input == False:
#         print("Number ONLY")
# Verify that the input is an integer and it is positive. Research the isDigit() method of the string object. 
# If it is not valid, prompt the user to re-enter until they enter a valid number.
# Create a function that displays only even numbers between and including 0 up to and including (if valid)
# the number provided by the user.
# y = num
# num = [x for x in range(0,y,2)]
# print(num)
