
       #!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

"""
Class personal budget 
"""


class Category:
    def __init__(self, category, expense_item, amount, cur_balance):
        #Class attributes
        self.category = category
        self.expense = expense_item
        self.amount = amount
        self.cur_balance = cur_balance


    @classmethod
    def convert_dict_to_str(self, data):
        self.data = data
        return str(self.data)

        
    @classmethod
    def remove_dict_item(self,file_name,d_dict):
        self.file_name = file_name
        self.d_dict = d_dict

        rline = ''
        #dict for new budget license
        dict_hold_item = {}

        # opening a text file
        try:
            with open(file_name, "r+") as f:
                 rline = f.readlines()
                 f.seek(0)

                 for i in rline:
                     print(i)
                     print(d_dict)
                     if i != d_dict:
                        f.write(i)
                        dict_hold_item = i
                        print(dict_hold_item)
                 f.truncate()
                 
        except:
            print('Unable to update with new balance')
        print()
        Category.main_menu()

    @classmethod
    def add_expenses(self, file_name):
        self.file_name = file_name
        new_expense_dict = {}
        
        'Get key, values for Expenses'
        self.category = input('Enter expense category: ')
        value1 = self.category.capitalize()
        self.expense = input('Enter expense item: ' )
        value2 = self.expense
        self.amount = input('Enter amount spent: ')
        value3 = float(self.amount) #{:.2f}".format(value2)
        print()
        
        #Populate dictionary
        for i in range(3):
	        key = value1
	        value = value2, value3
	        new_expense_dict[key] = value

        print()
    
        try:
            #append dictionary to txtfile
            with open(self.file_name, 'a+') as f:
                f.write(str(new_expense_dict))
                
        except:
            print('Unable to update Expense file')

        print("Expense: %s, Amount: $%.2f saved." % (value2, value3))
        print()
        Category.main_menu()

    @classmethod
    def add_new_budget_items(self, file_name):
        self.file_name = file_name
        new_budget_item_dict = {}
        
        #Get key, values for Budget'
        self.category = input('Enter expense category: ')
        value1 = self.category.capitalize()
        value2 = self.amount = input('Enter budgeted amount: ')
        value2 = self.amount
        
        
        #Populate dictionary
        for i in range(2):
	        key = value1
	        value = value2

        new_budget_item_dict[key] = value1
        new_budget_item_dict[value] = value2

        
        try:
            #append dictionary to txtfile
            with open(self.file_name, 'a+') as f:
                 f.write(str(new_budget_item_dict) + '\n')
                
        except:
             print('Unable to update Budget file')

        print()
        Category.main_menu()


    @classmethod
    def print_expenses(self, file_name):
        print()
        print('*****Budget Expenses*****')
        print()
        self.file_name = file_name
        try:
            with open(file_name, "r") as f:
                for line in f:
                    print(line)
        except:
            print('Unable to access Expense file')
        Category.main_menu()
       

    @classmethod
    def print_budget_categories(self, file_name):
        d = {}
        self.file_name = file_name
        print()
        print('*****Budget Categories and Current Balance*****')
        print()

        try:
            with open(file_name, "r") as f:
                for line in f:
                    d = eval(line)
                    for key,value in d.items():
                        print("%s, $%.2f" % (key, value))
                    break
        except:
            print('Unable to access Budgets file')
        print()
        Category.main_menu()    
            
    @classmethod
    def update_category_items(self, file_name):
        self.file_name = file_name
        d_dict1 = {}
        s_dict = {'Debt':109.00}
        
        with open('Budget.txt', "r+") as f:

            for line in f:
                d_dict1 = eval(line)
                for key,value in d_dict1.items():
                    d_key = key 
                    d_val = value
                    for key,value in s_dict.items():
                        s_key = key
                        s_val = value
                        new_val = d_val + s_val
                    
                if s_key == d_key:
                    #self.remove_dict_item('Budget.txt',d_dict1)
                     
                    d_val = new_val

                    d_dict1.update(s_dict)
                    
                    f.write(str(d_dict1))


    @classmethod
    def check_balance(self, category, file_name):
        # find category in file

        self.category = category
        self.file_name = file_name
        string1 = ''
        d = {}

        string1 = str(category.capitalize())
        # opening a text file
        with open(self.file_name, 'r') as f:
            # Loop through the file line by line
            for line in f:
                #checking string is present in line or not
                d = eval(line)
                if string1 in d:
                    print('check bal', str(d))
                    return (str(d))
                else:
                    return None


    @classmethod
    def does_budget_exist(self,category,file_name):
        self.category = category
        self.file_name = file_name
        
        thisdict = {}

        with open(self.file_name, 'r') as f:
            # Loop through the file line by line to see if budget item exists            
            for line in f:
                thisdict = eval(line)
                               
                for i in thisdict :
                    #if found, return the category and balance dictionary
                    if self.category in (i, thisdict[i]):
                        return str(thisdict)
                        break 
        print()
        Category.main_menu()
          


    @classmethod
    def options(self):

        selected_option = 0
        Category.file_name = ''

        while (selected_option != 5):
            selected_option = int(input("Please select an option: ")) 
                      
            if (selected_option == 1):

                Category.file_name = 'Budget.txt'
                self.add_new_budget_items('Budget.txt')
                self.update_category_items(self.file_name)                  
                

            elif (selected_option == 2):
                #Add budget expense and cost
                self.file_name = 'Expenses.txt'
                self.add_expenses(self.file_name)

            elif (selected_option == 3):
                #List budget category and balances
                self.print_budget_categories('Budget.txt')
                
            elif (selected_option == 4):  
                #List budget expense and price
                self.print_expenses('Expenses.txt')
            
            elif(selected_option == 5):
                #Exit app
                exit

            else:
                print('Invalid selection, please make another selection')


    @classmethod
    def main_menu(self):
        today = datetime.datetime.now()

        print("*********** Personal Budget***********")
        print()
        print(today.strftime("%c"))
        print()
        print("These are the available options:")
        print()
        print("1. Add new budget categories")
        print("2. Add new expense items")
        print("3. List budget categories")
        print("4. List expenses")
        print("5. Exit program")
        print()

        Category.options()

if __name__ == '__main__':
    Category.main_menu()
    
    
         
    