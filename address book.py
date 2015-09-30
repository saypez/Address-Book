#==================================================( Slicing List )=============================================================================================================
#this function read all the lines of the list and seperate it accordig to some special character
def sliceList(List):
	i = 0
	for item in List: 													#this loop split each item of the list based on defined spliters
		List[i] = List[i][:len(List[i])-1] 								#removeing "/n" character from end of each item
		List[i] = List[i].split("%") 									#seperating each line by the "%" charachter
		List[i][1]= List[i][1].split("?") 								#seperating different numbers by the "?" charachter
		List[i][2]= List[i][2].split("|")								#seperating different address by the "|" charachter
		List[i][3]= List[i][3].split(";") 								#seperating different e-mail address by the ":" charachter
		i = i+1
	return List
#==================================================( Joining Data )===============================================================================================================
def joinList(List):
	i = 0
	for item in List: 													#this loop split each item of the list based on defined spliters
		List[i][3]= ";".join(List[i][3]) 								#seperating different e-mail address by the ":" charachter
		List[i][2]= "|".join(List[i][2])								#seperating different address by the "|" charachter
		List[i][1]= "?".join(List[i][1]) 								#seperating different numbers by the "?" charachter
		List[i] = "%".join(List[i])
		List[i] = str(List[i])+"\n"										#seperating each line by the "%" charachter
		i = i+1
	return List
#==================================================( List to File )=============================================================================================================
def listTofile(List,addressBookFile):
	for line in List:
		addressBookFile.write(line)
	addressBookFile.close()	
#==================================================( Sort File )==============================================================================================================
# this function is to read the file and sort it based on the name 	
def sortFile():
	addressBookFile = open("address book.txt","r+")
	fileList = addressBookFile.readlines()
	for item in fileList:
		item[0].upper()
	fileList.sort(key = str.lower)
	addressBookFile.seek(0)
	for line in fileList:
		addressBookFile.write(str(line))
	addressBookFile.close()	
#==================================================( Search )===================================================================================================================
def search(searchStr):
	searchList = []											        # a list of records finded by search function
	addressBookFile = open("address book.txt","r")
	fileList = addressBookFile.readlines()								        # converting the file to a list
	addressBookFile.close()
	for line in fileList:											# searching through the all file
		if line.find(searchStr) != -1 :									# this "if" cheks to see if the string is in this line of address book or not
			searchList.append(line)									# appending this line to the searchList	
	if searchList != []:
		sliceList(searchList)
	return searchList
#==================================================( Delete )===================================================================================================================
def delete():
	delItem = []															#it is a list that we want to delete
	delSearchList = []														#this list holds the search result for deleting
	delStr = raw_input("Please write the name or telephone number that you want to delete or write cancel : ")                      #ask user to input somthing for del
	while delStr.upper() != "CANCEL":
		delSearchList = search(delStr)										                #it search testring inputet by user to find the address book by search function
		if delSearchList != []:												        #if find something to delete
			print ""
			showList(delSearchList)											        # show the items finded by search function
			delSelection = raw_input("Select the number of contact that you want to delete or type cancel to skip: ")	#which item user wants to delete
			if delSelection.upper() != "CANCEL":
				if delSelection.isdigit() and 0 < int(delSelection) and int(delSelection)<= len(delSearchList):
					delLineList = delSearchList[int(delSelection)-1]						#finding the exact line for delete
					delItem.append(delLineList)
					delItem = joinList(delItem)
					addressBookFile= open("address book.txt", "r")							#reading the whole file and puting it into a new list
					fileList = addressBookFile.readlines() 								#list of the whole file
					addressBookFile.close()
					fileList.remove(str(delItem[0]))								#removing the delet Item from newList
					addressBookFile = open("address book.txt", "w")							#over writing the newList to the file
					listTofile(fileList,addressBookFile)
					print "The accout: ","'",delSearchList[int(delSelection)-1][0],"'", "was deleted successfully"
					delStr = "CANCEL"
				else:
					print ""
					print "Not valid selection!"
					print "You must select integer between 1 and", len(delSearchList)
					print ""
			else:
				delStr = "CANCEL"
				print ""
				print "Delete process has been aborted."
				print ""
		else:
			delStr = "CANCEL"
			print "The input contact could not find!"
