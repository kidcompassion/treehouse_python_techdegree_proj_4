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
    selected = input(" What would you like to do?").upper()

    # Validate user's entry
    if selected in ['V','A','B']:
            return selected
    else:
        input('''
                \n Your selection was not valid.
                \r Press enter to review your options and try again.
            ''')

def submenu():
    pass



def clean_date():
    pass

def clean_price():
    pass

def clean_id():
    pass


def display_product():
    pass

def add_product():
    pass

def update_product():
    pass

def delete_product():
    pass

def export_csv():
    pass




def add_csv():
    with open('inventory.csv') as csvfile:
        incoming_data = csv.reader(csvfile)
        for row in incoming_data:
            product_name = row[0]
            product_price = row[1]
            product_quantity = row[2]
            date_updated = row[3]
            new_product = Product(product_name = product_name, product_price = product_price, product_quantity = product_quantity, date_updated=date_updated)
            print(new_product)
            #individual_product = session.query(Product).filter(Product.product_name == row[0]).one_or_none()
   
   

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
    pass







if __name__ == '__main__':
    add_csv()