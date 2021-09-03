# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 07:08:30 2021

@author: zmoay
"""

def cilisus_to_farenfite(cilisus : float) -> float:
    farenhite = (1.8 * cilisus) + 32
    print('your temprator is ', cilisus, 'and ', farenhite, 'farenhite',
          end= ' ')
    print('degree',end='')
    
#%%

def test_password ():
     input_password = input('Enter your pass : ')
     old_password = input('Enter your old pass : ')
     if input_password == old_password:
         print('your password : ', input_password == old_password )
     else:
         print("your password : ", input_password == old_password )
        
#%%

def abselute_number(number):
    if int(number) >= 0 :
        print('the abselute value of ', number, 'is', number)
    else:
        print('the abselute value of ', number, 'is', -1 * int(number))
        
#%%

def inches_to_feet(inch):
    feet = int(inch) // 12
    extra_inch = int(inch) % 12
    print(inch, 'Inches is ',feet, 'Feet &', extra_inch, 'Inches')
    
#%%


def count_down(first_number: int = 10) -> None:
    first_number += 1
    while (first_number > 1):
        first_number -= 1
        print(first_number, end=" ")
    print('\nBLASTOFF! , DONE :)')
    
count_down()

#%%

def count_down2(first_number: int = 10) -> None:
    for i in range(first_number, 0, -1):
        print(i, end=" ")
        
count_down2()        











    
    