#==================================================( Show )=====================================================================================================================
#This procedure get a list in the format that provide by slicingList() procedure and shows it on scereen.
def showList(List):
	nameCounter=0													# A counter to count the number of names in the address book.
	phoneCounter=0													# A counter to count the number of phones in a contact.
	addressCounter=0												# A counter to count the number of addresses in a contact.
	emailCounter=0													# A counter to count the number of emails in a contact.
	print 160*"_"
	print '{:^4}'.format(''),"|",'{:^32}'.format('Fullname'),"|",'{:^30}'.format('Phone Number'),"|",'{:^50}'.format('Address'),"|",'{:^30}'.format('Email'),"|"	# Preant a heading for the table of contants which will be shown
	print 160*"_"
	for nameItem in List:
		for phoneItem in List[nameCounter][1]:						#===========================================================================#
			phoneCounter +=1										#																			#
		for addressItem in List[nameCounter][2]:					#																			#
			addressCounter +=1										#In this three for loops the number of phones, addresses and emails counted.#
		for emailItem in List[nameCounter][3]:						#																			#
			emailCounter +=1										#===========================================================================#
		rowNumber = max(phoneCounter,addressCounter,emailCounter)		# rowNumber get the maximum number among phones, addresses and emails of a contacs that need when a contact is shown on screen.
		newList = [["" for x in xrange(4)] for y in xrange(rowNumber)]	# This list contain a four column(fullname, phone number, address, email) and the number of rows is equal to rowNumber. Each field will field with only one string of phones or emails or addresses 
		newList[0][0] = List[nameCounter][0]						#===========================================================================#
		for i in range(0,phoneCounter):								#																			#
			newList[i][1] = List[nameCounter][1][i]					#																			#
		for i in range(0,addressCounter):							#In this three  for loops newList is filled by detail information of one	#
			newList[i][2] = List[nameCounter][2][i]					#contacts that indicate bye nameCounter.									#
		for i in range(0,emailCounter):								#																			#
			newList[i][3] = List[nameCounter][3][i]					#===========================================================================#
		
		for i in xrange(0,rowNumber):								#In this for loop all rows of newList that contains detail information of one contacs shows on screen. 
			for j in xrange(0,4):
				if i ==0 and j == 0:								#In this if checks to show the number of contacts only one time in the first row.
					print '{:<4}'.format(str(nameCounter+1)),"|",'{:^32}'.format(newList[i][j]),"|",	# number of contacts are shown on the left of 4 characters and name of the contact in center of 32 characters
				elif j == 0:										#for the other rows of newList nothing shows in field number and name	
					print '{:<4}'.format(""),"|",'{:^32}'.format(newList[i][j]),"|",
				elif j!= 2:
					print '{:^30}'.format(newList[i][j]),"|",		#Phone numbers of contacts are shown in center of 30 characters
				else:
					print '{:^50}'.format(newList[i][j]),"|",		#Address of contacts are shown in center of 50 characters
			print													# This print put cursor to new line on screen after a row of newList has been shown.
		print 160 * "_"
		nameCounter += 1											#========================================================#
		phoneCounter=0												#nameCounter increment to show next contact.			 #
		addressCounter=0											#all other counters refresh to zero for the next contact.#
		emailCounter=0												#========================================================#
#==================================================( Get Fullname )=============================================================================================================
#This functin get a name and checks if it is in proper format and return it by full_name.
def getFullname():
	special_chars = ["%","?","|",";"]								#These characters are used for separating different field of a contacts in file. So they are reserved for that purpose.
	print "Full name cannot contain: ? % | ;"
	while_flag = True												#This flag use in the following while loop to keep user in this function in order to enter a proper name or type cancel to exit.
	while while_flag:
		print "Type cancel to cancel"
		full_name = raw_input("Please enter full name: ")			#full_name is an string which contains a name and getFullname returns it.
		validity_flag = True										#This flag is used to determine whether the input name is in proper format or not.
		if full_name.upper() == "CANCEL" or "":						#This if condition checks if user enter cancel or leaves the name blank and return None.
			return None
		else:
			for i in range (0,len(full_name)):						#===============================================================================#
				if full_name[i] in special_chars:					#In tihs for loop full_name is checked that not contains special characters.	#
					validity_flag = False							#===============================================================================#
			if validity_flag == False or full_name == "":			#In This if condition gives proper information to user if the input name wouldn't in the proper format.
				print ""
				print "The input full name was not valid!"
				print "It cannot be empty or contains these special characters: ? % | ;"
			else:
				print ""
				return full_name
