import traceback
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def create_password():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_letters+ password_numbers+ password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    try:
        with open ("data.json", "r") as data_file:
            all_passwords = json.load(data_file)
            website = website_input.get()
            u = all_passwords[website]["email"]
            p = all_passwords[website]["password"]
    except KeyError:
        error = messagebox.showinfo(title="Oops", message = "Oops! You have not saved a password for this website.\n Save a password first!")

    except FileNotFoundError:
        error = messagebox.showinfo(title="Oops", message = "Oops! Save a password first.")
    except:
        # print(traceback.format_exc())
        error = messagebox.showinfo(title="Oops", message = "Unknown Error")
    else:
        with open ("data.json", "r") as data_file:
            all_passwords = json.load(data_file)
            website = website_input.get()
            empty_fields = messagebox.showinfo(title=website, message=f"username: {all_passwords[website]["email"]}\n Password: {all_passwords[website]["password"]}")

    finally:
        website_input.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
        new_dict={website_input.get():
                      {
                          "email":username_input.get(),
                          "password":password_input.get()
                      }
                  }
        password_entry = f"{website_input.get()} | {username_input.get()} | {password_input.get()}"
        if (website_input.get()==""or username_input.get()=="" or password_input==""):
            empty_fields = messagebox.showinfo(title="Oops", message= "Please don't leave any fields empty! Try Again")
        else:
            output = messagebox.askokcancel(title = website_input.get(),message= f"These are the details entered:\n username: {username_input.get()}\n password: {password_input.get()}")
            if output ==True:
                try:
                    with open("data.json", "r") as password_storage:
                        pass
                except:
                    with open("data.json", "w") as password_storage:
                        json.dump(new_dict, password_storage, indent =4)
                else:
                    with open("data.json", "r") as password_storage:

                        # password_storage.write(password_entry +"\n")
                        data = json.load(password_storage)
                        data.update(new_dict)
                    with open("data.json", "w") as password_storage:
                        json.dump(data, password_storage, indent =4)
                finally:
                    website_input.delete(0,END)
                    password_input.delete(0,END)
                    username_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize()
window.config(padx=50, pady=50)


canvas = Canvas(width = 200, height = 200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100,110, image= logo)
canvas.grid(row = 1, column =2)

website = Label(text = "Website:")
website.grid(row = 2, column = 1)
website_input = Entry(width = 52)
website_input.grid(row = 2, column = 2, columnspan = 2)
website_input.focus()

username = Label (text = "Email/Username:")
username.grid(row = 3, column = 1)
username_input = Entry(width = 52)
username_input.grid (row = 3, column = 2, columnspan = 2)
# username_input.insert(0, "helloworld@gmail.com")


password = Label(text = "Password:")
password.grid(row = 4, column = 1)
password_input = Entry(width = 33)
password_input.grid (row = 4, column =2)

generate_password = Button(text = "Generate Password")
generate_password.grid(row = 4, column =3)
generate_password.config(command=create_password)

add = Button(text = "Add", width = 44)
add.grid(row = 5, column =2, columnspan = 2)
add.config (command = add_data)

search = Button(text = "Search", width = 14, command = search_website)
search.grid(row = 2, column = 3)


window.mainloop()






