# Main customer store 

import tkinter as tk
from tkinter.font import Font
from tkinter import *  
from tkinter import messagebox
from db.products import Products
# from  models.Store import Store
from  models.ShoppingCart import ShoppingCart
from utils import center

def viewStore():
    global storeWindow 
    storeLabelFrame = LabelFrame(storeWindow, text="Store Items")
    storeLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    storeItemsFrame = Frame(storeLabelFrame)
    storeItemsFrame.pack(padx="10", pady="5")
    
    products = Products()
    items = products.list() 
    for item in items:
        itemFrame = Frame(storeItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")

        nameLabel = Label(itemFrame, text=item.name,font=("Candara",15),fg="blue")
        categoryLabel = Label(itemFrame, text=item.category_name,font=("Candara",8),fg="green")
        priceLabel = Label(itemFrame, text="₹ %s"%item.price , font=("Candara",13),fg="red")  
        addToCartBtn = Button(itemFrame, text="Add To Cart",cursor="hand2", command=lambda i=item: addItemToCart(i) ) 
        btnImage=PhotoImage(file="images/addToCart.png")       
        addToCartBtn.image= btnImage
        addToCartBtn.config(image=btnImage,width="40",height="40")

        nameLabel.pack(side="left")
        categoryLabel.pack(side="left")
        
        priceLabel.pack(side="left",fill="both", expand="yes" )
        addToCartBtn.pack(side="right" )

    btnGoCart = Button(storeWindow, text="Go To Cart", font=("Candara",15,"bold"),fg="red",bg="white",cursor="hand2", command=viewCart )
    btnGoCart.pack(pady="6")

def viewCart():   
    cartWindow = Toplevel()
    cartWindow.title("The Cart")
    cartWindow.geometry("450x450")
    center(cartWindow)
    cartWindow.grab_set()
    global cart
    cartItems = cart.getCartItems()

    cartItemsLabelFrame = LabelFrame(cartWindow,text="Cart Items")
    cartItemsLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    cartItemsFrame = Frame(cartItemsLabelFrame, padx=3, pady=3)
    cartItemsFrame.pack()
    index = 0
    for item in cartItems:
        itemFrame = Frame(cartItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")

        nameLabel = Label(itemFrame, text=item.name,font=("Candara",15),fg="blue")
        priceLabel = Label(itemFrame, text="₹ %s"%item.price,font=("Candara",13),fg="red")  
        addToCartBtn = Button(itemFrame, text="Remove From Cart", font=("Candara",11,"bold"),fg="red",bg="white",cursor="hand2", command=lambda i=index: removeFromCart(i,cartWindow) )

        nameLabel.pack(side="left")
        priceLabel.pack(side="left")
        addToCartBtn.pack(side="right" )
        index += 1

    shippingFrame = Frame(cartWindow, pady="10")
    shipToLabel = Label(shippingFrame,text="Ship To ",font=("Candara",12,"bold"),fg="indigo")
    shipToLabel.pack(side="left")
    shipTo = Entry(shippingFrame,width=36,borderwidth=1,relief="groove")
    shipTo.pack(side="left")
    shippingFrame.pack()
    
    paymentFrame = Frame(cartWindow, pady="10")
    paymentLabel = Label(paymentFrame,text="Card Number ",font=("Candara",12,"bold"),fg="indigo")
    paymentLabel.pack(side="left")
    paymentEdit = Entry(paymentFrame,width=24,borderwidth=1,relief="groove")
    paymentEdit.pack(side="left")
    paymentFrame.pack()
    
    paymentFrame = Frame(cartWindow, pady="10")
    paymentLabel = Label(paymentFrame,text="Expiry ",font=("Candara",10,"bold"),fg="indigo")
    paymentLabel.pack(side="left")
    paymentEdit = Entry(paymentFrame,width=8,borderwidth=1,relief="groove")
    paymentEdit.pack(side="left")
    
    paymentLabel = Label(paymentFrame,text="CVV ",font=("Candara",10,"bold"),fg="indigo")
    paymentLabel.pack(side="left")
    paymentEdit = Entry(paymentFrame,width=6,borderwidth=1,relief="groove")
    paymentEdit.pack(side="left")
    paymentFrame.pack()
    
  
    
    checkOutFrame = Frame(cartWindow, pady="10")
    totalPriceLabel = Label(checkOutFrame, text="Total Price : ₹ %s" % cart.getTotalPrice(), font=("Candara",14,"bold"),fg="indigo")
    totalPriceLabel.pack(side="left")
    buyBtn = Button(checkOutFrame, text="Buy Now", font=("Candara",15,"bold"),fg="indigo",bg="white",cursor="hand2", command=lambda : buyCommand(cartWindow))
    buyBtn.pack(side="left",padx="10")
    checkOutFrame.pack()

    backToStoreBtn = Button(cartWindow, text="Back To Store", font=("Candara",15,"bold"),fg="red",bg="white",cursor="hand2",command=cartWindow.destroy)
    backToStoreBtn.pack(pady="6")

    cartWindow.mainloop()

def addItemToCart(item):
    global cart
    cart.addToCart(item)
    messagebox.showinfo(title="Success" , message="Item %s Added To The Cart !!"%item.name )

def removeFromCart(itemIndex=None,cartWindow=None):
    global cart
    cart.removeFromCart(itemIndex)
    messagebox.showinfo(title="success",message="Item Removed")
    cartWindow.destroy()
    viewCart()
    
def buyCommand(cartWindow):
    global cart
    cart.itemsSold()
    cart.emptyCart()
    cartWindow.destroy()    
    messagebox.showinfo(title="success",message="Purchase Completed Successfully")



# Start of Main application

storeWindow = tk.Tk()
storeWindow.geometry("450x450")
storeWindow.title("The Store")
center(storeWindow)
viewStore()

cart = ShoppingCart() 

storeWindow.mainloop()
