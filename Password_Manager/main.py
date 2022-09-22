from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# TODO. Import pyperclip


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# Password Generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    # TODO add - pyperclip.copy(password)


# Save password
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Fields empty.")
    else:
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
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# Search function


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message="File does not exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"Email: {email}\n"
                                        f"Password: {password}")
        else:
            messagebox.showinfo(title="Error",
                                message=f"No existing password for {website}")


# UI SETUP
# window
window = Tk()
window.title("Password Manager")
window.config(padx=5, pady=5, bg="white")

# background
canvas = Canvas(width=510, height=300,
                bg="black",
                highlightthickness=10,
                highlightcolor="black",
                highlightbackground="black")
background = PhotoImage(file="background_street.png")
canvas.create_image(100, 300, image=background)
canvas.grid(column=0, columnspan=16, row=0)

# lock logo
logo = PhotoImage(file="logo_red.png")
canvas.create_image(260, 170, image=logo)


# K.S Sig
canvas.create_text(470, 30,
                   text="K.S",
                   font=(f"{FONT_NAME}", 25, "italic"),
                   fill="pink")

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# email label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

##website entry
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# email entry
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "keelan@gmail.com")

# password entry
password_entry = Entry(width=50)
password_entry.grid(row=3, column=1, columnspan=2)

# generate password button
generate_password_button = Button(text="Generate Password",
                                  command=generate_password,
                                  width=16)
generate_password_button.grid(row=3, rowspan=2, column=4, columnspan=2)

# add button
add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# search button
search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=1, rowspan=2, column=4, columnspan=2)

window.mainloop()
