import tkinter

class Window:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Hello Tkinter")
        
        label = tkinter.Label(self.main_window, text = "Hello World!")
        label.pack(fill=tkinter.BOTH, expand=True, padx=100, pady=50)

        tkinter.mainloop()

def main():
    root = Window()

main()