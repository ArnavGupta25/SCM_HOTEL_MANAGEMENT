from tkinter import *
from tkinter import messagebox
import sqlite3
import main

class FeedbackUI:
    def _init_(self, root):
        self.root = root
        self.root.title("Feedback")
        self.root.geometry("400x350")

        # Create feedback label
        feedback_label = Label(self.root, text="Please share your feedback:", font=("Arial", 16))
        feedback_label.pack(pady=10)

        # Create name label and entry
        name_label = Label(self.root, text="Name:", font=("Arial", 12))
        name_label.pack()
        self.name_entry = Entry(self.root, font=("Arial", 12))
        self.name_entry.pack()

        # Create feedback entry
        feedback_entry_label = Label(self.root, text="Feedback:", font=("Arial", 12))
        feedback_entry_label.pack()
        self.feedback_entry = Text(self.root, height=8, width=40, font=("Arial", 12))
        self.feedback_entry.pack(pady=10)

        # Create submit button
        submit_button = Button(self.root, text="Submit", font=("Arial", 12), command=self.submit_feedback)
        submit_button.pack(pady=10)

        # Connect to database and create table if it doesn't exist
        self.conn = sqlite3.connect('Hotel.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS feedback
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           feedback TEXT)''')
        self.conn.commit()

        self.root.mainloop()


    def submit_feedback(self):
        # Get name and feedback from entries
        name = self.name_entry.get()
        feedback = self.feedback_entry.get("1.0", "end-1c")

        # Check if name is entered
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return

        if not feedback:
            messagebox.showerror("Error", "Please enter your feedback.")
            return

        # Add feedback to database
        self.c.execute("INSERT INTO feedback (name, feedback) VALUES (?, ?)", (name, feedback))
        self.conn.commit()

        # Show thank you message
        messagebox.showinfo("Thank You", "Thank you for your feedback!")

        # Clear entries
        self.name_entry.delete(0, END)

        # Clear feedback entry
        self.feedback_entry.delete("1.0", "end")

    def _del_(self):
        # Close database connection when object is deleted
        self.conn.close()


# Run feedback UI
def feedback_ui_fun():
    root = Tk()
    application = FeedbackUI(root)
    root.mainloop()