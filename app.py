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
        submenu(selected)
    else:
        input('''
                \n Your selection was not valid.
                \r Press enter to review your options and try again.
            ''')

def submenu(selection):
    if selection == "V":
        requested_id = input("Enter ID of product ")
        display_product(requested_id)
    elif selection == "A":
        print("Add new product")
    elif selection =="B":
        print("Export DB")
    else:
        pass


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

def clean_id():
    pass


def display_product(product_id):
    # get inputted id
    # query for item with matching id
    selected_product = session.query(Product).filter(Product.product_id==product_id).first()
    # return product info
  
    print(selected_product)

def add_product():
    pass

def update_product():
    pass

def delete_product():
    pass

def export_csv():
    pass



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
                product_name = row[0]
                product_price = clean_price(row[1])
                product_quantity = int(row[2])
                date_updated = clean_date(row[3])
                new_product = Product(product_name = product_name, product_quantity = product_quantity, product_price = product_price, date_updated=date_updated)
                print(new_product)
                session.add(new_product)
        
        session.commit()
          
   
   

# def add_csv():
#     with open('suggested_books.csv') as csvfile:
#         data = csv.reader(csvfile)
#         for row in data:
#             book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
#             if book_in_db == None:
#                 date = clean_date(row[2])
#                 title = row[0]
#                 author = row[1]
#                 price = clean_price(row[3])
#                 new_book = Book(title = title,author = author, published_date = date, price = price)
#                 session.add(new_book)

#         session.commit()
            





def app():
    app_running = True
    while app_running:
        menu()







if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()
    #add_csv()
    #clean_date("2019/2/21")
   