import requests
import datetime
import services

#colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

#header
print(f"{green}{bold}\t\t{underline}[Megumin?!]{end}")

print()
print(f"{bold}fixed by{end}", end="")
print(f"{green}{bold} >> {end}", end = "")
print(f"{cyan}{bold}sy{end}")

# Logo
print('''

▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀ ░█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀█ 
▒█▒█▒█ ▒█▄▄█ ▒█░▄▄ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░ ▒█▄▄█ ░▀▀▀▄▄ ▒█▒█▒█ ▒█▀▀▄ 
▒█░░▒█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░░▀█ ░▒█░░ ▒█░▒█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄█

''')

#inputs
print('only rus\nnumber\nexample: 9996667711')
input_number = input(green + bold + '>> ' + end)
print('how???')
sms = int(input(green + bold + '>> ' + end))



def parse_number(number):
	msg = f"[*]check number - {green}{bold}OK{end}"
	if int(len(number)) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]check number - {red}{bold}failed number!{end}\nThis bomber is intended only for Russia and if the number you entered belongs to another country then alas this bomber is not suitable for you!")
		quit()
	return number
number = parse_number(input_number)



services.attack(number, sms)
