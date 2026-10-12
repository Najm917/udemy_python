from tkinter import *
from tkinter import messagebox
import random,pyperclip

letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol=['.','@','_','%','!','+']


letter_max_char=random.randint(5,8)
max_number=random.randint(2,4)
max_symbol=random.randint(1,2)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Pehle purana password agar likha ho toh clear karein
    password_entry.delete(0, END)

    password_letters = [random.choice(letter) for _ in range(letter_max_char)]
    password_symbols = [random.choice(symbol) for _ in range(max_number)]
    password_numbers = [random.choice(number) for _ in range(max_symbol)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
  website=website_entry.get()
  email=email_entry.get()
  password=password_entry.get()
  
  if len(website) ==0 or len(password) <8:
    messagebox.showinfo(title= "OPPS" ,message="Please make sure you have not left any field and password len minimum 8")
  else:
    
  # popup conform to save
    is_ok=messagebox.askokcancel(title=website,message=f"these are the details:\n email: {email}\n"f"\n password: {password}\n Is it ok to save")
    if is_ok:
      with open ("data.txt","a")as data_file:
        data_file.write(f"website:{website} | email:{email}| password:{password}\n")
        
      website_entry.delete(0,END)
      password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# --- Labels (sticky="w" se left-align rahenge) ---
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w", pady=3)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="w", pady=3)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w", pady=3)

# --- Entries & Buttons ---
# Website input (columns 1 aur 2 dono ko cover karega)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew", pady=3)
website_entry.focus()

# Email input (columns 1 aur 2 dono ko cover karega)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=3)
email_entry.insert(0,"s.najm08875@gmail.com")

# Password input (column 1 me rahega)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew", pady=3)

# Generate Password Button (column 2 me fit aayega)
generate_pass = Button(text="Generate Password",command=generate_password)
generate_pass.grid(row=3, column=2, sticky="ew", padx=(5, 0), pady=3)

# Add Button (full width - columns 1 aur 2 dono ke barabar)
save_pass = Button(text="Add", width=36,command=save)
save_pass.grid(row=4, column=1, columnspan=2, sticky="ew", pady=3)

window.mainloop()