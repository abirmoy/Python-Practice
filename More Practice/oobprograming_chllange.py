# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:01:30 2019

@author: Abirmoy
"""

class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance+amount
        print(amount, "$ has been sucessfully added to the main balance.")
        print("Current balance: ", self.balance)
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return print("Fund not available!")
        else:
            self.balance = self.balance - amount
            
            print(amount, "$ Fund has been successfully withdrawn.")
            print("Current balance: ", self.balance)
            return self.balance
    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"

a = Account('Abir', 500)

b = a.deposit(200)

a.withdraw(350)

print(a)