import tkinter as tk
import string
import secrets




root = tk.Tk()
root.title("Paswort Generator")

entry_label = tk.Label(root, text = "Paswort länge")
entry_label.grid(row = 0, column = 0)
entry_label = tk.Label(root, text = "Verwendungszweck")
entry_label.grid(row = 1, column = 0)

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

login_kennung = "z003sujp"

gen = True

def gen_pw():
    global pwd
    text_box.delete('1.0', tk.END)
    pwd = ""
    inp_len = int(user_entry1.get())
    for i in range(inp_len):
        pwd += ''.join(secrets.choice(alphabet))
    text_box.insert("end-1c", f"Dein Paswort lautet: {pwd}")

def log_pw():
    inp_vw = user_entry2.get()
    save_dir_pw = f"C:\\Users\\{login_kennung}\\Documents\\pw_save.txt"
    file_pw = open(save_dir_pw,'a+')
    file_pw.write(f"Verwendungszweck = {inp_vw} , Passwort = {pwd} \n")

def close():
    global gen
    gen = False
    root.geometry("0x0")


if gen:
    button1=tk.Button(root, text="Erzeugen", command=gen_pw)
    button1.grid(row=0,column=2)
    button2=tk.Button(root, text="Merken", command=log_pw)
    button2.grid(row=1,column=2)


    user_entry1 = tk.Entry(root)
    user_entry1.grid(row = 0, column = 1)
    user_entry2 = tk.Entry(root)
    user_entry2.grid(row = 1, column = 1)

    text_box = tk.Text(root, width = 65, height = 2)
    text_box.grid(row = 2, column = 0, columnspan = 2)

    root.mainloop()