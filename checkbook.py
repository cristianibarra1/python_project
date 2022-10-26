#Combination of all locale settings. If this flag is used when the locale is changed, setting the locale for all categories is attempted. If that fails for any category, no category is changed at all. When the locale is retrieved using this flag, a string indicating the setting for all categories is returned. This string can be later used to restore the settings.

#https://docs.python.org/3/library/locale.html
import locale
locale.setlocale( locale.LC_ALL, '' )



#r is read 
#w write
#a append 



def current_balance():
    '''current balance from the current account and the current moment'''
    #open file money.txt save into my folder as m
    with open ("money.txt" ,"r") as m:
        #transactions is money txt file 
        transactions = m.readlines()
        amount = 0
        #for loop 
        for line in transactions:
            line = float(line)
            amount+= line
            balance = locale.currency(amount, grouping =True)
        
    print("current balance: " + balance)
    
    
def deposit():
    '''Deposit money aka how much youre putting into the account'''
    #variable created to return total number= deposit 
    deposit_total= input("please input the total number for deposit  ")
    #a append 
    with open ("money.txt", 'a') as m:
        m.write('\n')
        m.write(deposit_total)
        
        
def Withdrawl():
    '''how much money you want to take out'''
    #variable created to return total number= withdraw 
    withdrawl_total= input("input the total amount you want to withdraw ? ")
    #a append 
    with open ("money.txt", 'a') as m:
        m.write('\n')
        m.write("-" + withdrawl_total)
#input the name of the customer 
customer= input( "Welcome, please provide account name? ")
        
        
def menu():
    '''list of choices from the menu created attaching all the followinig fuinctions in this function'''
    #start menu printing out the options 
    print('Hello ' + str(customer))
    print ("What can I do for you? ")
    print("1. Current Balance")
    print("2. Deposit")
    print("3. Withdrawl")
    print("4. End Session")

choice = "1"
#while loop to make the menu 
while choice != "4":
    menu()
    print('\n')
    #picking a number aka menu option
    choice = input("enter a number ")
    #1 balance
    if choice == "1":
        current_balance()
    elif choice =='2':
    #2 deposit money
        deposit()
        current_balance()
    elif choice == "3":
    #withdraw money 
        Withdrawl()
        current_balance()
    elif choice == "4":
    #end session 
        print('\n')
        print(" Have a nice day")
    else:
    #if number is not 1-4 please retry again
    print("Invalid entry, please enter 1-4 numbers")

    

    
#Additional Features----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Once you have finished the basic application (in no particular order),done

# add a menu item that allows the user to view all historical transactions,

# assign categories to each transaction

# add a menu item to allow the user to view all the transactions in a given category

# provide the user with summary statistics about the transactions in each category

# keep track of the date and time that each transaction happened

# allow the user to view all the transactions for a given day

# make sure your list of previous transactions includes the timestamp for each

# allow the user to optionally provide a description for each transaction

# allow the user to search for keywords in the transaction descriptions, and show all the transactions that match the user's search term

# allow the user to modify past transactions