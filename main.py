from tkinter import *  
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

#To DO: Assuming the website exists put in a feature that finds the website even if the .com or .org is missing. 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passsword():
    passwordEntry.delete(0, "end")
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
    passwordEntry.insert(0, completePassword)
    pyperclip.copy(completePassword) 

# ---------------------------- GET PASSWORD ------------------------------- # 
def get_info():
    user_input = siteEntry.get()
    try: 
        with open("password_manager/data.json", "r") as file:
            passwords = json.load(file)    
            selected_password = passwords[user_input]
            messagebox.showinfo(title = "Password", 
            message = " Email: {} \n Password: {}".format(selected_password["email"], selected_password["password"]))
    except (FileNotFoundError, KeyError):
        messagebox.showerror(title= "Error", message= "No Password Found!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():   
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
        messagebox.showwarning(title = "Error", message = "Website and Password fields cannot be blank.") 
    else:
        is_ok = messagebox.askokcancel(title = siteValue, message = 
        "These are the details entered: \nWebsite: {} \nEmail: {}, \nPassword: {} \n Is this ok to save?".format(siteValue, contactValue, passwordValue)) 
        if is_ok:
            try:
                with open("password_manager/data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("password_manager/data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)
                with open("password_manager/data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                siteEntry.delete(0, END)
                passwordEntry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #  

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

#Lock Icon 
canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
lock = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100, 100, image = lock)
canvas.grid(row = 0, column = 1)

#Labels 
website = Label(text = "Website:") 
website.grid(row = 1, column = 0)
contact = Label(text = "Email/Username:")
contact.grid(row = 2, column = 0) 
password = Label(text = "Password:")
password.grid(row = 3, column = 0) 

#Entry Fields 
siteEntry = Entry(width = 21)
siteEntry.focus()
siteEntry.grid(row = 1, column = 1) 
contactEntry = Entry(width = 35)
contactEntry.insert(0, "kevinlaguerre7689@gmail.com")
contactEntry.grid(row = 2, column = 1, columnspan = 2) 
passwordEntry = Entry(width = 21) 
passwordEntry.grid(row = 3, column = 1) 

#Buttons 
getPassword = Button(text = "Generate Password", command = generate_passsword)
getPassword.grid(row = 3, column = 2)
add = Button(text = "Add", width = 36, command = save_password)
add.grid(row = 4, column = 1, columnspan = 2)  
search = Button(text = "Search", command = get_info, width = 13) 
search.grid(row = 1, column = 2)


window.mainloop()