import tkinter

class Window:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Hello Tkinter")

        self.label = tkinter.Label(self.main_window, text = "Choose One")
        self.label.pack(fill=tkinter.BOTH, expand=True, padx=100, pady=30)

        hello_button = tkinter.Button(self.main_window, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tkinter.LEFT, padx=(20,0), pady=(0,20))

        goodbye_button = tkinter.Button(self.main_window, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tkinter.RIGHT, padx=(0,20), pady=(0,20))
    
    def say_hello(self):
        self.label.configure(text="Hello World!")

    def say_goodbye(self):
        self.label.configure(text="Goodbye!\n (Closing in 2 seconds)")
        self.main_window.after(2000, self.main_window.destroy)


def main():
    root = Window()
    root.main_window.mainloop()

main()