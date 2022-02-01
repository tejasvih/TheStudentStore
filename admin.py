# Main admin management 

from ctypes import alignment
from tkinter import * 
import tkinter as tk
from db.product import Product
from db.products import Products
from utils import center

class admin_management():
    def __init__(self):
        self.showProducts()
       
        
    def showProducts(self):
        # productsWindow = Toplevel()
        productsWindow = tk.Tk()
        productsWindow.geometry("450x450")
        productsWindow.title("Products")
        productsWindow.grab_set()
        center(productsWindow)
        self.prodWindow = productsWindow
        
        storeLabelFrame = LabelFrame(productsWindow, text="Products")
        storeLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

        storeItemsFrame = Frame(storeLabelFrame)
        storeItemsFrame.pack(padx="10", pady="5")
        products = Products()
        items = products.list() 
        for item in items:
            itemFrame = Frame(storeItemsFrame,  pady="5")
            itemFrame.pack(fill="both", expand="yes")

            nameLabel = Label(itemFrame, text=item.name,font=("Candara",12),fg="blue")
            categoryLabel = Label(itemFrame, text=item.category_name,font=("Candara",8),fg="green")
            priceLabel = Label(itemFrame, text="₹ %s"%item.price,font=("Candara",10),fg="red" )  
            
            qtyLabel = Label(itemFrame, text=" Qty: %s"%item.available_quantity,font=("Candara",10),fg="blue" )  
            warningQtyLabel = Label(itemFrame, text=" Warning Qty:  %s"%item.warning_quantity,font=("Candara",10),fg="maroon" )  
            
            editBtn = Button(itemFrame, text="Edit", command=lambda i=item: self.addEditProduct(i) ) 
            
            # btnImage=PhotoImage(file="images/addToCart.png")       
            # addToCartBtn.image= btnImage
            # editBtn.config(image=btnImage,width="40",height="40")
            
            nameLabel.pack(side="left")
            categoryLabel.pack(side="left")
            priceLabel.pack(side="left",fill="both", expand="yes" )
            qtyLabel.pack(side="left",fill="both", expand="yes" )
            warningQtyLabel.pack(side="left",fill="both", expand="yes" )
            editBtn.pack(side="right" )
        
        actionFrame = Frame(productsWindow,  pady="1")
        actionFrame.pack(fill="both", expand="yes")
        btnAdd = Button(actionFrame, text="Add", width=10,command = lambda :self.addEditProduct(None))
        btnAdd.pack(side="right",padx="6")
        btnClose = Button(actionFrame, text="Close", width=10,command=productsWindow.destroy)
        btnClose.pack(side="right",padx="6")
        productsWindow.mainloop()    
        
        
    def addEditProduct(self,item : Product):    
        itemWindow = Toplevel()
        itemWindow.geometry("300x250")
        itemWindow.title("Product")
        itemWindow.grab_set()
        center(itemWindow)
        
    
        l1 = Label(itemWindow, text = "Name")
        l2 = Label(itemWindow, text = "Category Name") 
        l3 = Label(itemWindow, text = "Price") 
        l4 = Label(itemWindow, text = "Available Quantity") 
        l5 = Label(itemWindow, text = "Warning Quantity") 

        # grid method to arrange labels in respective 
        # rows and columns as specified 

        l1.grid(row = 1, column = 1, pady = 10,padx=15) 
        l2.grid(row = 2, column = 1, pady = 4,padx=15) 
        l3.grid(row = 3, column = 1, pady = 4,padx=15) 
        l4.grid(row = 4, column = 1, pady = 4,padx=15) 
        l5.grid(row = 5, column = 1, pady = 4,padx=15) 

        # entry widgets, used to take entry from user 
        self.e1 = Entry(itemWindow) 
        self.e2 = Entry(itemWindow) 
        self.e3 = Entry(itemWindow) 
        self.e4 = Entry(itemWindow) 
        self.e5 = Entry(itemWindow) 
        
        if (item != None):
            self.e1.insert(0, item.name)
            self.e2.insert(0, item.category_name)
            self.e3.insert(0, item.price)
            self.e4.insert(0, item.available_quantity)
            self.e5.insert(0, item.warning_quantity)
            
        # this will arrange entry widgets 
        self.e1.grid(row = 1, column = 2, pady = 10) 
        self.e2.grid(row = 2, column = 2, pady = 4) 
        self.e3.grid(row = 3, column = 2, pady = 4) 
        self.e4.grid(row = 4, column = 2, pady = 4) 
        self.e5.grid(row = 5, column = 2, pady = 4) 

       
        # Button() function is used to create button widgets
        cancelBtn = Button(itemWindow,text="Cancel",width=10, command = itemWindow.destroy)
        cancelBtn.grid(column=2,row=6,pady="10",padx=10)
        
        saveBtn = Button(itemWindow,text="Save", width=10,command=lambda : self.saveProduct(item,itemWindow))
        saveBtn.grid(column=1,row=6,pady="10",padx=10)


        mainloop()     
        
        
    def saveProduct(self,item : Product,itemWindow : Toplevel):    
        products = Products()
        if (item == None):
            item = Product(0,self.e1.get(),0,self.e2.get(),self.e3.get(),self.e4.get(),self.e5.get())
            products.add(item)
        else:
            item.name = self.e1.get()
            item.category_name = self.e2.get()
            item.price = self.e3.get()
            item.available_quantity = self.e4.get()
            item.warning_quantity = self.e5.get()
            products.update(item)
            
        itemWindow.destroy()
        self.prodWindow.destroy()
        self.showProducts()
    

# Start    
admin_management()    



    