#==================================================( Get Phone )================================================================================================================
#This functin get a phone number and checks if it is in proper format and return it by phone_input.
def getPhone():
	valid_phone_char = ["1","2","3","4","5","6","7","8","9","0","#","*","p","P"]	#valid_phone_char is a list that contains all possible characters in a phone numbers.
	print "Phone number can contains only digits, +, * and p"
	while_flag = True																#This flag use in the following while loop to keep user in this function in order to enter a proper phone number or type cancel to exit.
	while while_flag:
		print "Type cancel to cancel."
		phone_input = raw_input("Please enter phone number: ")						#phone_input is an string which contains a phone number and getPhone returns it.
		validity_flag = True														#This flag is used to determine whether the input phone number is in proper format or not.
		if phone_input.upper() == "CANCEL" or phone_input == "":					#This if condition checks if user enter cancel or leaves the phone number blank and return "".
			print "Phone number has been skipped."
			print ""
			return ""
		else:
			for i in range (0,len(phone_input)):									#===============================================================================#
				if not (phone_input[i] in valid_phone_char):						#In tihs for loop phone number is checked that contains only valid_phone_char.	#
					validity_flag = False											#===============================================================================#
			if validity_flag == False:												#In This if condition gives proper information to user if the input phone number wouldn't in the proper format. 
				print ""
				print "The input phone number was not valid!"
				print "It should contain only digits, +, *, # and p"
			else:
				print ""
				return phone_input
#==================================================( Get Address )==============================================================================================================
#This functin get an address and checks if it is in proper format and return it by address_input.
def getAddress():
	special_chars = ["%","?","|",";"]								#These characters are used for separating different field of a contacts in file. So they are reserved for that purpose.
	print "Address cannot contain: ? % | ;"
	while_flag = True												#This flag use in the following while loop to keep user in this function in order to enter a proper address or type cancel to exit.
	while while_flag:
		print "Type cancel to cancel."
		address_input = raw_input("Please enter address: ")			#address_input is an string which contains a address and getAddress returns it.
		validity_flag = True										#This flag is used to determine whether the input address is in proper format or not.
		if address_input.upper() == "CANCEL" or address_input == "":#This if condition checks if user enter cancel or leaves the address blank and return "".
			print "Address has been skipped."
			print ""
			return ""
		else:
			for i in range (0,len(address_input)):					#===============================================================================#
				if address_input[i] in special_chars:				#In tihs for loop address_input is checked that not contains special characters.#
					validity_flag = False							#===============================================================================#
			if validity_flag == False:								#In This if condition gives proper information to user if the input address wouldn't in the proper format.
				print ""
				print "The input address was not valid!"
				print "It cannot contains these special characters: ? % | ;"
			else:
				print ""
				return address_input
#==================================================( Get Email )================================================================================================================
#This functin get an Email and checks if it is in proper format and return it by email_input.
def getEmail():
	import re
	print "Email format is like: xxxxx@xxxx.xxx"
	while_flag = True													#This flag use in the following while loop to keep user in this function in order to enter a proper address or type cancel to exit.
	while while_flag:
		print "Type cancel to cancel."
		email_input = raw_input("Please enter email address: ")			#email_input is an string which contains an Email and getAddress returns it.
		if email_input.upper() == "CANCEL" or email_input == "":		#This if condition checks if user enter cancel or leaves the Email blank and return "".
			print "Email address has been skipped."
			print ""
			return ""
		else:
			if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email_input):	#This if condition checks email_input to be in proper Email format and if it is not gives proper information to user.
				print ""
				print "The input email address was not valid!"
				print "It should be like: xxxxx@xxxx.xxx"
			else:
				print ""
				return email_input
