# Prevents writing of pycache file
# Must be at top of file
import sys
sys.dont_write_bytecode = True
# sys.dont_write_bytecode=1

#used function imports
import yaml, csv, random, math
from datetime import datetime
from helpers import *


def build_csv():
	header = ['SKU','Name','WarehouseLocation',
	'WeightOz','Category','Tag1','Tag2','Tag3',
	'Tag4','Tag5','CustomsDescription','CustomsValue',
	'CustomsTariffNo','CustomsCountry','ThumbnailUrl',
	'UPC','FillSKU','Length','Width','Height','UseProductName',
	'Active','ParentSKU','IsReturnable']


	################## Spacer ##################

	product_list = get_product_list("products.yml")

	my_file_name = "my_products.csv"

	################## Spacer ##################
	#Make Row
	rows = []
	for i in range(1, 493+1):
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

		row.extend([[SKU,Name,WarehouseLocation,WeightOz,
			Category,Tag1,Tag2,Tag3,Tag4,Tag5,
			CustomsDescription,CustomsValue,CustomsTariffNo,
			CustomsCountry,ThumbnailUrl,UPC,FillSKU,Length,Width,
			Height,UseProductName,Active,ParentSKU,IsReturnable]])
		# Add  to rows
		rows.extend(row)

	# Write rows to csv
	write_csv(header, rows, my_file_name)

build_csv()