# Prevents writing of pycache file
# Must be at top of file
import sys

sys.dont_write_bytecode = True

# Used function imports
import math
from helpers import *


def check_order_num() -> int:
    answer = input("Please enter number of orders: ") or "50"
    try:
        return int(answer)
    except ValueError:
        return 50


def check_locale() -> str:
    answer = input("Please enter locale(domestic, canada, international): ") or "domestic"
    if answer in ['domestic', 'canada', 'international']:
        return answer
    return 'domestic'


def check_multi_order() -> str:
    answer = input("Use multi-line orders (y/n)?: ").lower() or "y"
    return 'y' if answer == 'y' else 'n'


def get_order_number(current_order_num: int, number_of_orders: int, is_multi_order: str) -> str:
    now = datetime.now()
    now_time = now.strftime("%Y%m%d_%H%M%S")
    value = multi_order(current_order_num, number_of_orders, is_multi_order)
    return f"{now_time}_{value}"


def get_order_quantity(num: int) -> int:
    return random.randint(1, num)


def multi_order(current_order_num: int, number_of_orders: int, is_multi_order: str) -> int:
    if is_multi_order == 'y':
        set_range = 10
        if current_order_num % set_range == 0:
            return current_order_num
        temp_num = math.ceil(current_order_num / set_range)
        return set_range * temp_num
    return current_order_num


def build_csv() -> None:
    header = [
        'Amount Paid', 'Buyer Full Name', 'Custom Field 1', 'Custom Field 2', 'Custom Field 3',
        'Date Paid', 'Height(in)', 'Length(in)', 'Order #', 'Order Date', 'Order Source',
        'Order Total', 'Shipping Paid', 'Shipping Service', 'Tax', 'Weight(oz)', 'Width(in)',
        'Address Line 1', 'Address Line 2', 'Address Line 3', 'Buyer Email', 'Buyer First Name',
        'Buyer Last Name', 'Buyer Phone', 'Buyer Username', 'City', 'Country Code', 'Postal Code',
        'Recipient Company', 'Recipient First Name', 'Recipient Full Name', 'Recipient Last Name',
        'Recipient Phone', 'State', 'Item Marketplace ID', 'Item Name', 'Item Options',
        'Item Quantity', 'Item SKU', 'Item Unit Price', 'Item Warehouse Location', 'Item Weight (oz)',
        'Gift Flag', 'Gift Message', 'Internal Notes', 'Notes from the Buyer', 'Notes to the Buyer'
    ]

    # Get user inputs for the number of orders, locale, and multi-order option
    num = check_order_num()
    locale = check_locale()
    is_multi_order = check_multi_order()

    # Set the output file name based on the number of orders and locale
    my_file_name = f"{num}_{locale}.csv"

    # Load product and address data
    product_list = get_product_list("products.yml")
    address_list = get_address_list("address.yml", locale)

    # Initialize rows for the CSV
    rows = []

    # Generate order details
    for i in range(1, num + 1):
        row = []
        product = get_single_product(product_list)
        address = get_single_address(address_list)
        quantity = get_order_quantity(5)
        order_amount = quantity * product["price"]
        shipping = 10
        amount_paid = round(order_amount * 1.0825 + shipping, 2)
        buyer_full_name = f"{address['first_name']} {address['last_name']}"

        custom_field_1 = get_notes() if i % 3 == 0 else ''
        custom_field_2 = get_notes() if i % 6 == 0 else ''
        custom_field_3 = get_notes() if i % 3 == 0 and i % 6 == 0 else ''

        order_number = get_order_number(i, num, is_multi_order)
        order_date = get_formatted_date()
        order_total = amount_paid
        tax = round(amount_paid * 0.0825, 2)
        gift_flag = str(bool(random.getrandbits(1))).lower()
        gift_message = get_gift_message() if gift_flag == 'true' else ''

        internal_notes = get_notes("good") if i % 10 == 0 else ''
        notes_from_the_buyer = get_notes("good") if i % 10 == 0 else ''
        notes_to_the_buyer = get_notes("good") if i % 10 == 0 else ''

        row = [
            amount_paid, buyer_full_name, custom_field_1, custom_field_2, custom_field_3, '',
            get_order_quantity(3), get_order_quantity(3), order_number, order_date, '',
            order_total, shipping, product["service"], tax, product["weight"], get_order_quantity(3),
            address["ln1"], address["ln2"], '', address["email"], address["first_name"], address["last_name"],
            address["phone"], address["email"], address["city"], address["country"], address["zip"],
            address["company"], address["first_name"], buyer_full_name, address["last_name"], address["phone"],
            address["state"], '', product["product_name"], '', quantity, product["sku"], product["price"],
            product["order_source"], product["weight"], gift_flag, gift_message, internal_notes,
            notes_from_the_buyer, notes_to_the_buyer
        ]

        rows.append(row)

    # Write rows to CSV
    write_csv(header, rows, my_file_name)


build_csv()
