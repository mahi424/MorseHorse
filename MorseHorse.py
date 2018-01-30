# import argparse
import easygui
from easygui import *

MorseCode= { 
					'A':".-", 'B':'-...',
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
                    # 'AB':'ttt',
                    # ', ':'--..--', '.':'.-.-.-',
                    # '?':'..--..', '/':'-..-.', '-':'-....-',
                    # '(':'-.--.', ')':'-.--.-'
                    }


# inv_map={'---': 'O', '--.': 'G', '-...': 'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q', '--..': 'Z', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '-.-.': 'C', '..-.': 'F', '-.--': 'Y', '-': 'T', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '.----': '1', '-----': '0', '-.-': 'K', '-..': 'D', '----.': '9', '-....': '6', '.---': 'J', '.--.': 'P', '....-': '4', '--': 'M', '-.': 'N', '....': 'H', '---..': '8', '...-': 'V', '--...': '7', '.....': '5', '...--': '3'}

def MorseCodeGen(data):
	result = ''
	for char in data:
		if str(char).isalnum():
			result += MorseCode[char.upper()]+'   '
		elif char==' ':
			result += '       '
	# print result
	return result

def MorseCodeDec(data,inv_map):
	print 'Called'
	count=0;
	# data='.-'
	result = ''
	temp= ''
	# temp=temp+data
	# print data
	data=data+'   '
	for char in data:
		if char=='.' or char =='-':
			temp=temp+char
			# print temp
			count=0
		else:
			count=count+1
			if count==3:
				result=result+inv_map[str(temp)]
				# print inv_map[str(temp)]
				temp=''
			elif count==7:
				result=result+' '

	return result
			# print count
		# elif char==' ':
		# 	result=result+inv_map[str(temp)]
		# 	print result
		# 	temp=''

			# count+=1;
			# print count
			# if count==1:
			# 	print temp
			# 	result=result+inv_map[str(temp)]
			# 	temp=''
			# elif count==7:
			# 	result=result+' '
		# else:
		# 	result=result+inv_map[temp]
	# result=result+' '+'hi'
	# print result
			


def fromconsole():
	msg ="Enter You Text"
	title = "MorseHorse"
	str_input = enterbox(msg, title)
	# str_input = str_input.rstrip("\n\r")
	print 'recieved'+str_input
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
	# print len(MorseCode)
	inv_map = {v: k for k, v in MorseCode.iteritems()}
	# print inv_map
	msg ="How Do You Like It?"
	title = "MorseHorse : Morse Code To Plain Text Conversion Mode"
	choices = ["From console to console","From console to text file","From text file to console","From text file to text file" ]
	choice = choicebox(msg, title, choices)
	if choice=="From console to console":
		str_input=fromconsole()
		result=MorseCodeDec(str_input,inv_map)
		toconsole(result)

	# print inv_map['-...']
	# print len(inv_map)
	# print str(inv_map)
	# print "yes"

	elif choice=="From console to text file":
		str_input=fromconsole()
		result=MorseCodeDec(str_input)
		tofile(result)
	#################################################################################################################
	# from file to console
	elif choice=="From text file to console":
		str_input=fromfile()
		result=MorseCodeDec(str_input)
		toconsole(result)
	#################################################################################################################
	# from file to file
	elif choice=="From text file to text file":
		str_input=fromfile()
		result=MorseCodeDec(str_input)
		tofile(result)
	else:
		print "Error!!!"

else:
	msg ="How Do You Like It?"
	title = "MorseHorse : Plain Text To Morse Code Conversion Mode"
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


