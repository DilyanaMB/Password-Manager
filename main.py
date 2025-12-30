from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = entry_website.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            if  website in data:
                email=data[website]['email']
                password=data[website]['password']
                messagebox.showinfo(message=website, detail=f'Email: {email}\n Password: {password}')
    except:
        pass

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols
    shuffle(password_list)

    password = ''.join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {'email': email, 'password': password},
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(message='Missing required data', detail=f'Some of the fields are emtpy. '
                                                                       f'Please fill all fields and then click \'Add\'\n')
    else:
        is_ok = messagebox.askokcancel(message=website, detail=f'This are the details that you entered:\n'
                                                               f'Email: {email}\n Password: {password}\n '
                                                               f'Is it ok to save?')
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    # reading old data
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    # creating new data
                    json.dump(new_data, f, indent=4)
            else:
                # update existing data with new data
                data.update(new_data)

                with open("data.json", "w") as f:
                    # saving updated data
                    json.dump(data, f, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_email.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
security_png = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=security_png)
canvas.grid(column=1, row=0)

label_website = Label(text='Website:')
label_website.grid(column=0, row=1)

label_email = Label(text='Email/Username:')
label_email.grid(column=0, row=2)

label_password = Label(text='Password:')
label_password.grid(column=0, row=3)

entry_website = Entry(width=21)
entry_website.grid(column=1, row=1)
entry_website.focus()

entry_email = Entry(width=38)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, 'dilyana.m.bodurova@gmail.com')

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

button_search = Button(text='Search',width =13, command=find_password)
button_search.grid(column=2, row=1)

button_generate_password = Button(text='Generate Password', command=generate_password)
button_generate_password.grid(column=2, row=3)

button_add = Button(text='Add', width=36, command=save_data)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
