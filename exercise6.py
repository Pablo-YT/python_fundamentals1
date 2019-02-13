home = 25
counter = 0
go_home = 0
energy = 100
rest = 0
print("You Are Currently {} km away from home".format(home))


while counter < home and energy > 0:
	
	print("Would you like to run or walk?")
	exercise = input()
	
	if exercise == "run":
		counter += 5
		print("Distance from home is {} km".format(counter))
		energy -= 25
		if energy < 0:
			energy = 0
		print("Energy Levels At {}%".format(energy))



	elif exercise == "walk":
		counter += 1
		print("Distance from home is {} km".format(counter))
		energy += 10
		if energy < 0:
			energy = 0
		print("Energy Levels At {}%".format(energy))


	else:
	 	print("Goodbye")
	 	break

	if int(energy) == 0:
		print("You Are Tired And Can No Longer Continue!")
		print("You Need To Rest!!")
		print("Enter 'rest' in order to restore energy levels")
		rest = input()

	if rest == 'rest':
		print("You're energy levels are back")
		break
	
	#else: print("Energy levels are too low cannot move forward. May I suggest a Gaterade")



if counter >= home:
	print("You Made It HOME!!!")
	


#6

if counter >= 25:
	print("Ready To Stop exercising? Enter 'Go Home' To Stop exercising!")
	go_home = input()
    


if go_home == "go home":
	print("Welcome Home")

else:print("Do Some Strecthes Before Continuing!") 


	

		