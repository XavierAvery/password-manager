from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_tf.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_tf.insert(0, password)
    pyperclip.copy(password)  # Copies to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_tf.get()
    email = email_tf.get()
    password = password_tf.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Opps", "Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Deletes text entries once saved
            website_tf.delete(0, END)
            password_tf.delete(0, END)


# ---------------------------- SEARCH  ------------------------------- #
def find_password():
    website = website_tf.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)
# --------- Canvas --------- #
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# --------- Labels --------- #
website_lb = Label(text="Website:", background=WHITE, fg=BLACK)
website_lb.grid(column=0, row=1)

email_lb = Label(text="Email/Username:", fg=BLACK, background=WHITE)
email_lb.grid(column=0, row=2)

password_lb = Label(text="Password:", fg=BLACK, background=WHITE)
password_lb.grid(column=0, row=3)

# --------- Text Fields --------- #
website_tf = Entry(width=35, bg=WHITE, highlightthickness=0, fg=BLACK, insertbackground=BLACK)
website_tf.focus()
website_tf.grid(column=1, row=1, columnspan=2)

email_tf = Entry(width=35, bg=WHITE, highlightthickness=0, fg=BLACK, insertbackground=BLACK)
email_tf.insert(0, "x@gmail.com")
email_tf.grid(column=1, row=2, columnspan=2)

password_tf = Entry(width=35, bg=WHITE, highlightthickness=0, highlightbackground=WHITE,
                    insertbackground=BLACK, fg=BLACK)
password_tf.grid(column=1, row=3, columnspan=2)

# --------- Buttons --------- #
generate_password_btn = Button(text="Generate Password", bg=WHITE, highlightbackground=WHITE,
                               width=10, command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=33, bg=WHITE, highlightbackground=WHITE, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", bg=WHITE, highlightbackground=WHITE, width=10, command=find_password)
search_btn.grid(column=2, row=1)

window.mainloop()
