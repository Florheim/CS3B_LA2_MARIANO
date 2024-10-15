#  function created to register the user of his\her personal details
def registerUser(): 
    print("Enter your Information to Register.") #print the message to the user to enter the followings
    userData = []  # created an empty list to store the user details

    # Collecting user information through promth the user to type
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    course = input("Enter Course: ")
    yearLevel = input("Enter Year Level: ")
    section = input("Enter Section: ")
    userName = input("Enter Username: ")
    password = input("Enter Password: ")
    pinCode = input("Enter Pin Code (max 8 characters): ")

    # Validating pin code length
    if len(pinCode) > 8: # if else statement used to check the pin code if longer than the maximum of 8 characters
        print("Pin Code must be a maximum of 8 characters.")  # Prints error message if the pin code is too long
        return # Exits the function after registering

    # Storing user information in an array from the user_data collected
    userInfo = {  #a directory created to store the data
        "first_name": firstName,
        "last_name": lastName,
        "course": course,
        "year_level": yearLevel,
        "section": section,
        "username": userName,
        "password": password,
        "pin_code": pinCode
    }
    userData.append(userInfo) # Adds the user information dictionary to the user_data list

    print("Registration successful! Congratulations, {} {}!".format(firstName, lastName)) # message the user to congratulates after succcessfully regitered.
    return userData # exit the function after congartulating the user

def loginUser(userData): #function created to handle the registered user to login
    while True:   # Starts an infinite loop for multiple login attempts
        userName = input("Enter Username: ")  # prompt the user to insert his/her username
        password = input("Enter Password: ")   # prompt the user to insert his/her password

        # Checking for valid username and password
        for user in userData:  # Loops through the user_data list to find the matching user
            if user['userName'] == userName and user['password'] == password:   # Checks if the username and password match from the entered username and password from registering
                pinCode = input("Enter Pin Code: ")   # Prompts the user for their pin code
                if pinCode == user['pin_code']:  # check if the pin code is match from the registered pin code
                    print("Login successful! Here is your registered information:")   #print message to the user
                    print(user)  # to display the information
                    return    # Exits the login function
                else:
                    print("Incorrect Pin Code. Please try again.")  #print the message if the pin code is wrong
                break
        else:
            print("Invalid Username or Password. Please try again.")   # Exits the for loop after a failed pin code attempt

def main():   #created function that the main function combine the user and register function
    userData = []  #Initializes an empty list for storing registered user data
    userData = registerUser()  # Calls the register_user function and stores the returned data
    
    if userData:  # Checks if the user_data is not empty (successful registration)
        log_in = input("Do you want to log in? (yes/no): ").strip().lower()  # Asks the user if they want to log in
        if log_in == 'yes':  # if the user answer yes to login 
            loginUser(userData)   # Calls the login_user function
        else:
            print("Exiting the program. Thank you!")   # Exits the program if the user doesn't want to log in

if __name__ == "__main__":  # the main function script
    main()  # exit the main function