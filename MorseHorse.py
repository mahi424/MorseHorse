# import argparse
import easygui
from easygui import *

MorseCode= { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----',
                    # ', ':'--..--', '.':'.-.-.-',
                    # '?':'..--..', '/':'-..-.', '-':'-....-',
                    # '(':'-.--.', ')':'-.--.-'
                    }

def MorseCodeGen(data):
	result = ''
	for char in data:
		if str(char).isalnum():
			result += MorseCode[char.upper()]+'   '
		elif char==' ':
			result += '       '
	# print result
	return result

def fromconsole():
	msg ="Enter You Text"
	title = "MorseHorse"
	str_input = enterbox(msg, title)
	str_input = str_input.rstrip("\n\r")
	return str_input


def toconsole(result):
	print result


def fromfile():
	path=easygui.fileopenbox();
	f=open(path,'r')
	str_input=f.read()
	str_input = str_input.rstrip("\n\r")
	return str_input

	

def tofile(result):
	f=open('Result.txt','w')
	f.write(result)
	f.close()
	msg ="Your Result written to Result.txt"
	title = "MorseHorse"
	msgbox(msg,title, ok_button="Good job!")



msg ="What Can I Do For You?"
title = "MorseHorse"
choices = ["Morse Code To Text","Text To Morse Code"]
choice = choicebox(msg, title, choices)

if choice=="Morse Code To Text":
	print "yes"
else:
	msg ="How Do You Like It?"
	title = "MorseHorse"
	choices = ["From console to console","From console to text file","From text file to console","From text file to text file" ]
	choice = choicebox(msg, title, choices)
	
	#################################################################################################################
	# from console to console
	if choice=="From console to console":
		str_input=fromconsole()
		result=MorseCodeGen(str_input)
		toconsole(result)
	#################################################################################################################
	# from console to file
	elif choice=="From console to text file":
		str_input=fromconsole()
		result=MorseCodeGen(str_input)
		tofile(result)
	#################################################################################################################
	# from file to console
	elif choice=="From text file to console":
		str_input=fromfile()
		result=MorseCodeGen(str_input)
		toconsole(result)
	#################################################################################################################
	# from file to file
	elif choice=="From text file to text file":
		str_input=fromfile()
		result=MorseCodeGen(str_input)
		tofile(result)
	else:
		print "Error!!!"


