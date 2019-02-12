home = 20
counter = 0
go_home = 0
print("You Are Currently {} km away from home".format(home))



while counter < 20:
	
	print("Would you like to run or walk?")
	exercise = input()
	
	if exercise == "run":
		counter += 5
		print("Distance from home is {} km".format(counter))
		
			
	

	elif exercise == "walk":
		counter += 1
		print("Distance from home is {} km".format(counter))
		

	else:
	 	print("Goodbye")
	 	break


if counter >= 20:
	print("You Made It HOME!!!")
	


#6

if counter >= 20:
	print("Ready To Stop exercising? Enter 'Go Home' To Stop exercising!")
	go_home = input()
    


if go_home == "go home":
	print("Welcome Home")

else:print("Do Some Strecthes Before Continuing!") 


	

		







