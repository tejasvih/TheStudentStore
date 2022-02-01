# import tkinter module 
from tkinter import * 
import tkinter as tk
from db.categories import Categories
from db.products import Products
from utils import center

    
def main():    
    # creating main tkinter window/toplevel 
    root = tk.Tk() 

    #geometry() method is used to resize the Gui Window
    root.geometry("350x350")
    root.title('Admin')

    center(root)
    # Button() function is used to create button widgets
    # categories = Button(root,text="Categories", command=showCategories)
    # categories.grid(column=1,row=1,pady="10",padx=10)

    products = Button(root,text="Products", command = showProducts)
    products.grid(column=1,row=2,pady="10",padx=10)


    mainloop() 



def showCategories():
    itemWindow = Toplevel()
    itemWindow.geometry("250x250")
    itemWindow.title("Categories")
    itemWindow.grab_set()
    center(itemWindow)
    
    storeLabelFrame = LabelFrame(itemWindow, text="Categories")
    storeLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    storeItemsFrame = Frame(storeLabelFrame)
    storeItemsFrame.pack(padx="10", pady="5")
    categories = Categories()
    items = categories.list() 
    for item in items:
        itemFrame = Frame(storeItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")

        nameLabel = Label(itemFrame, text=item.name)
        nameLabel.pack(side="left")
    
    
    btnAdd = Button(itemWindow, text="Add", cursor="hand2")
    btnAdd.pack(pady="6")
    btnClose = Button(itemWindow, text="Close", command=itemWindow.destroy)
    btnClose.pack(pady="6")
    itemWindow.mainloop()
    
    
def showProducts():
    itemWindow = Toplevel()
    itemWindow.geometry("450x450")
    itemWindow.title("Products")
    itemWindow.grab_set()
    center(itemWindow)
    
    storeLabelFrame = LabelFrame(itemWindow, text="Products")
    storeLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    storeItemsFrame = Frame(storeLabelFrame)
    storeItemsFrame.pack(padx="10", pady="5")
    products = Products()
    items = products.list() 
    for item in items:
        itemFrame = Frame(storeItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")

        nameLabel = Label(itemFrame, text=item.name)
        priceLabel = Label(itemFrame, text="₹ %s"%item.price )  
        
        qtyLabel = Label(itemFrame, text=" Qty: %s"%item.available_quantity )  
        warningQtyLabel = Label(itemFrame, text=" Warning Qty:  %s"%item.warning_quantity )  
        
        editBtn = Button(itemFrame, text="Edit", command=lambda i=item: showProducts(i) ) 
        
        # btnImage=PhotoImage(file="images/addToCart.png")       
        # addToCartBtn.image= btnImage
        # editBtn.config(image=btnImage,width="40",height="40")
        
        nameLabel.pack(side="left")
        priceLabel.pack(side="left",fill="both", expand="yes" )
        qtyLabel.pack(side="left",fill="both", expand="yes" )
        warningQtyLabel.pack(side="left",fill="both", expand="yes" )
        editBtn.pack(side="right" )
    
    
    btnAdd = Button(itemWindow, text="Add", command = addProduct)
    btnAdd.pack(pady="6")
    btnClose = Button(itemWindow, text="Close", command=itemWindow.destroy)
    btnClose.pack(pady="6")
    itemWindow.mainloop()    
    
    
def addProduct():    
    itemWindow = Toplevel()
    itemWindow.geometry("450x450")
    itemWindow.title("Add Product")
    itemWindow.grab_set()
    center(itemWindow)
    # Button() function is used to create button widgets
    saveBtn = Button(itemWindow,text="Save", command=lambda : saveProduct(itemWindow))
    saveBtn.grid(column=1,row=1,pady="10",padx=10)

    cancelBtn = Button(itemWindow,text="Cancel", command = itemWindow.destroy)
    cancelBtn.grid(column=1,row=2,pady="10",padx=10)


    mainloop()     
    
    
def saveProduct(itemWindow : Toplevel):    
    itemWindow.destroy()
    
main()


    