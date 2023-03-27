from tkinter import *
from tkinter import messagebox
import sqlite3

class RoomServiceUI:
    def _init_(self, root):
        self.root = root
        self.root.title("Room Service")
        pad = 3
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # Create room number label and entry field
        room_number_label = Label(self.root, text="Room Number:", font=("Arial", 12))
        room_number_label.pack()
        self.room_number_entry = Entry(self.root, font=("Arial", 12))
        self.room_number_entry.pack()


        # Create room service label
        room_service_label = Label(self.root, text="Room Service Menu", font=("Arial", 16))
        room_service_label.pack(pady=10)

        # Create room service label and drop-down menu
        room_service_options = ["Pizza", "Burger", "Sandwich", "Fries", "Coke", "Pepsi", "Water", "Juice", "Clean room"]
        room_service_label = Label(self.root, text="Room Service:", font=("Arial", 12))
        room_service_label.pack()
        self.room_service_listbox = Listbox(self.root, height=9, selectmode=MULTIPLE)
        for option in room_service_options:
            self.room_service_listbox.insert(END, option)
        self.room_service_listbox.pack()

        # Create submit button
        submit_button = Button(self.root, text="Submit", font=("Arial", 12), command=self.submit_order)
        submit_button.pack(pady=10)

        # Connect to database and create table if it doesn't exist
        self.conn = sqlite3.connect('Hotel.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS orders
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       room_service TEXT,
                       room_number TEXT)''')

        self.conn.commit()

        self.root.mainloop()


    def submit_order(self):
        # Get selected room service
        room_service_indices = self.room_service_listbox.curselection()

        # Check if room service is selected
        if not room_service_indices:
            messagebox.showerror("Error", "Please select room service.")
            return

        # Retrieve the selected room service options
        room_service = [self.room_service_listbox.get(index) for index in room_service_indices]
    
        # Join the selected items into a comma-separated string
        room_service_str = ", ".join(room_service)

        # Get room number
        room_number = self.room_number_entry.get()
        # Check if room number is empty
        if not room_number:
            messagebox.showerror("Error", "Please enter room number.")
            return

        # Add order to database
        self.c.execute("INSERT INTO orders (room_service, room_number) VALUES (?, ?)", (room_service_str, room_number))
        self.conn.commit()

        # Show success message
        success_message = f"Order for {room_service_str}"
        success_message += f" for room {room_number} received."
        messagebox.showinfo("Order Successful", success_message)

        # Reset selection and room number entry field
        self.room_service_listbox.selection_clear(0, END)
        self.room_number_entry.delete(0, END)


    def _del_(self):
        # Close database connection when object is
        self.conn.close()


# Run payment UI
def room_service_ui_fun():
    root = Tk()
    application = RoomServiceUI(root)
    root.mainloop()