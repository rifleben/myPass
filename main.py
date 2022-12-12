from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def gen_pass():

    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    account = account_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(account) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Check to see if any fields are empty or invalid")
    else:

        choice = messagebox.askokcancel(title=account,
                                        message=f"You've entered\nAccount: {account}\nUsername: {username} \n"
                                                f"Password: {password}\n Ok to save?")

        if choice:
            with open("data.text", "a") as password_file:
                password_file.write(f"{account} | {username} | {password}\n")

            account_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels

account_label = Label(text="Account: ")
account_label.grid(row=1, column=0)
username_label = Label(text="Username: ")
username_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# values:

account_entry = Entry(width=35)
account_entry.grid(row=1, column=1, columnspan=2)
account_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# button

passgen_button = Button(text="Generate Password", command=gen_pass)
passgen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
