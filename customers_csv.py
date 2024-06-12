# Prevents writing of pycache file
import sys

sys.dont_write_bytecode = True

from helpers import *


def build_csv() -> None:
    # CSV header
    header = ['Full Name', 'First Name', 'Last Name', 'Company Name', 'Phone Number', 'Email Address',
              'Username', 'Address Line 1', 'Address Line 2', 'City', 'State', 'Postal Code', 'Country Code']
    rows = []

    # Get the number of customers
    num = input("Please enter number of customers: ") or "10"
    try:
        num = int(num)
    except ValueError:
        num = 10

    # Get the address list from YAML file
    address_list = get_address_list("address.yml", "domestic")
    my_file_name = f"{num}_customers.csv"

    # Generate customer data
    for i in range(num):
        row = []
        address = get_single_address(address_list)

        full_name = f"{address['first_name']} {address['last_name']}"
        first_name = address["first_name"]
        last_name = address["last_name"]
        company_name = address["company"]
        phone_number = address["phone"]
        email_address = address["email"]
        username = address["email"]
        address_line_1 = address["ln1"]
        address_line_2 = address["ln2"]
        city = address["city"]
        state = address["state"]
        postal_code = address["zip"]
        country_code = address["country"]

        row.append([full_name, first_name, last_name, company_name, phone_number, email_address, username,
                    address_line_1, address_line_2, city, state, postal_code, country_code])

        rows.extend(row)

    # Write rows to CSV file
    write_csv(header, rows, my_file_name)


build_csv()
