#Prevents writing of pycache file
import sys
sys.dont_write_bytecode = True
#sys.dont_write_bytecode=1

#standard imports
import yaml, json, glob, csv
import random, re, time, os
from datetime import datetime

def write_csv(my_header, my_rows, file_name):
	header = my_header
	rows = my_rows
	filename = file_name
	    
	# newline avoids blanks lines on windows
	with open(filename, 'w', newline='') as csvfile:  
	    csvwriter = csv.writer(csvfile) 
	    csvwriter.writerow(header) 
	    csvwriter.writerows(rows)

def get_address_list(filename, locale):
	with open(filename, encoding="utf8") as file:
		# The FullLoader parameter handles the conversion from YAML
		# scalar values to Python the dictionary format
		file = yaml.load(file, Loader=yaml.FullLoader)
		data = file[locale]
	return data

def get_product_list(filename):
	with open(filename, encoding="utf8") as file:
		data = yaml.load(file, Loader=yaml.FullLoader)
	return data

def get_user_input(question, default):
	userinput = input(question) or default
	return userinput

def get_single_product(product_list):
	product = product_list[random.randint(1,len(product_list))]
	return product

def get_single_address(address_list):
	address = address_list[random.randint(1,len(address_list))]
	return address

def get_gift_message():
	gift_list = ("Gift Message 1", "Gift Message 2", "Gift Message 3", "Gift Message 4" )
	return str(random.sample(gift_list, 1)[0])

def get_notes(text = 'short'):
	good = ("Thanks for explaining the word “many” to me, it means a lot.",
	 	"I can’t believe I got fired from the calendar factory. All I did was take a day off!",
	 	"Did you hear about the guy whose whole left side got amputated? He’s all right now.",
	 	"I find it ironic that the colors red, white, and blue stand for freedom until they are flashing behind you.",
	 	"Don’t spell part backward. It’s a trap.")
	short = ('ad', 'adipiscing', 'aliqua', 'aliquip', 'amet', 'anim', 'aute', 'cillum', 'commodo',
         'consectetur', 'consequat', 'culpa', 'cupidatat', 'deserunt', 'do', 'dolor', 'dolore',
         'duis', 'ea', 'eiusmod', 'elit', 'enim', 'esse', 'est', 'et', 'eu', 'ex', 'excepteur',
         'exercitation', 'fugiat', 'id', 'in', 'incididunt', 'ipsum', 'irure', 'labore', 'laboris',
         'laborum', 'lorem', 'magna', 'minim', 'mollit', 'nisi', 'non', 'nostrud', 'nulla',
         'occaecat', 'officia', 'pariatur', 'proident', 'qui', 'quis', 'reprehenderit', 'sed',
         'sint', 'sit', 'sunt', 'tempor', 'ullamco', 'ut', 'velit', 'veniam', 'voluptate')
	bork = ("Testing «ταБЬℓσ»: 1<2 & 4+1>3, now 20%% off!")
	if(text =='good'):
		return str(random.sample(good, 1)[0])
	elif(text =='short'):
		return str(random.sample(short, 1)[0])
	else:
		return str(random.sample(bork, 1)[0])

def get_formatted_date():
	date = datetime.now()
	formatted_date = date.strftime("%m-%d-%y")
	return formatted_date