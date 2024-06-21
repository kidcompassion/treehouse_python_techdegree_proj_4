from models import (Base, session, engine, Product)
import datetime
import csv
import time


def menu():
    print('''
        \n **** PRODUCT INVENTORY ****
        \r Enter V to view a single item in the database
        \r Enter A to add a new product
        \r Enter B to generate a backup of database contents
        ''')
    selected = input(" What would you like to do? ").upper()

    # Validate user's entry
    if selected in ['V','A','B']:
        return submenu(selected)
    else:
        input('''
                \n ******Your selection was not valid.*******
                \n Press enter to review your options and try again.
            ''')

def submenu(selection):
    if selection == "V":
        return display_product()   
        
    elif selection == "A":
        return add_product()
    elif selection =="B":
        return export_csv()
    else:
        pass


def clean_product(product_name):
    cleaned_product = product_name.split('"')
    return cleaned_product[0]


def clean_date(date_str):
    # Split date from CSV
    cleaned_date = date_str.split('/')
    # Pass date into datetime obj correctly in Y, M, d
    formatted_date = datetime.date(int(cleaned_date[2]), int(cleaned_date[0]), int(cleaned_date[1]))
    return formatted_date

def clean_price(price_str):
    cleaned_price = price_str.split("$")
    cleaned_price = float(cleaned_price[1])*100
    cleaned_price = str(cleaned_price).split('.')
    cleaned_price = int(cleaned_price[0])
    return cleaned_price


def get_all_ids():
    all_results = []
    for product in session.query(Product):
        all_results.append(product.product_id)
        
    return all_results


# Check that entered IDs are 1) integers and 2) included in the list of active product IDs
def clean_id(str_id, all_values):

    try:
        # Check that entered value is an integer
        selected_id = int(str_id)
    except ValueError:
        input('''
                \n **** Sorry, that's not a valid number. ***
                \n Press ENTER to return to the main menu and try your request again.
            ''')
    else:
        # if entered value is an integer, check if it's an active product ID
        if selected_id in all_values:
            return selected_id
        else:
            input('''
                \n ***Sorry, that's not a valid product ID.***
                \n Press ENTER to return to the main menu and try your request again.
            ''')

       
# Create a function to handle getting and displaying a product by its product_id.
def display_product():    
    
    requested_id = input("\rEnter ID of product ")
    # assume there is an error
    id_error = True 

    # get list of all valid product ids
    all_ids = get_all_ids()

    # pass requested id and list of ids into cleaning function. 
    # it will return either a valid int, or a value of None
    id_selected = clean_id(requested_id, all_ids)

    # if it does not return None, assume the value is okay and switch off the error, 
    if id_selected != None:
        id_error = False

    if id_error == False:
        # Query to retrieve product matching requested ID
        selected_product = session.query(Product).filter(Product.product_id==requested_id).first()
        # Print product details
        
        print(f'''
            \nID: {selected_product.product_id}
            \rProduct: {selected_product.product_name}
            \rQuantity Available: {selected_product.product_quantity}
            \rPrice: ${display_price(selected_product.product_price)}
            \rLast updated: {selected_product.date_updated}
        ''')
        # Delay the next step for a second, just to make it nicer for the user when reading
        time.sleep(1)
        # Let the user go back to the main menu
    input("\nPress ENTER to return to the main menu, whenever you are ready.")
    menu()


# Create a function to handle adding a new product to the database.   
def add_product():  
    # prompt the user to enter the product's name, quantity, and price
    product_name = input("What is the product's name? ")
    product_quantity = input("How many are there? ")
    product_price = input("Enter price in $0.00 format. ")
    
    new_product = Product(product_name = product_name, product_quantity = product_quantity, product_price = clean_price(product_price), date_updated = datetime.datetime.now())
    session.add(new_product)
    session.commit()
  
    


def format_price(price_int):
    float = price_int/100
    decimal_positions = format(float, '.2f')
    return "$"+decimal_positions

def format_date(date_str):
    my_date = date_str.strftime("%m/%d/%Y").split("/")
    month = int(my_date[0])
    date = int(my_date[1])
    year = my_date[2]
    
    revised_info = str(month) + "/" + str(date) + "/" + year
    return revised_info

def export_csv():
    # This will hold the queried data
    export_body = []
    # Query for all products
    for product in session.query(Product):
        row = {
            "product_name": product.product_name, 
            "product_quantity" : product.product_quantity, 
            "product_price": format_price(product.product_price), 
            "date_updated" : format_date(product.date_updated)
            }
        export_body.append(row)
        
    
    # generate export csv
    with open('backup.csv', 'w') as csvfile:
         fieldnames = ["product_name", "product_price", "product_quantity", "date_updated"]
         rowwriter = csv.DictWriter(csvfile, fieldnames= fieldnames)
         rowwriter.writeheader()
         rowwriter.writerows(export_body)

    # return success message
    
    print("Export complete")

def display_price(cleaned_price):
    return cleaned_price/100


def add_csv():
    counter = 0
    with open('inventory.csv') as csvfile:
        incoming_data = csv.reader(csvfile)
        # Skip the header row
        next(incoming_data)
        for row in incoming_data:  
            product_exists = session.query(Product).filter(Product.product_name==row[0]).one_or_none()
            if product_exists == None:      
                product_name = clean_product(row[0])
                product_price = clean_price(row[1])
                product_quantity = int(row[2])
                date_updated = clean_date(row[3])
                new_product = Product(product_name = product_name, product_quantity = product_quantity, product_price = product_price, date_updated=date_updated)
                session.add(new_product)            
        
        session.commit()




def app():
    app_running = True
    while app_running:
        # if the db is empty, read in the csv
        add_csv()
        menu()
        







if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app = app()
   