from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# import pandas
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(5,7)#int(input("How many letters would you like in your password?\n"))
    nr_symbols = random.randint(5,7)#int(input(f"How many symbols would you like?\n"))
    nr_numbers = random.randint(5,7)#int(input(f"How many numbers would you like?\n"))

    library = [letters, numbers, symbols]
    randlet = random.randint(0, len(letters) - 1)

    sh_letters = [random.choice(letters) for x in range(nr_letters)]
    sh_symbols = [random.choice(symbols) for x in range(nr_symbols)]
    sh_numbers = [random.choice(numbers) for x in range(nr_numbers)]

    password = sh_numbers + sh_symbols + sh_letters
    random.shuffle(password)
    password = "".join(password)

    pass_entry.delete(0,END)
    pass_entry.insert(0,password)

    pyperclip.copy(password)
    generate_pass.config(text="Password Copied")

    # Revert button text back to "Generate Password" after 2 seconds
    generate_pass.after(2000, reset_button_text)

def reset_button_text():
    generate_pass.config(text="Generate Password")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    mail = mail_entry.get()
    password = pass_entry.get()
    website = web_entry.get()

    web_data = {
        website:{
            "Email/Username": mail,
            "Password":password
        }
    }

    if len(website) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill the columns")
    else:
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(web_data, file, indent=4)

        else:
            data.update(web_data)
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- SEARCH FUNCTION ------------------------------- #

def find_password():
    website = web_entry.get()

    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found")
    else:
        if website in data:
            mail = data[website]["Email/Username"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f'Email/Username: {mail}\n'
                                                       f'Password: {password}')
        else:
            messagebox.showerror(title="Error", message=f"{website} does not exist in the data file")





# ---------------------------- UI SETUP ------------------------------- #

# Displaying Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="White")
window.resizable(0,0)

# Canvas for image
canvas = Canvas(width=200, height=200, bg="White", highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(110, 95, image=logo_img)
canvas.grid(column=1, row=0)

# Website label
web_label = Label(text="Website: ", bg="White", highlightthickness=0)
web_label.grid(column=0, row=1)

# Website input
web_entry = Entry()
web_entry.grid(column=1, row=1, sticky="ew")
web_entry.focus()

# Email
mail_label = Label(text="Email/Username: ", bg="White", highlightthickness=0)
mail_label.grid(column=0, row=2)

# Email input
mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
mail_entry.insert(1, "mymail@gmail.com")

# Password
pass_entry = Label(text="Password: ", bg="White", highlightthickness=0)
pass_entry.grid(column=0, row=3)

# Password input
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3, sticky="ew")

# Button Generate
generate_pass = Button(text="Generate Password", command=pass_gen, width=16)
generate_pass.grid(column=2, row=3)

# Search Button
search = Button(text="Search", width=16, command=find_password)
search.grid(column=2, row=1)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")



window.mainloop()
