from tkinter import *
from tkinter import messagebox
import sqlite3
import main

class PaymentUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment")
        pad=3
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # Create payment label
        payment_label = Label(self.root, text="Enter payment information:", font=("Arial", 16))
        payment_label.pack(pady=10)

        # Create name label and entry
        name_label = Label(self.root, text="Name:", font=("Arial", 12))
        name_label.pack()
        self.name_entry = Entry(self.root, font=("Arial", 12))
        self.name_entry.pack()

        # Create amount label and entry
        amount_label = Label(self.root, text="Amount:", font=("Arial", 12))
        amount_label.pack()
        self.amount_entry = Entry(self.root, font=("Arial", 12))
        self.amount_entry.pack()

        # Create submit button
        submit_button = Button(self.root, text="Submit", font=("Arial", 12), command=self.submit_payment)
        submit_button.pack(pady=10)

        # Connect to database and create table if it doesn't exist
        self.conn = sqlite3.connect('Hotel.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS payments
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           amount INTEGER)''')
        self.conn.commit()

        self.root.mainloop()

    def submit_payment(self):
        # Get name and amount from entries
        name = self.name_entry.get()
        amount = self.amount_entry.get()

        # Add payment to database
        self.c.execute("INSERT INTO payments (name, amount) VALUES (?, ?)", (name, amount))
        self.conn.commit()

        # Show success message
        success_message = f"Payment of {amount} received from {name}"
        messagebox.showinfo("Payment Successful", success_message)

        # Clear entries
        self.name_entry.delete(0, END)
        self.amount_entry.delete(0, END)

    def __del__(self):
        # Close database connection when object is deleted
        self.conn.close()


# Run payment UI
def payment_ui_fun():
    root = Tk()
    application = PaymentUI(root)
    root.mainloop()
