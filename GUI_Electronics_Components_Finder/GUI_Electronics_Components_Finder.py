import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox

import time
from datetime import datetime

class GUI():
    def __init__(self):
        #Setup Variable
        self.url_link;
        self.database_path;

        #GUI
        self.app = tk.Tk()
        self.app.geometry('688x400')   # Set size of the frame + place it at 0,0 in the screen
        self.app.configure(bg='white')                  # set background
        self.app.title('Electronis Components Finder')  # set window's title

        #Style 
        self.style = ttk.Style()
        self.style.configure('TFrame',background='white')
        self.style.configure('TLabel',foreground='black',background='white')
        self.style.configure('TCheckbutton',foreground='black',background='white')
        self.style.configure('TRadiobutton',foreground='black',background='white')

        # Main Frame
        self.GUI_URL_FRAME = ttk.Frame(self.app)
        self.GUI_URL_FRAME.pack(side=tk.TOP,fill=tk.X,expand=False)

        self.GUI_INFO_FRAME = ttk.Frame(self.app)
        self.GUI_INFO_FRAME.pack(side=tk.TOP,fill=tk.X,expand=False)

        self.GUI_DATABASE_FRAME = ttk.Frame(self.app)
        self.GUI_DATABASE_FRAME.pack(side=tk.TOP,fill=tk.X,expand=False)


        # URL
        self.URL_label = ttk.Label(self.GUI_URL_FRAME, text="URL :")
        self.URL_entry = ttk.Entry(self.GUI_URL_FRAME, width=96)
        self.URL_button = ttk.Button(self.GUI_URL_FRAME, text="Find")

        self.URL_label.pack(side=tk.LEFT)
        self.URL_entry.pack(side=tk.LEFT)
        self.URL_button.pack(side=tk.LEFT)

        # INFO
        self.INFO_label = ttk.Label(self.GUI_INFO_FRAME, text="Infos :")
        self.INFO_DigikeyNumber_label = ttk.Label(self.GUI_INFO_FRAME, text="Digikey  #  :")
        self.INFO_DigikeyNumber_entry = ttk.Entry(self.GUI_INFO_FRAME, width=40)
        self.INFO_Description_label = ttk.Label(self.GUI_INFO_FRAME, text="Description :")
        self.INFO_Description_entry = ttk.Entry(self.GUI_INFO_FRAME, width=40)
        self.INFO_Datasheet_label = ttk.Label(self.GUI_INFO_FRAME, text="Datasheet  :")
        self.INFO_DatasheetLink_entry = ttk.Entry(self.GUI_INFO_FRAME, width=40)
        self.INFO_ProductNumber_label = ttk.Label(self.GUI_INFO_FRAME, text="Product  #  :")
        self.INFO_ProductNumber_entry = ttk.Entry(self.GUI_INFO_FRAME, width=40)
        self.INFO_Manufacturer_label = ttk.Label(self.GUI_INFO_FRAME, text="Manufacturer :")
        self.INFO_Manufacturer_entry = ttk.Entry(self.GUI_INFO_FRAME, width=40)
        self.INFO_Price_label = ttk.Label(self.GUI_INFO_FRAME, text="Price ($)  :")
        self.INFO_Price_entry = ttk.Entry(self.GUI_INFO_FRAME, width=40)
        self.INFO_AddItem = ttk.Button(self.GUI_INFO_FRAME,text="Add Component")

        self.INFO_label.grid(row=0,column=0,sticky=tk.W,padx=2,pady=2)
        #Section 1
        self.INFO_DigikeyNumber_label.grid(row=1,column=0,sticky=tk.E)
        self.INFO_DigikeyNumber_entry.grid(row=1,column=1)
        self.INFO_Description_label.grid(row=2,column=0,sticky=tk.E)
        self.INFO_Description_entry.grid(row=2,column=1)
        self.INFO_Datasheet_label.grid(row=3,column=0,sticky=tk.E)
        self.INFO_DatasheetLink_entry.grid(row=3,column=1)
        #Section 2
        self.INFO_ProductNumber_label.grid(row=1,column=2,sticky=tk.E)
        self.INFO_ProductNumber_entry.grid(row=1,column=3)
        self.INFO_Manufacturer_label.grid(row=2,column=2,sticky=tk.E)
        self.INFO_Manufacturer_entry.grid(row=2,column=3)
        self.INFO_Price_label.grid(row=3,column=2,sticky=tk.E)
        self.INFO_Price_entry.grid(row=3,column=3)
        self.INFO_AddItem.grid(row=4,column=3,sticky=tk.E)
        
        #Database
        self.DATABASE_label = ttk.Label(self.GUI_DATABASE_FRAME,text="    Database :") # add spacing to match section INFO
        self.DATABASE_entry = ttk.Entry(self.GUI_DATABASE_FRAME,width=54)
        self.DATABASE_select = ttk.Button(self.GUI_DATABASE_FRAME,text="...",width=3)
        self.DATABASE_export = ttk.Button(self.GUI_DATABASE_FRAME,text="Export Excel")

        self.DATABASE_label.grid(row=0,column=0)
        self.DATABASE_entry.grid(row=0,column=1)
        self.DATABASE_select.grid(row=0,column=2)
        self.DATABASE_export.grid(row=0,column=3)










app = GUI()
app.app.mainloop()