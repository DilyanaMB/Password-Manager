from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
security_png = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=security_png)
canvas.grid(column=1, row=0)

label_website = Label (text='Website:')
label_website.grid(column=0, row=1)

label_email = Label (text='Email/Username:')
label_email.grid(column=0, row=2)

label_password = Label (text='Password:')
label_password.grid(column=0, row=3)

entry_website = Entry(width=38)
entry_website.grid(column=1, row=1, columnspan=2)

entry_email = Entry(width=38)
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

button_generate_password = Button(text='Generate Password')
button_generate_password.grid(column=2, row=3)

button_add = Button(text='Add',width=36)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()