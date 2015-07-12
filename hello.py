print("Helllllllloooooo World!") #Print greeting
print("What is your name?") #Provide a prompt for the user to provide input
my_name = input() #Create a variable that allows for input
print("Nice to meet you, " + str.capitalize(my_name)) #You are concatenating the string and capitalizing the input from my_name
print('Your name has ' + str(len(my_name)) + ' letters in it.') #Concatenate the string and integer which is the length of your name.
#In order to do that you must convert the integer which is the length of your name which you call with len() to a string with str()
#You have nested the methods
if len(my_name) > 5:
	print("Does your name ever feel heavy?")
else:
	print("Your name is so light it could float away.")
	#Use an if else statement to analyze the length of the name that was entered.