#==================================================( Add )======================================================================================================================
#This procedure add a new contact to "address book.txt" file by using getFullname(), getPhone(), getAddress() and getEmail() functions and finally use sortFile() procedure to sort "address book.txt" file by name of contacts. 
def add():
	record = ""											#record is a string which contains one contact as a string when a new contact add to addressbook such that name, phones, addresses and Emails separate by % phones separate by ? addresses separate by | and emails separate by ;
	phone = ""											#phone is an string which contains phones of one contact when a new contact add and each phone number separate by ?
	address = ""										#address is an string which contains addresses of one contact when a new contact add and each address separate by |
	email = ""											#email is an string which contains emails of one contact when a new contact add and each email separate by ;
	fullName = getFullname()
	if fullName == None:								#This if condintion checks user enter a name for new contact otherwise noting add to "address book.txt" file.
		command = "back"								#command is a string which keep user order and use in while loops to add more phones, addresses and emails.
	else:
		command = "a"
		while command.upper() == "A":					#In this while loop phone numbers add to a new contact while user order it by enter "a".
			phone_input = getPhone()
			if phone == "":								#This if condition use to not add ? for the first phone number and add ? between each of the phone numbers.
				phone = phone_input
			else:
				if phone_input != "":
					phone = phone + "?" + phone_input
			command = raw_input("Press (a) to add another phone number or any other key to continue.")
			print ""

		command = "a"
		while command.upper() == "A":					#In this while loop addresses add to a new contact while user order it by enter "a".
			address_input = getAddress()
			if address == "":							#This if condition use to not add | for the first address and add | between each of the addresses.
				address = address_input
			else:
				if address_input != "":
					address = address + "|" + address_input
			command = raw_input("Press (a) to add another address or any other key to continue.")
			print ""
		command = "a"
		while command.upper() == "A":					#In this while loop Emails add to a new contact while user order it by enter "a".
			email_input = getEmail()
			if email == "":								#This if condition use to not add ; for the first email and add ; between each of the emails.
				if email_input != "":
					email = email_input
			else:
				if email_input != "":
					email = email + ";" + email_input
			command = raw_input("Press (a) to add another address or any other key to continue.")
			print ""
		record = fullName + "%" + phone + "%" + address + "%" + email + "\n"	#record join fullname and all related phone numbers, addresses and emails and separate them by %.
		address_book = open("address book.txt", "a")	#===========================================================================================================#
		address_book.write(record)						#In this three lines "address book.txt" file open and record add to the end of the file then close the file.#
		address_book.close()							#===========================================================================================================#
		sortFile()										#"address book.txt" file sort by sortFile() procedure because a new line added to the end.
		print "The following contact has been added successfully:"
		showList(search(record))						#In this line shows the contact which has been added by user on screen by using search() function and showList() procedure.
