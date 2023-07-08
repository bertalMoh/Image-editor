from tkinter import ttk ,Tk,PhotoImage,Canvas,filedialog,RIDGE
from Image_Manipulations import *


class FrontEnd :
    def __init__(self,master):
        self.master=master
        self.Frame_header=ttk.Frame(self.master)
        self.Frame_header.pack()
        #///////////////////////////////// Header
        # /////// The Logo
        self.logo=PhotoImage(file='icons8-opencv-480.png').subsample(7,7)
        print(self.logo)
        Image_Label=ttk.Label(self.Frame_header,image=self.logo)
        Image_Label.grid(row=0,column=0,rowspan=2)
        Image_Label.image=self.logo
        #//////////////////////// Welcoming Text
        ttk.Label(self.Frame_header,text="Welcome to image editor app").grid(row=0 ,column=1)
        ttk.Label(self.Frame_header, text="Upload,edit and save your images easily!").grid(row=1, column=1)
        #///////////////////////////////// End of Header

        #//////////////////////// Main Menu
        self.Frame_Menu=ttk.Frame(self.master)
        self.Frame_Menu.pack()
        self.Frame_Menu.configure(relief=RIDGE ,padding=(50,10))
        #//////////////////////////////////////////////////// Uploading An Image
        ttk.Button(self.Frame_Menu,text="Upload An Image" , command=Upload_Action()).grid(row=0,column=0,padx=5,pady=5)
        # //////////////////////////////////////////////////// Croping An Image
        ttk.Button(self.Frame_Menu, text="Crop Image", command=Crop_Action()).grid(row=1, column=0, padx=5,pady=5)
        # //////////////////////////////////////////////////// Adding Text to the Image
        ttk.Button(self.Frame_Menu, text="Add Text", command=Add_Text_Action()).grid(row=2, column=0, padx=5,pady=5)
        # //////////////////////////////////////////////////// Drawing Over The Image
        ttk.Button(self.Frame_Menu, text="Draw Over Image", command=Drawing_Action()).grid(row=3, column=0, padx=5,pady=5)
        # //////////////////////////////////////////////////// Filter The Image
        ttk.Button(self.Frame_Menu, text="Apply Filters", command=filter_Action()).grid(row=4, column=0, padx=5,pady=5)
        # //////////////////////////////////////////////////// Blur or Smoothing The Image
        ttk.Button(self.Frame_Menu, text="Blur/Smoothing", command=blur_Action()).grid(row=5, column=0, padx=5,pady=5)
        # //////////////////////////////////////////////////// Adjuste The Levels of The Image
        ttk.Button(self.Frame_Menu, text="Adjust Levels", command=adjuste_Action()).grid(row=6, column=0, padx=5,pady=5)
        # //////////////////////////////////////////////////// Rotate The Image
        ttk.Button(self.Frame_Menu, text="Rotate", command=rotate_Action()).grid(row=7, column=0, padx=5,pady=5)
        # //////////////////////////////////////////////////// Flip The Image
        ttk.Button(self.Frame_Menu, text="Flip", command=flip_Action()).grid(row=8, column=0, padx=5, pady=5)
        # //////////////////////////////////////////////////// Save The Image
        ttk.Button(self.Frame_Menu, text="Save As", command=save_as_Action()).grid(row=9, column=0, padx=5, pady=5)




root=Tk()
FrontEnd(root)
root.mainloop()
