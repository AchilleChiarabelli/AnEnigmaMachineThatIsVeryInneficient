import time
import os
# https://www.w3schools.com/python/python_file_handling.asp

# VARIABLES
shift = 0
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
final = ""
choice = 0

# FUNCTIONS
def enigma(shift, length, script) :
	message = ""
	for i in range(length):
		char = script[i].upper()
		temp = alphabet.rfind(char) - shift
		message += alphabet[temp]
	return message

def denigma(shift, length, script):
	message = ""
	for i in range(length):
		char = script[i].upper()
		temp = alphabet.rfind(char) + shift
		while temp >= 25:
			temp -= 26
		message += alphabet[temp]
	return message

def the_full_product(shift, length , script, choice, name):
	#makes it less than 26
	while shift > 25:
		shift -= 26
	if int(choice) == 1:
		make_file(shift, length, script, name)
		print("enigmaing")
		time.sleep(2.5)
		os.system("clear")
		print("File made.")
	else:
		something = get_message(shift, name)
		print("denigmaing")
		time.sleep(2.5)
		os.system("clear")
		print("This is the uncensored text: " + something)

def make_file(shift, length, script, file_name):
	f = open(file_name.upper(), 'w')
	print("make file started")
	content = enigma(shift, length, script)
	f.write(content)
	f.close()
	
def get_message(shift, file_name):
	#add file name check
	f = open(file_name.upper(), 'r')
	thing = f.read()
	length = len(thing)
	anotherthing = denigma(shift, length, thing)
	f.close()
	return anotherthing

# MAIN

#getting all inputs for the text, shift, length, and enigma/denigma

choice = input("Would you like to enigma (1) or denigma (2) a text? ")
shift = int(input("What would you like to make the key? (insert a number 1 - infinity) "))
length = 0
script = "Nothin here"
if int(choice) == 2:
	name = input("What file would you like to denigma??? (¡ctrl + v the file name here!)").upper()
	#read the message and get length(in read message)
	the_full_product(shift, length, script, choice, name)
else:
	script = input("What would you like enigma??? ").upper()
	length = len(script)
	name = input("What would you like to name the message??? ")
	the_full_product(shift, length, script, choice, name)