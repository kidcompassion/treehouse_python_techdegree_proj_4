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


def clean_date(date_str):
    
    cleaned_date = date_str.split('/')
    #return cleaned_date
    formatted_date = datetime.date(int(cleaned_date[2]), int(cleaned_date[0]), int(cleaned_date[1]))
    return formatted_date

def clean_price(price_str):
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
    counter = 0
    with open('inventory.csv') as csvfile:
        incoming_data = csv.reader(csvfile)
        #
        next(incoming_data)
        
        for row in incoming_data:  
            print(clean_date(row[3]))
                
            #pass
        #filter out header cell
            # Check if the product already exists
            #product_exists = session.query(Product).filter(Product.product_name == row[0]).one_or_none()
                
            # product_name = row[0]
            # product_price = row[1]
            # product_quantity = row[2]
            # date_updated = clean_date(row[3])
            # new_product = Product(product_name = product_name, product_quantity = product_quantity, product_price = product_price, date_updated=date_updated)
            # print(new_product)
            #session.add(new_product)
        
       # session.commit()
          
   
   

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
    #clean_date("2019/2/21")
   