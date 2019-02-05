# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.Rasha.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print(store.name) 

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores :
        if store_name == store.name :
            return store
        else:
            return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()

    user_input = input("Pick a store by typing its name Or type checkout to pay your bills")
    if user_input == 'checkout':
        return False 
    elif get_store(user_input):
        return get_store(user_input)
    else :
        print("invaild store name please try again")



def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    flag=False
    picked_store.print_products()
    print("Enter the products you would like to add to your cart or type back to stor selection menu")
    while True:
        user_input = input()
        if user_input =="back" : 
            break
        
        for product in picked_store.products:
            if product.name == user_input:
                cart.add_to_cart(product)
                flag=True
        if flag==False:
            print("invalid")

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
   
    while True:
        store = pick_store()
        if store :
            pick_products(cart , store)
        else :
            break
    cart.checkout()




def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