#==================================================( Edit )======================================================================================================================
def edit():
	editItem = []											#editItem is a list that contains the contact which user wants to edit and all changes effect on this list.
	tempEditItem = []										#tempEditItem is a list that contains the contact which is joind by joinList() that user wants to edit but no changes are done in it.
	editSearchList = []										#editSearchList is a list that includes all contacts that found in "address book.txt" and contains the string which user input.
	editStr = raw_input("Please write the name or telephone number that you want to edit or write cancel : ") #editStr is a string that user want to search in "address book.txt" to edit it.
	while editStr.upper() != "CANCEL":						#This while loop keep user in editing process. user can cancel editing process by enter cancel.
		editSearchList = search(editStr)					#Search in "address book.txt" for user input by serach() function.
		if editSearchList != []:							#This if condition check whether there is any contact which contains editStr.
			print ""
			showList(editSearchList)						#show all the contact which include editStr by showList() procedure.
			editSelection = raw_input("Select the number of contact that you want to edit or type cancel to skip: ")	#editSelection ask user to enter the number of the contact in editSearchList which want to edit.
			if editSelection.upper() != "CANCEL":			#If user enter cancel edit process cancel.
				if editSelection.isdigit() and 0 < int(editSelection) and int(editSelection)<= len(editSearchList):		#This if condition checks user input a digit in range of editSearchList rows. If the input was wrong gives user proper information.
					editLineList = editSearchList[int(editSelection)-1]		#edit 
					editItem = [editLineList[:]]			#put selected contact by user in editItem.
					tempEditItem = joinList([editLineList[:]])	#put selected contact which is joined by joinList().
					showList(editItem)						#show the contact that user selected to edit on screen.
					command = True							#command is a flag to keep user in editing process up to enter cancel or done ideal changes. 
					while command == True:					#This while loop use to keep user in editing process of selected contact.
						print "n) Edit Name"
						print "p) Edit Phone"
						print "a) Edit Address"
						print "e) Edit Email"
						print "d) Done"
						print "Type cancel to cancel edit process."
						selectedField = raw_input("Please select which field do you want to edit: ")	#selectedField ask user to input the field that wants to change.
						#Following if/else block checks user input and start proper codes to edit selected field of selected contact.
						if selectedField.upper() == "N":	#If selectedField is "n" start to change name of selected contact.
							newName = getFullname()			#Get new name by getFullname() function.
							if  newName != None:			#Check user enter a name otherwise no changes will occur and gives proper information to user.
								editItem [0][0] = newName	#Assign new name to the slected contact for editing 
								showList(editItem)			#Show edited list to user.
							else:
								print "Editing name has been canceled!"
						elif selectedField.upper() == "P":	#If selectedField is "p" start to edit phones of selected contact.
							print ""
							print "a) Add new phone number"
							print "e) Edit or delete existing phone number"
							editCommand = raw_input("Please enter your command:")	#ask user to input an order whether want to edit or delete an existing phone number or add new one.
							if editCommand.upper() == "A":							#If	editCommand is "a" start to add new phone number to selected contact.
								newPhone = getPhone()								#Get new phone number.
								if newPhone != "":									#If there wasn't any other phone number in the selected contact it add to it.
									if editItem[0][1][0] == "":
										editItem [0][1] = [newPhone]				#new phone is added to selected contact.
									else:
										editItem [0][1].append(newPhone)			#New phone append to selectec contact.
									showList(editItem)
							elif editCommand.upper() == "E":						#If	editCommand is "e" start to edit edit or delete an existing phone number of selected contact.
								if editItem[0][1][0] == "":							#check whether there is any phone number in the selected contact to edit or not. If not, gives proper information to user.
									print ""
									print "There is no number to edit!"
									print ""
								else:
									validityCheck = False							#This flag use in the following while loop to keep user in editing phone number of selected contact.
									while validityCheck == False:					#This while loop keeps user in editing phone number of selected contact.
										numberOfPhones = 0							#This counter is used to show to user the number of phone number of selected contact.
										print 38*"_"
										print '{:^4}'.format(''),"|",'{:^30}'.format('Phone Number'),"|"	#print a title for all phone numbers of selected contact.
										print 38*"_"
										for i in editItem [0][1]:					#This for loop shows all phone numbers of selected contact on screen. 
											numberOfPhones += 1
											print '{:^4}'.format(numberOfPhones),"|",'{:^30}'.format(i),"|"										
										print 38*"_"
										slectedPhone = raw_input("Please select the phone number you want to edit or delete or type cancel:")	#slectedPhone ask user to enter the number of the phone number of the selected contact which want to edit.
										if slectedPhone.isdigit() and 0 < int(slectedPhone) and int(slectedPhone)<= numberOfPhones:				#This if condition checks user input to be a digit in range of the number of the phone number. If the input was wrong gives user proper information.
											print "To delete selected phone number leave it blank."
											newPhone = getPhone()	#Get a new phone number to replace the old one.
											if newPhone == "":		#Check if the input of new number is blank delete, the old phone number otherwise replace the old one with the new phone number.
												del(editItem[0][1][int(slectedPhone)-1])
											else:
												editItem[0][1][int(slectedPhone)-1] = newPhone
											showList(editItem)		#Show to user the edited list.
											validityCheck = True	#Assign True to get out of editing phone number.
										elif slectedPhone.upper() == "CANCEL":
											validityCheck = True
										else:
											print ""
											print "Invalid input!"
											print "You should input a digit between 1 and", numberOfPhones,"."
							else:
								print ""
								print "Invalid input command!"
								print ""
								
						elif selectedField.upper() == "A":	#If selectedField is "A" start to edit Address of selected contact.
							print ""
							print "a) Add new address "
							print "e) Edit or delete existing address "
							editCommand = raw_input("Please enter your command:")	#ask user to input an order whether want to edit or delete an existing address or add new one.
							if editCommand.upper() == "A":							#If	editCommand is "a" start to add new address to selected contact.
								newAddress = getAddress()							# get a new address
								if newAddress != "":								#If there wasn't any other address in the selected contact it add to it.
									if editItem[0][2][0] == "":				
										editItem [0][2] = [newAddress]				#new address is added to selected contact.
									else:
										editItem [0][2].append(newAddress)			#New address to selectec contact.
									showList(editItem)
							elif editCommand.upper() == "E":						#If	editCommand is "e" start to edit edit or delete an existing address of selected contact.
								if editItem[0][2][0] == "":							#check whether there is any address in the selected contact to edit or not. If not, gives proper information to user.
									print ""
									print "There is no address to edit!"
									print ""
								else:
									validityCheck = False							#This flag use in the following while loop to keep user in editing address of selected contact.
									while validityCheck == False:                   #This while loop keeps user in editing address of selected contact.                                                    
										numberOfAddresses = 0						#This counter is used to show to user the number of addresses of selected contact.
										print '{:^4}'.format(''),"|",'{:^60}'.format('Address')			#print a title for all addresses of selected contact.
										print 66*"_"
										for i in editItem [0][2]:
											numberOfAddresses += 1
											print '{:^4}'.format(numberOfAddresses),"|",'{:^60}'.format(i)										
										print ""
										slectedAddress = raw_input("Please select the address you want to edit or delete or type cancel:")		#slectedPhone ask user to enter the number of the addresses of the selected contact which want to edit.
										if slectedAddress.isdigit() and 0 < int(slectedAddress) and int(slectedAddress)<= numberOfAddresses:	#This if condition checks user input to be a digit in range of the number of the address. If the input was wrong gives user proper information.
											print "To delete selected phone number leave it blank."
											newAddress = getAddress()	#Get a new address to replace the old one.
											if newAddress == "":	#Check if the input of new address is blank, delete the old address otherwise replace the old one with the new address.
												del(editItem[0][2][int(slectedAddress)-1])
											else:
												editItem[0][2][int(slectedAddress)-1] = newAddress
											showList(editItem)		#Show to user the edited list.
											validityCheck = True	#Assign True to get out of editing address.
										elif slectedAddress.upper() == "CANCEL":
											validityCheck = True
										else:
											print ""
											print "Invalid input!"
											print "You should input a digit between 1 and", numberOfAddresses,"."
							else:
								print ""
								print "Invalid input command!"
								print ""

						elif selectedField.upper() == "E":	#If selectedField is "A" start to edit Email of selected contact.

							print ""
							print "a) Add new Email"
							print "e) Edit or delete existing Email"
							editCommand = raw_input("Please enter your command:")	#ask user to input an order whether want to edit or delete an existing Email or add new one.
							if editCommand.upper() == "A":							#If	editCommand is "a" start to add new Email to selected contact.
								newEmail = getEmail()								# get a new Email
								if newEmail != "":									#If there wasn't any other Email in the selected contact it add to it.
									if editItem[0][3][0] == "":
										editItem [0][3] = [newEmail]				#new Email is added to selected contact.
									else:
										editItem [0][3].append(newEmail)			#New email to selectec contact.
									showList(editItem)
							elif editCommand.upper() == "E":						#If	editCommand is "e" start to edit edit or delete an existing Email of selected contact.
								if editItem[0][3][0] == "":							#check whether there is any Email in the selected contact to edit or not. If not, gives proper information to user.
									print ""
									print "There is no email to edit!"
									print ""
								else:
									validityCheck = False							#This flag use in the following while loop to keep user in editing email of selected contact.
									while validityCheck == False:				 	#This while loop keeps user in editing Email of selected contact.                                                                      
										numberOfEmails = 0							#This counter is used to show to user the number of Email of selected contact.
										print '{:^4}'.format(''),"|",'{:^30}'.format('Email Address')	#print a title for all Emails of selected contact.
										print 36*"_"
										for i in editItem [0][3]:
											numberOfEmails += 1
											print '{:^4}'.format(numberOfEmails),"|",'{:^30}'.format(i)										
										print ""
										slectedEmail = raw_input("Please select the Email you want to edit or delete or type cancel:")		#slectedPhone ask user to enter the number of the Emails of the selected contact which want to edit.
										if slectedEmail.isdigit() and 0 < int(slectedEmail) and int(slectedEmail)<= numberOfEmails:			#This if condition checks user input to be a digit in range of the number of the Emails. If the input was wrong gives user proper information.
											print "To delete selected phone number leave it blank."
											newEmail = getEmail()	#Get a new Email to replace the old one.
											if newEmail == "":	#Check if the input of new Email is blank, delete the old Email otherwise replace the old one with the new Email.
												del(editItem[0][3][int(slectedEmail)-1])
											else:
												editItem[0][3][int(slectedPhone)-1] = newEmail
											showList(editItem)		#Show to user the edited list.
											validityCheck = True	#Assign True to get out of editing Email.
										elif slectedEmail.upper() == "CANCEL":
											validityCheck = True
										else:
											print ""
											print "Invalid input!"
											print "You should input a digit between 1 and", numberOfEmails,"."
							else:
								print ""
								print "Invalid input command!"
								print ""
								
						elif selectedField.upper() == "D":
							addressBookFile= open("address book.txt", "r")	#opening database to read.
							fileList = addressBookFile.readlines()			#bringing database to a list.
							addressBookFile.close()							#closing database.
							fileList.remove(str(tempEditItem[0]))			#deleting old contacts from the list.
							fileList.append(joinList(editItem)[0])			#appending edited contact to the list.
							addressBookFile = open("address book.txt", "w") #opening database to write on.
							listTofile(fileList,addressBookFile)			#overwriting list to the database.
							sortFile()										#sorting file by sortFile() subprogram.
							command = False									#changing command to False to get out of editing selected contact.
							editStr = "CANCEL"								#changing editStr to 'cancel' to get out of edit process.
						elif selectedField.upper() == "CANCEL":
							command = False
				else:
					print ""
					print "Not valid selection!"
					print "You must select integer between 1 and", len(editSearchList)
					print ""
			else:
				editStr = "CANCEL"
				print ""
				print "Edit process has been aborted."
				print ""
		else:
			editStr = "CANCEL"
			print "The input contact could not find!"

#==================================================( Main )=====================================================================================================================
command = ""
while command != "Q":
	print "a) Add new contact"
	print "d) Delete contact"
	print "e) Edit"
	print "sh) Show all the contact"
	print "s) Search"
	print "q) Quit"
	print ""
	command = raw_input("Please enter your command: ")		# command  asks user to input what he wants to do (Add a new contact, delete a contact, Edit, Search , showa all contacts or exit from program)
	print ""
	command = command.upper()								#changing command string to upper case
	#Following if/else block checks user input and start corresponding codes to user's order.
	if command == "A":										# if user selected add new contact
		add()
	elif command == "S":									#if user selected search new contact
		searchStr = raw_input("Please enter a name or telephone number: ")	# getting user a string to search
		if search(searchStr) != []:
			showList(search(searchStr))
		else:
			print "The input contact could not find!"
	elif command == "D":									#if use selected delete contact.
		delete()
		
	elif command == "E":									#if use selected edit contact.
		edit()
		
	elif command == "SH":									#if user selected show all the contact
		addressBookFile = open("address book.txt","r")
		List = addressBookFile.readlines()
		addressBookFile.close()
		sliceList(List)
		showList(List)
	
	
