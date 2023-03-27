from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info
import payment_ui
import room_service_ui
import feedback_ui
import os


class Hotel:
    def _init_(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top", fill=BOTH)

        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        
        # create feedback button
        self.feedback_button = Button(top, text="FEEDBACK", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2,
                                      width=15, fg="black", anchor="center",
                                      command=feedback_ui.feedback_ui_fun)
        self.feedback_button.pack(side="right", padx=10, pady=10)



        # display message
        self.label = Label(top, font=('arial', 50, 'bold'), text="                WELCOME", fg="#15d3ba", anchor="center")
        self.label.pack(side=TOP, fill=X, padx=5, pady=5)

        # create check in button
        self.check_in_button = Button(bottom, text="CHECK IN", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2,
                                      width=50,
                                      fg="black", anchor="center",
                                      command=check_in_ui.check_in_ui_fun)  # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.grid(row=0, column=2, padx=5, pady=5)

        # create check out button
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2,
                                       width=50, fg="black", anchor="center",
                                       command=check_out.check_out_ui)  # call check_out_ui function from check_out.py file
        self.check_out_button.grid(row=1, column=2, padx=5, pady=5)

        # create show list button
        self.room_info_button = Button(bottom, text="INFORMATION OF ROOMS", font=('', 20), bg="#15d3ba", relief=RIDGE,
                                       height=2,
                                       width=50, fg="black", anchor="center",
                                       command=get_info.get_info_ui)  # call get_info_ui function from get_info.py file
        self.room_info_button.grid(row=2, column=2, padx=5, pady=5)

        # create get information of all the guest
        self.get_info_button = Button(bottom, text="INFORMATION OF ALL GUEST", font=('', 20), bg="#15d3ba",
                                      relief=RIDGE,
                                      height=2, width=50, fg="black", anchor="center",
                                      command=customer_info.customer_info_ui)
        # call customer_info_ui function from customer_info.py file
        self.get_info_button.grid(row=3, column=2, padx=5, pady=5)


        # Add the following button to the Hotel class
        self.payment_button = Button(bottom, text="MAKE PAYMENT", font=('', 20), bg="#15d3ba",
                                      relief=RIDGE,
                                      height=2, width=50, fg="black", anchor="center",
                                      command=payment_ui.payment_ui_fun)
        self.payment_button.grid(row=4, column=2, padx=5, pady=5)

        # Add the following button to the Hotel class
        self.room_service_button = Button(bottom, text="ROOM SERVICE", font=('', 20), bg="#15d3ba",
                                      relief=RIDGE,
                                      height=2, width=50, fg="black", anchor="center",
                                      command=room_service_ui.room_service_ui_fun)
        self.room_service_button.grid(row=5, column=2, padx=5, pady=5)

        # button to exit the program
        self.exit_button = Button(bottom, text="EXIT", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2, width=50,
                                  fg="black",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=6, column=2, padx=5, pady=5)


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if _name_ == '_main_':
    home_ui()
