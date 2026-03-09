'''
Project 1 - Hotel Reservation System
(Part 1) - Spring 2026
Author: Jeriah Williams VT PID: Jerwill20

    This is a user-guided hotel reservation system that asks questions of the user to determine
how long they want to stay, their age(for discounts), and information about themselves (such as their name)
to determine if they are eligible for reservation for any discounts and quantify the cost of their stay.

I have neither given or received Unauthorized 
assistance on this assignment.
Signed: Jeriah Williams
'''
  #------------- functions ----------------
def calculate_discounted_rate(standard_nightly_rate,age):
    ''' This function is used to calculate the discount rate based on the person's age.
if they are younger  than 22 they get a 10% discount,
if they are older than 64 they get a 15% discount, 
If they are between 22 and 64 the pay full price.'''
    #student_discount is 10% off the nightly rate if less than 22 years old
    Student_discount = .90
    #senior discount is 15% off the nightly rate if greater than 64 years old
    Senior_discount = .85
    if age < 22:
        return standard_nightly_rate * Student_discount
    elif age> 64:
        return standard_nightly_rate * Senior_discount
    else:
        return standard_nightly_rate 
def calculate_reservation_total(number_of_nights_stay, age):
    standard_nightly_rate = 120
    '''This function takes into account the 6% tax and discounted rate to get 
    an accurate cost of the resveration. 
    Subtotal = number of nights x nightly rate X tax x discount rate(age) x tax'''
    return number_of_nights_stay * calculate_discounted_rate(standard_nightly_rate, age) * (1.06)

def print_menu():
    '''the function "print menu" prints a simple message which informs 
    the user of the options to choose from.'''    
    message_1 = f"""
Select an option from the following menu:
1. Create a reservation
2. Exit the program
    """
    print(message_1)
def create_reservation():
    '''the create reservation function calls the other functions to ask the user questions 
    and calculate thier respones based on thier
    age and number of nights they plan to stay.'''
    first_name = input("What is the guest's first name? ")
    last_name = input("What is the guest's last name? ")
    amount_of_nights_stay = int(input("How many nights? "))
    age = int(input("What is the age of the primary guest? "))
    print(" ")
    '''the f string print statement uses input variables (for first and last name) and calls the function "calculate_resvation_total" to print the total cost based on user numerical inputs.'''
    print(f"The cost of this reservation for {first_name} {last_name} is ${calculate_reservation_total(amount_of_nights_stay, age):.2f}")
    print(" ")

def main():
    
    ''' The function "main" calls the function "create_reservation" and "print_menu" statement. 
    both of these functions are repeated within the while loop until the user inputs "2" in the "menu options" which ends the program'''
    # -------------------------------------------------------
    '''The welcome statment is placed outside the while loop it is the only non repeat statment in the program."'''
    print("Welcome to the Python hotel reservation system!")
    '''within the main function the "create reservation" system is called.
    create_resevations calls most of funtions used in the program.'''
    while True:
        print_menu()
        opening_user_input = input("What is your selection? ")
        '''when 1 is selected the program will start the reservation and ask the user questions'''
        if opening_user_input == "1":
            print(" ")
            print("-"*50)
            print(" ")
            print("Creating new reservation...")

            create_reservation()
            
            print("-"*50)
            '''Once the reservation is complete, the while loop will loop back to the print menu.'''
        elif opening_user_input == "2":
            print(" \nNow exiting program. Thanks for visiting!")
            exit()
            '''When "2" is selected the program will print a "exiting" and "thank you" messege, then exit.'''   
        else:
            print(" \nInvalid choice. please try again.")
            '''Any other character will be flagged as an invalid choice.
            the while loop will loop back to the print menu.'''       
# Call main like this to keep Web-CAT happy:
if __name__ == '__main__':
     main()
