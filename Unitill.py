import os

# setting change

# version number
versnum = "2.0.0"

# crash protection
num1 = 0
num2 = 0
awn = 0



os.system("clear")
print("Unitill version", versnum)
print("By: Evan Pratten")
print("")
print("__________________________________________________")
print("|---------------------[debug info]---------------|")
print("|----script id-----------------------------------|")
print("|------Unitill sparkils--------------------------|")
print("|------------------------------------------------|")
print("|-----optamized for chrome os and backtrack 5----|")
print("|------------------------------------------------|")
print("|------------------[WARNING]---------------------|")
print("|------This version will not work on windows-----|")
print("|------------------------------------------------|")
print("")
print("|-----------------Press ENTER -------------------|")
print("")
verify = input ("")
os.system("clear")

print("Unitill version", versnum)
print("By: Evan Pratten")

# main menu

print("")
print("_________________________________________________")
print("|---------------selection screen----------------|")
print("|--1. Math--------------------------------------|")
print("|--2. BibCreator--------------------------------|")
print("|-----------------------------------------------|")
print("|--99. exit-------------------------------------|")
print("|-----------------------------------------------|")



# input selection

sel1 = input(">>")

os.system("clear")
print("Unitill version", versnum)
print("By: Evan Pratten")

# bts program selection

# math program
if sel1 == '1':
	# math menu
	print("|----------------select operation----------------|")
	print("|----1.add---------------------------------------|")
	print("|----2.subtract----------------------------------|")
	print("|----3.multiply----------------------------------|")
	print("|----4.divide------------------------------------|")
	print("|----5.experimental calculator-------------------|")
	print("|------------------------------------------------|")
	print("")
	
	#select
	sel2 = input(">>")
	
	if sel2 == '1':
		os.system("clear")
		print("Unitill version", versnum)
		print("By: Evan Pratten")
		print("")
		print("You have chosen ADD")
		print("Enter the first number")
		num1 = input(">>")
		print("Enter the second number")
		num2 = input(">>")
		
		awn = num1 + num2

		print(num1, "+", num2, "=")
		print(awn)
		# reset numbers
		num1 = 0
		num2 = 0
		awn = 0		

	else:
		if sel2 == '2':
			os.system("clear")
			print("Unitill version", versnum)
			print("By: Evan Pratten")
			print("")
			print("You have chosen SUBTRACT")
			print("Enter the first number")
			num1 = input(">>")
			print("Enter the second number")
			num2 = input(">>")
			
			awn = (num1 - num2)
			print(num1, "-", num2, "=")
			print(awn)

			#reset numbers
			num1 = 0
			num2 = 0
			awn = 0
			
		else:
			if sel2 == '3':
				os.system("clear")
				print("Unitill version", versnum)
				print("By: Evan Pratten")
				Print("")
				print("You have chosen MULTIPLY")
				print("Enter the first number")
				num1 = input(">>")
				print("Enter the second number")
				num2 = input(">>")
				
				awn = num1 * num2
				print(num1, "*", num2, "=")
				#reset numbers
				num1 = 0
				num2 = 0
				awn = 0
			else:
				if sel2 == '4':
					print("Unitill version", versnum)
					print("By: Evan Pratten")
					print("")
					print("you have chosen DIVIDE")
					print("enter the first number")
					num1 = input(">>")
					print("Enter the second number")
					num2 = input(">>")
					
					awn = num1 / num2
					print(num1, "/", num2, "=")
					print(awn)
					# reset numbers
					num1 = 0
					num2 = 0
					awn = 0
				else:
					if sel2 == '5':
						print("Warning this feature is not done!")
						print("enter math here")
						m = input(">>")
						math2 = eval('m')
						print(math2)

else:
	
# bibcreator
	if sel1 == '2':
		random = 0
		
