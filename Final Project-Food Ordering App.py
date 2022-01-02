#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Food_ordering_app_admin():
    
    def __init__(self):
        
        self.admin_info={'Sarthak':'Sarthak@321'}
        self.food_name_list=[]
        self.food_dict={}
        
    
    def admin_login(self,admin_username,admin_password):
        admin_username_list=[admin_username,admin_password]
        for key,value in self.admin_info.items():
            if (key==admin_username_list[0] and value==admin_username_list[1]):
                print("\nSuccessfully logged-in!")
                while True:
                    a_input=input("\nChoose the action you want to perform\n\n1.)Add Food Item\n2.)Edit Food Item\n3.)View the list of all Food Items\n4.)Remove a Food Item\n5.)Go back to main menu\n\nChoose the option: ") 
                    if a_input == str(1):
                        A.add_food_item()
                    elif a_input == str(2):
                        A.edit_food_item()
                    elif a_input == str(3):
                        A.view_food_items()
                    elif a_input == str(4):
                        A.remove_food_item()
                    elif a_input == str(5):
                        break
                    else:
                        print("Please feed the valid option")
                        
            else:
                print("\nInvalid Credentials!")
        

    def add_food_item(self):
        
        
        food_name=input("\nEnter the Food item name: ")
        
        quantity=input("Enter the Food quantity: ")
        price=input("Enter the price of Food item: ")
        discount=input("Enter the discount on Food item: ")
        stock=input("Enter the stock of Food item: ")
        
        
        self.food_name_list.append(food_name)
        food_id=len(self.food_name_list)
        self.food_dict[food_id]=[food_name,quantity,price,discount,stock]
    
    def edit_food_item(self):
        
        print("\nFollowing are the Food IDs corresponding to Food Items. ")
        
        for id,values in self.food_dict.items():
            print(id,' - ',values)
        ad_input=int(input("\nPlease select the Food ID you want to edit: "))
        
        print("\nWant to edit Food Name of corresponding Food ID ")
        edit_input=input("Y/N ")
        if edit_input=='Y':
            self.food_dict[ad_input][0]=input("\nEnter the New Food Name")
        elif edit_input=='N':
            pass
        else:
            print("Please choose Y/N")
       
        print("\nWant to edit Food Quantity of corresponding Food ID ")
        edit_input=input("Y/N ")
        if edit_input=='Y':
            self.food_dict[ad_input][1]=input("\nEnter the New Food Quantity")
        elif edit_input=='N':
            pass
        else:
            print("Please choose Y/N")
        
        print("\nWant to edit Food Price of corresponding Food ID ")
        edit_input=input("Y/N ")
        if edit_input=='Y':
            self.food_dict[ad_input][2]=input("\nEnter the New Food Price")
        elif edit_input=='N':
            pass
        else:
            print("Please choose Y/N")
        
        print("\nWant to edit Food Discount of corresponding Food ID ")
        edit_input=input("Y/N ")
        if edit_input=='Y':
            self.food_dict[ad_input][3]=input("\nEnter the New Food Discount")
        elif edit_input=='N':
            pass
        else:
            print("Please choose Y/N")
        
        print("\nWant to edit Food Stock of corresponding Food ID ")
        edit_input=input("Y/N ")
        if edit_input=='Y':
            self.food_dict[ad_input][4]=input("\nEnter the New Food Stock")
        elif edit_input=='N':
            pass
        else:
            print("Please choose Y/N")
    
    def view_food_items(self):
        for id,values in self.food_dict.items():
            print('\nFood Id-',id)
            print('Food Name-',self.food_dict[id][0])
            print('Food Quantity-',self.food_dict[id][1])
            print('Food Price-',self.food_dict[id][2])
            print('Food Discount-',self.food_dict[id][3])
            print('Food Stock-',self.food_dict[id][4])
    
    def remove_food_item(self):
        remove_input=int(input("\nEnter the Food ID whose Food item is to be removed: "))
        if remove_input in self.food_dict:
            del self.food_dict[remove_input]
            print(f"\nItem of Item Id {remove_input} removed.")
        else:
            print("Food Id not available.")


