from tkinter import ttk ,Tk,PhotoImage,Canvas,filedialog


class FrontEnd :
    def __init__(self,master):
        self.master=master
        self.Frame_header=ttk.Frame(self.master)


root=Tk()
FrontEnd(root)
root.mainloop()
