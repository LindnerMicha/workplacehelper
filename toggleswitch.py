import tkinter as tk

root = tk.Tk()

def ausgabe():
    aktuell_ausgewaehlt = checkbox01var.get()
    textausgabe = tk.Label(root, text=aktuell_ausgewaehlt, bg="orange")
    textausgabe.pack()

checkbox01 = tk.Checkbutton(root)
checkbox01["text"] = "Baugruppe"
checkbox01.pack()

checkbox01var = tk.BooleanVar()
checkbox01var.set(True)
checkbox01["variable"] = checkbox01var

checkbox02 = tk.Checkbutton(root)
checkbox02["text"] = "Leiterplatte"
checkbox02.pack()

checkbox02var = tk.BooleanVar()
checkbox02["variable"] = checkbox02var

schaltf1 = tk.Button(root, text="Übernehmen", command= ausgabe)
schaltf1.pack()

root.mainloop()