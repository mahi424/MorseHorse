import easygui
from easygui import *

MorseCode={ 
'A':".-", 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
 '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', 
 ',':'--..--', '.':'.-.-.-','?':'..--..','/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'
 }

def MorseCodeGen(data):
	result = ''
	for char in data:
		if str(char).isalnum():
			result += MorseCode[char.upper()]+'   '
		elif char==' ':
			result += '       '
	return result

def MorseCodeDec(data,inv_map):
	print 'Called'
	count=0;
	result = ''
	temp= ''
	data=data+'   '
	for char in data:
		if char=='.' or char =='-':
			temp=temp+char
			count=0
		else:
			count=count+1
			if count==3:
				result=result+inv_map[str(temp)]
				temp=''
			elif count==7:
				result=result+' '

	return result

def fromconsole():
	msg ="Enter You Text"
	title = "MorseHorse"
	str_input = enterbox(msg, title)
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
	title ="MorseHorse"
	msgbox(msg,title, ok_button="Good job!")





msg ="What Can I Do For You?"
title ="MorseHorse"
choices =["Morse Code To Text","Text To Morse Code"]
choice = choicebox(msg, title, choices)

if choice=="Morse Code To Text":
	inv_map = {v: k for k, v in MorseCode.iteritems()}
	msg ="How Do You Like It?"
	title = "MorseHorse : Morse Code To Plain Text Conversion Mode"
	choices = ["From console to console","From console to text file","From text file to console","From text file to text file" ]
	choice = choicebox(msg, title, choices)
	if choice=="From console to console":
		str_input=fromconsole()
		result=MorseCodeDec(str_input,inv_map)
		toconsole(result)
	elif choice=="From console to text file":
		str_input=fromconsole()
		result=MorseCodeDec(str_input)
		tofile(result)
	elif choice=="From text file to console":
		str_input=fromfile()
		result=MorseCodeDec(str_input)
		toconsole(result)
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
	if choice=="From console to console":
		str_input=fromconsole()
		result=MorseCodeGen(str_input)
		toconsole(result)
	elif choice=="From console to text file":
		str_input=fromconsole()
		result=MorseCodeGen(str_input)
		tofile(result)
	elif choice=="From text file to console":
		str_input=fromfile()
		result=MorseCodeGen(str_input)
		toconsole(result)
	elif choice=="From text file to text file":
		str_input=fromfile()
		result=MorseCodeGen(str_input)
		tofile(result)
	else:
		print "Error!!!"


