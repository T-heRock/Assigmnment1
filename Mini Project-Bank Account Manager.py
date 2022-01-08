#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Account():
    
    def __init__(self):
        self.account_number=['XXXX123456','XXXX234567','XXXX1234','XXXX2345','XXXX3456','XXXX4567']
        self.pin_dict={'XXXX123456':'1234','XXXX234567':'4567','XXXX1234':'0000','XXXX2345':'0001','XXXX3456':'0002','XXXX4567':'0003'}
        self.savings_customer_info={'XXXX123456':['PQRS','XXXX123','987654321',10000,'1234'],'XXXX234567':['ABCD','XXXX456','0987654321',50000,'4567']}
        self.checking_customer_info={'XXXX1234':['PQR','XXXX123W','9876543219',10000,'0000'],'XXXX2345':['ABCD','XXXX456E','09876543218',3000,'0001']}
        self.business_customer_info={'XXXX3456':['WXYZ','XXXX123R','9876543217',100000,'0002'],'XXXX4567':['ABD','XXXX456T','09876543216',200000,'0003']}
        
    
    
    def info(self):
       
        if user_input in self.account_number:
            pin_input=input("\nPlease enter your 4 digit PIN")
            for k,v in self.pin_dict.items():
                if self.pin_dict[user_input]==pin_input:
        
                    acc_type_input=input("\nPress 1 for Savings Account\nPress 2 for Checking Account\nPress 3 for Business Account\n")
                    if acc_type_input==str(1):
                        AS.start()
                        break
        
                    elif acc_type_input==str(2):
                        AC.start1()
                        break
        
                    elif acc_type_input==str(3):
                        AB.start2()
                        break
            
                else:
                    print("\nIncorrect PIN!")
                    break

                
        else:
            print("\nAccount Number does not match.\nPlease provide correct one.")
            
        
        
class atm_savings_account(Account):
    
    def start(self):
        while True:
            input_=input("\nEnter the Choice:\n1. Withdraw\n2. Deposit\n3. Balance Enquiry\n4. Exit")
            if input_==str(1):
                AS.withdraw()
                print("\nAmount Withdrawed")
            elif input_==str(2):
                AS.deposit()
                print("\nAmount Deposited")
            elif input_==str(3):
                AS.Balance()
            elif input_==str(4):
                print("\nApplication Terminated")
                break
            
    
    
    def withdraw(self):
        w_input=int(input("\nEnter the amount to be withdrawn: "))
        for key in A.savings_customer_info:
            if key==user_input:
                A.savings_customer_info[user_input][3]=A.savings_customer_info[user_input][3]-w_input
                
        
    
    def deposit(self):
        d_input=int(input("\nDeposit the Amount: "))
        for key in A.savings_customer_info:
            if key==user_input:
                A.savings_customer_info[user_input][3]=A.savings_customer_info[user_input][3]+d_input
    
    def Balance(self):
        print("\nYour Account Balance:")
        print("Rs",A.savings_customer_info[user_input][3])
    
    
class atm_checking_account(Account):
    
    def start1(self):
        while True:
            input_=input("\nEnter the Choice:\n1. Withdraw\n2. Deposit\n3.Balance Enquiry\n4. Exit\n")
            if input_==str(1):
                AC.withdraw()
                print("\nAmount Withdrawed")
            elif input_==str(2):
                AC.deposit()
                print("\nAmount Deposited")
            elif input_==str(3):
                AC.Balance()
            elif input_==str(4):
                print("\nApplication Terminated")
                break
    
    
    def withdraw(self):
        w_input=int(input("\nEnter the amount to be withdrawn: "))
        for key in A.checking_customer_info:
            if key==user_input:
                A.checking_customer_info[user_input][3]=A.checking_customer_info[user_input][3]-w_input
                
        
    
    def deposit(self):
        d_input=int(input("\nDeposit the Amount: "))
        for key in A.checking_customer_info.items():
            if key==user_input:
                A.checking_customer_info[user_input][3]=A.checking_customer_info[user_input][3]+d_input
    
    def Balance(self):
        print("\nYour Account Balance:")
        print("Rs.",A.checking_customer_info[user_input][3])     
    

class atm_business_account(Account):
    
    def start2(self):
        while True:
            input_=input("\nEnter the Choice:\n1. Withdraw\n2. Deposit\n3. Balance Enquiry\n4. Exit\n")
            if input_==str(1):
                AB.withdraw()
                print("\nAmount Withdrawed")
            elif input_==str(2):
                AB.deposit()
                print("\nAmount Deposited")
            
            elif input_==str(3):
                AB.Balance()
            elif input_==str(4):
                print("\nApplication Terminated")
                break
        
    
    
    def withdraw(self):
        w_input=int(input("\nEnter the amount to be withdrawn: "))
        for key in A.business_customer_info:
            if key==user_input:
                A.business_customer_info[user_input][3]=A.business_customer_info[user_input][3]-w_input
                
        
    
    def deposit(self):
        d_input=int(input("\nDeposit the Amount: "))
        for key in A.business_customer_info:
            if key==user_input:
                A.business_customer_info[user_input][3]=A.business_customer_info[user_input][3]+d_input
    
    def Balance(self):
        print("\nYour Account Balance:")
        print("Rs",A.business_customer_info[user_input][3])


# In[6]:


A=Account()
AC=atm_checking_account()
AS=atm_savings_account()
AB=atm_business_account()

user_input=input("Please Enter your Account Number: ")
A.info()


# In[8]:


A.business_customer_info


# In[ ]:




