from random import choice, randint, shuffle
import json
import pyperclip 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passsword(passwordEntry, headless=False):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwordList =  [choice(letters) for _ in range(randint(8, 10))]
    passwordList += [choice(symbols) for _ in range(randint(2, 4))] 
    passwordList += [choice(numbers) for _ in range(randint(2, 4))]
    
    shuffle(passwordList)
    completePassword = "".join(passwordList) 
    
    if headless==True: 
        return display_password(completePassword, passwordEntry, True)

    else:
        display_password(completePassword, passwordEntry)
    
# ---------------------------- DISPLAY PASSWORD ------------------------------- # 
def display_password(password, passwordEntry, headless=False): 
    if headless == True: 
        return password 

    else:   
        passwordEntry.delete(0, "end")
        passwordEntry.insert(0, password)
        pyperclip.copy(password) 

# ---------------------------- GET PASSWORD ------------------------------- # 
def get_info(siteEntry, messageBox, headless=False): 
    if headless==True:  
        user_input=siteEntry
        try: 
            with open("data.json", "r") as file:
                passwords = json.load(file)    
                selected_password = passwords[user_input], 
                message = " Email: {} \n Password: {}".format(selected_password["email"], selected_password["password"]) 
                return message
        except (FileNotFoundError, KeyError):
            message = "No Password Found!"
            return message 

    else: 
        user_input = siteEntry.get()
        try: 
            with open("data.json", "r") as file:
                passwords = json.load(file)    
                selected_password = passwords[user_input]
                messageBox.showinfo(title = "Password", 
                message = " Email: {} \n Password: {}".format(selected_password["email"], selected_password["password"]))
        except (FileNotFoundError, KeyError):
            messageBox.showerror(title= "Error", message= "No Password Found!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(siteEntry, contactEntry, passwordEntry, messageBox, headless=False):    
    if headless == True: 
        siteValue = siteEntry
        contactValue = contactEntry
        passwordValue = passwordEntry 
        success = "Data sucessfully saved"
        new_data = {
            siteValue:
            {   "email": contactValue,
                "password": passwordValue,

            }
        }
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4) 
                return success 
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
                return success
                

    else: 
        siteValue = siteEntry.get() 
        contactValue = contactEntry.get() 
        passwordValue = passwordEntry.get() 
        new_data = {
            siteValue:
            {   "email": contactValue,
                "password": passwordValue,

            }
        }

        if len(siteValue) == 0 or len(passwordValue) == 0: 
            messageBox.showwarning(title = "Error", message = "Website and Password fields cannot be blank.") 
        else:
            is_ok = messageBox.askokcancel(title = siteValue, message = 
            "These are the details entered: \nWebsite: {} \nEmail: {}, \nPassword: {} \n Is this ok to save?".format(siteValue, contactValue, passwordValue)) 
            if is_ok:
                try:
                    with open("data.json", "r") as data_file:
                        #Reading old data
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    #Updating old data with new data
                    data.update(new_data)
                    with open("data.json", "w") as data_file:
                        #Saving updated data
                        json.dump(data, data_file, indent=4)
                finally:
                    siteEntry.delete(0, 'end')
                    passwordEntry.delete(0, 'end')