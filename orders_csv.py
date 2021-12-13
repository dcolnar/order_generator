# Prevents writing of pycache file
# Must be at top of file
import sys
sys.dont_write_bytecode = True
# sys.dont_write_bytecode=1

#used function imports
import yaml, csv, random, math
from datetime import datetime
from helpers import *

def check_order_num():
    answer = input("Please enter number of orders: ") or "50"
    # Dummy Check
    try:
        answer = int(answer)
    except:
        answer = 50

    return answer

def check_locale():
    answer = input("Please enter locale(domestic, canada, international): ") or "domestic"
    # Dummy Check
    if answer == 'domestic' or answer == 'international' or answer == 'canada':
        answer == answer
    else:
        answer = 'domestic'

    return answer

def check_multi_order():
    answer = input("Use multi-line orders (y/n)?: ").lower() or "y"
    # Dummy Check
    if answer == 'y' or answer == 'n':
        answer == answer
    else:
        answer = 'n'

    return answer

def get_order_number(current_order_num, number_of_orders, is_multi_order):
    now = datetime.now()
    now_time = now.strftime("%Y%m%d_%H%M%S")
    value = multi_order(number_of_orders, current_order_num, is_multi_order)
    return now_time+"_"+str(value)

def get_order_quantity(num):
    num = random.randint(1, num)
    return num 

def multi_order(current_order_num, number_of_orders, is_multi_order):
    if is_multi_order == 'y':
        set_range = 10

        if current_order_num % set_range ==0:
            return current_order_num
        else:
            temp_num = math.ceil((current_order_num / set_range))
            return set_range * temp_num
    else:
        return current_order_num

def build_csv():
    header = ['Amount Paid', 'Buyer Full Name', 'Custom Field 1',
        'Custom Field 2', 'Custom Field 3', 'Date Paid',
        'Height(in)', 'Length(in)', 'Order #',
        'Order Date', 'Order Source', 'Order Total',
        'Shipping Paid', 'Shipping Serivce', 'Tax',
        'Weight(oz)', 'Width(in)', 'Address Ln 1',
        'Address Ln 2', 'Address Ln 3', 'Buyer Email',
        'Buyer First Name', 'Buyer Last Name', 'Buyer Phone',
        'Buyer Username', 'City', 'Country Code',
        'Postal Code', 'Recipient Company', 'Recipient First Name',
        'Recipient Full Name', 'Recipient Last Name',
        'Recipient Phone', 'State', 'Item Marketplace ID',
        'Item Name', 'Item Options', 'Item Quantity',
        'Item SKU', 'Item Unit Price', 'Item Warehouse',
        'Item Weight(oz)', 'Gift Flag', 'Gift Message',
        'Interal Notes', 'Notes from the Buyer', 'Notes to the Buyer']

    ################## Spacer ##################

    num = check_order_num()

    ################## Spacer ##################
    
    locale = check_locale()

    ################## Spacer ##################
    
    is_multi_order = check_multi_order()

    ################## Spacer ##################
    
    my_file_name = str(num)+"_"+locale+".csv"
    product_list = get_product_list("products.yml")
    # Roughly 2% of the addresses are not validating in SS, 
    # even though they are valid addresses.
    # Should start making note of these and remove them from YAML file.
    address_list = get_address_list("address.yml", locale)
   
    ################## Spacer ##################
    #Make Row
    rows = []
    for i in range(num):
        row = []
        product = get_single_product(product_list)
        address = get_single_address(address_list)
        quantity= get_order_quantity(5)
        order_amount = quantity * product["price"]
        # Should either add shipping cost to product file or calculate it somehow
        shipping = 10
        # Added fixed tax rate to the original with shipping cost and rounding to two decimals
        amount_paid = round((order_amount*.0825) + order_amount + shipping,2)
        buyer_full_name = address["first_name"] +" " + address["last_name"]
        custom_field_1 = ''
        custom_field_2 = ''
        custom_field_3 = ''
        if(i%3 ==0):
            custom_field_1 = get_notes()
        if(i%6 ==0):
            custom_field_2 = get_notes()
        if(i%3 == 0 and i%6 == 0):
            custom_field_3 = get_notes()
        date_paid = get_formatted_date()
        height_in = get_order_quantity(3)
        length_in = get_order_quantity(3)
        order_number = get_order_number(num, i, is_multi_order)
        order_date = get_formatted_date()
        order_source = ''
        order_total = amount_paid
        shipping_paid = shipping
        shipping_serivce = product["service"]
        # Should get variable tax rate for fun later
        tax = round((amount_paid*.0825), 2)
        weight_oz = product["weight"]
        width_in = get_order_quantity(3)
        address_ln_1 = address["ln1"]
        address_ln_2 = address["ln2"]
        address_ln_3 = ''
        buyer_email = address["email"]
        buyer_first_name = address["first_name"]
        buyer_last_name = address["last_name"]
        buyer_phone = address["phone"]
        buyer_username = address["email"]
        city = address["city"]
        country_code = address["country"]
        postal_code = address["zip"]
        recipient_company = address["company"]
        recipient_first_name = address["first_name"]
        recipient_full_name = address["first_name"] +" " + address["last_name"]
        recipient_last_name = address["last_name"]
        recipient_phone = address["phone"]
        state = address["state"]
        item_marketplace_id = ''
        item_name = product["product_name"]
        item_options = ''
        item_quantity = quantity
        item_sku = product["sku"]
        item_unit_price = product["price"]
        item_warehouse = product["order_source"]
        item_weight_oz = product["weight"]
        gift_flag = str(bool(random.getrandbits(1))).lower()
        if gift_flag == 'true':
            gift_message = get_gift_message()
        else:
            gift_message = ''
        if(i%10==0):
            interal_notes = get_notes("good")
            notes_from_the_buyer = get_notes("good")
            notes_to_the_buyer = get_notes("good")
        else:
            interal_notes = ''
            notes_from_the_buyer = ''
            notes_to_the_buyer = ''
        
        row.extend([[amount_paid, buyer_full_name, custom_field_1, custom_field_2,
            custom_field_3, date_paid, height_in, length_in, order_number, 
            order_date, order_source, order_total, shipping_paid, shipping_serivce,
            tax, weight_oz, width_in, address_ln_1, address_ln_2, address_ln_3, 
            buyer_email, buyer_first_name, buyer_last_name, buyer_phone,
            buyer_username, city, country_code, postal_code, recipient_company, 
            recipient_first_name, recipient_full_name, recipient_last_name, 
            recipient_phone, state, item_marketplace_id, item_name, item_options, 
            item_quantity, item_sku, item_unit_price, item_warehouse, item_weight_oz,
            gift_flag, gift_message, interal_notes, notes_from_the_buyer, notes_to_the_buyer]])
        # Add  to rows
        rows.extend(row)

    # Write rows to csv
    write_csv(header, rows, my_file_name)

build_csv()
