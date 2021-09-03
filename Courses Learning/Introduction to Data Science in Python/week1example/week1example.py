# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:55:33 2021

@author: zmoay
"""
#this is a example of week1-------------------------------------------------

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))

#%%

#this is a example of week1-------------------------------------------------

people = ['1 2 3', '4 5 6', '7 8', '9 10']
def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))

#%%

#this is a example of week1-------------------------------------------------

people = ['Ali', 'Zari', 'Zeinab']
def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))
#%%

#this is a example of week1-------------------------------------------------


g = lambda a,b:a*b
print(g(100,2))

#%%

#this is a example of week1-------------------------------------------------


x=[1,2,3]
y=list(map(lambda a:a**2, x))
print(y)


#%%

#this is a example of week1-------------------------------------------------


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

#%%

#this is a example of week1-------------------------------------------------


def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [j*i for i in range(10) for j in range(10)]

#%%

#this is a example of week1-------------------------------------------------

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids
