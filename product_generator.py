# Prevents writing of pycache file
import sys
sys.dont_write_bytecode = True

# Used function imports
from helpers import *

def build_csv() -> None:
    # CSV header
    header = [
        'SKU', 'Name', 'WarehouseLocation', 'WeightOz', 'Category', 'Tag1', 'Tag2',
        'Tag3', 'Tag4', 'Tag5', 'CustomsDescription', 'CustomsValue', 'CustomsTariffNo',
        'CustomsCountry', 'ThumbnailUrl', 'UPC', 'FillSKU', 'Length', 'Width', 'Height',
        'UseProductName', 'Active', 'ParentSKU', 'IsReturnable'
    ]

    # Get the product list from YAML file
    product_list = get_product_list("products.yml")
    my_file_name = "my_products.csv"

    # Generate product data
    rows = []
    for i in range(1, 494):
        row = []
        product = get_product(product_list, i)

        SKU = product["sku"]
        Name = product["product_name"]
        WarehouseLocation = product["warehouse_location"]
        WeightOz = product["weight"]
        Category = product["category"]
        Tag1 = product["tag1"]
        Tag2 = ''
        Tag3 = ''
        Tag4 = ''
        Tag5 = ''
        CustomsDescription = product["customs_description"]
        CustomsValue = product["price"]
        CustomsTariffNo = product["customs_tarrif_no"]
        CustomsCountry = product["customs_county"]
        ThumbnailUrl = product["thumbnail_url"]
        UPC = product["upc"]
        FillSKU = product["fill_sku"]
        Length = product["length"]
        Width = product["width"]
        Height = product["height"]
        UseProductName = product["use_product_name"]
        Active = product["active"]
        ParentSKU = product["parent_sku"]
        IsReturnable = product["is_returnable"]

        row.append([
            SKU, Name, WarehouseLocation, WeightOz, Category, Tag1, Tag2, Tag3, Tag4, Tag5,
            CustomsDescription, CustomsValue, CustomsTariffNo, CustomsCountry, ThumbnailUrl,
            UPC, FillSKU, Length, Width, Height, UseProductName, Active, ParentSKU, IsReturnable
        ])
        rows.extend(row)

    # Write rows to CSV file
    write_csv(header, rows, my_file_name)

build_csv()