class Food_ordering_app_user(Food_ordering_app_admin):
   
    def __init__(self):
        self.user_info={}
        self.order_history_list=[]
        self.user_profile={}
    
    def user_registration(self):

            full_name = input("\nPlease enter your Full Name: ")
            phone_number = input("Please enter your Phone Number: ")
            email=input("Please enter your E-mail: ")
            address=input("Please enter your Address: ")
            self.password=input("Please set the Password: ")
            self.details_of_user = {'Full Name':full_name, 'Phone Number':phone_number, 'E-mail':email, 'Address':address, 'Password':self.password}
            self.username=(self.details_of_user['Full Name']).split(' ')[0] + str(self.details_of_user['Phone Number'])[-4:]
            self.user_profile[self.username]=self.details_of_user

            print(f"\nGreetings {full_name}! You have successfully completed the Sign-up process.")
            print("Your Username is: ",self.username)
        
    def user_log_in(self,username,password):
        
        if username in self.user_profile:
            index_value = list(self.user_profile.keys()).index(username)
            details_of_user_key='Password'
            
            list_of_passwords = [val[details_of_user_key] for key, val in self.user_profile.items() if details_of_user_key in val]
            if list_of_passwords[index_value]==password:
                print('\nSuccessfully Logged in!')
                U.user_display()
            else:
                print("\nIncorrect Password!")
        else:
            print("\nIncorrect Username")
                
            
            
    def user_display(self):
        
             
        while True:
            user__input = input("\n1. Place New Order\n2. Order History\n3. Update Profile\n4. Log out\nEnter your desired task number: ")
            if user__input == str(1):
                U.Place_New_Order()
            elif user__input == str(2):
                U.order_history()
            elif user__input == str(3):
                U.update_profile()
            elif user__input == str(4):
                break
                
            else:
                print("Option Not Available. Please choose the valid option")
    
    
    def Place_New_Order(self):
        
        for key,values in A.food_dict.items():
            print(str(key) + '.',A.food_dict[key][0] + '(' + A.food_dict[key][1] + ')' + '[' +'INR' + A.food_dict[key][2] + ']')
        user_order_input=list(map(int,(input("\nPlease type the number corresponding to your order wish: ")).split(',')))
        print("\nOrder placed Successfully!\nYour orders are: ")
        for corresponding_number in  user_order_input:
            if corresponding_number in A.food_dict:
                self.order_history_list.append(A.food_dict[corresponding_number])
                
                print(A.food_dict[corresponding_number][0]+ '(' + A.food_dict[corresponding_number][1] + ')' + '[' +'INR' + A.food_dict[corresponding_number][2] + ']')

    def order_history(self):
        
        print("\nYour order history is: ")
        for lst in range(len(self.order_history_list)):
            print(str(self.order_history_list[lst][0])+ '(' +str(self.order_history_list[lst][1])+ ')'+ '['+'INR'+ str(self.order_history_list[lst][2])+ ']')
        print("\nTotal number of orders: ",len(self.order_history_list))
        
    
    
    def update_profile(self):
        print("\nYour Profile")
        
        for attributes,assign_values in self.details_of_user.items():
            print(attributes,' - ',assign_values)

        change_input=input("\nDo you want to change your Full Name?\nY/N ")
        if change_input=='Y':
            self.details_of_user['Full Name']=input("\nEnter the New Full Name: ")
        elif change_input=='N':
            pass
            
        change_input=input("\nDo you want to change your Phone Number?\nY/N ")
        if change_input=='Y':
            self.details_of_user['Phone Number']=input("\nEnter the New Phone Number: ")
        elif change_input=='N':
            pass
           
        
        change_input=input("\nDo you want to change your E-mail?\nY/N ")
        if change_input=='Y':
            self.details_of_user['E-mail']=input("\nEnter the New E-mail: ")
        elif change_input=='N':
            pass
            
        
        change_input=input("\nDo you want to change your Address?\nY/N ")
        if change_input=='Y':
            self.details_of_user['Address']=input("\nEnter the New Address: ")
        elif change_input=='N':
            pass
         
        change_input=input("\nDo you want to change your Password?\nY/N ")
        if change_input=='Y':
            self.details_of_user['Password']=input("\nEnter the New Password: ")
        elif change_input=='N':
            pass
            
                
U=Food_ordering_app_user()
A=Food_ordering_app_admin()

while True:
    input_=input("\nEnter the option for Admin login or User login:\n1.) Admin\n2.) User\n3.) Exit\nEnter the choice: ")
    if input_==str(1):
        print("\nEntering as Admin")
        admin_username=input("Enter Admin Username: ")
        admin_password=input("Enter Admin Password: ")
        A.admin_login(admin_username,admin_password)
        
        

    elif input_==str(2):
        while True:
            print("\nEntering as User")
           
            user_input=input("1.) Sign-up\n2.) Log-in\n3.) Go to previous page\nChoose the relevant option: ")
            
            if user_input==str(1):
                U.user_registration()
            
            elif user_input==str(2):
                username=input("Enter Username: ")
                password=input("Enter Password: ")
                
                U.user_log_in(username,password)
            
            elif user_input==str(3):
                break
            
            else:
                print("\nInvalid choice!\nPlease Reconsider")
    elif input_==str(3):
                print("\nApplication Terminated.")
                break
    
    else:
        print("\nEntered a wrong input!!\nPlease consider again.")
    


# In[ ]:




