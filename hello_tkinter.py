# Program:      hello-tkinter
# Description:  A simple "Hello World" program demonstrating basic GUI functionality using Tkinter widgets and geometry managers.

import tkinter
import tkinter.messagebox

class Window:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Hello Tkinter")

        self.label_text = tkinter.StringVar()
        self.label_text.set("My name is: ")

        self.name_text = tkinter.StringVar()

        self.label = tkinter.Label(self.main_window, textvariable=self.label_text)
        self.label.pack(fill=tkinter.BOTH, expand=True, padx=100, pady=10)

        self.name_entry = tkinter.Entry(self.main_window, textvariable=self.name_text)
        self.name_entry.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20)

        self.hello_button = tkinter.Button(self.main_window, text="Say Hello", command=self.say_hello)
        self.hello_button.pack(side=tkinter.LEFT, padx=(20,0), pady=(0,20))

        self.goodbye_button = tkinter.Button(self.main_window, text="Say Goodbye", command=self.say_goodbye)
        self.goodbye_button.pack(side=tkinter.RIGHT, padx=(0,20), pady=(0,20))
    
    def say_hello(self):
        message = "Hello there " + self.name_entry.get()
        tkinter.messagebox.showinfo("Hello", message)

    def say_goodbye(self):
        if tkinter.messagebox.askyesno("Close Window?", "Would you like to close this window?"):
            message = "Window will close in 2 seconds - goodbye " + self.name_entry.get()
            self.label_text.set(message)
            self.main_window.after(2000, self.main_window.destroy)
        else:
            tkinter.messagebox.showinfo("Not Closing", "Great! This window will stay open.")

def main():
    root = Window()
    root.main_window.mainloop()

main()