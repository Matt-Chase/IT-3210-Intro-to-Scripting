inventory = []

def add_inventory(new_item):
	# adds an item to the "inventory" list
	inventory.append(new_item)
	
def remove_inventory(del_item):
	# deletes an item from the "inventory" list
	inventory.remove(del_item)
	
def show_inventory():
	# prints the inventory if there is something in it
	if len(inventory) != 0:
		print "You have the following items in your inventory:"
		for item in inventory:
			print item
	else:
		print "You don't have anything in your inventory"

def credits():
	print """
	
	Written by Matt Chase
	Directed by Matt Chase
	
	Narrator            Matt Damon
	
	Adventurer          You
	
	Frankie the Lion    Himself
	
	Genie               Robin William's ghost (too soon?)
	
	Stranded Guy        Gary Oldman
	
	Cyclopic Unicorned
	Airborne Violet     Ice Cube
	Human Hunter
	
	Blind Old Man       Morgan Freeman
	
	"""
	
def reviews():
	print """
	
	"Playable, 10/10" - IGN
	
	"Cool" - my little brother
	
	"Two thumbs up" - probably what Roger Ebert would have said
	
	"Oh that's nice" - my mom
	
	"Totally worth an A" - like, everyone I know
	
	"""
	
# options after you beat the game
def endgame():
	print "1. Credits"
	print "2. Reviews"
	print "3. Exit"
	
	# user input
	last_thing = raw_input("> ")
	
	if last_thing == "1":
		credits()
		endgame()
	elif last_thing == "2":
		reviews()
		endgame()
	elif last_thing == "3":
		exit(0)
	else:
		print "Come on, man we got so far"
		print "Try again"
		endgame()

# last room function		
def finale():
	print "\nWhat do you do?"
	print "1. Sit down."
	print "2. Stay standing."
	print "3. Charge the old man."
	
	# user input
	final_choice = raw_input("> ")
	
	if final_choice == "1":
		print "\nVery carefully you make your way over and sit in the chair."
		print "\"Good, good\" the old man cackles."
		print "\"Here, have a drink,\" he says and slides over a bottle of tequila."
		print "You silently pour a bit into two glasses, not drinking until he does."
		print "\"I'm sure you're wondering what you're doing here?\" the old man playfully asks."
		print "\"It's crossed my mind, yes,\" you casually reply."
		print "\"First, I have but one question.\""
		print "\"Oh yeah, what's that?\""
		print "\"Does this rag smell like chloroform to you?"
		print "A big henchman comes out of nowhere and shoves a rag into your face."
		print "You try not to inhale the fumes, but eventually you succumb and pass out.\n\n\n"
		
		start()
	elif final_choice == "2":
		print "\n\"I think I'll stand\" you say to the old man."
		print "Look at you being all brave in the face of your captor."
		print "\"Have it your way.\" he says, in a rather disappointed tone."
		print "\"I was going to do this whole monologue where I explain my master plan"
		print "but I guess you're too tough for that.\""
		print "\"Well, I suppose I could sit down for a bit,\" you say."
		print "\"No, the moment passed. Goodbye.\""
		print "The man throws a bottle at your head and you bleed out."
		print "What a way to go..."
		
		dead()
		
	elif final_choice == "3":
		print "You muster up all the strength you have in you."
		print "\"I won't do what you tell me!\" you scream and jump over the table, tackling the old man!"
		
		for item in inventory:
			if item == "Horn":
				print "You pull out the horn that you were given"
				print "by the Cyclopic Unicorned Airborne Violet Human Hunter"
				print "Time to start stabbing!"
				
				# makes sure you input an integer
				try:
					# user input
					stab = int(raw_input("How many times will you stab the old man? "))
				except ValueError:
					print "You frantically search for a number key, any number will do"
					print "But in your haste you press something else! Quickly try again!"
					
				print "You stab the old man %d times!" % stab
				
				# extra fun with conditionals
				if stab > 5:
					print "Damn son, that's excessive!"
	
				print "You've killed the old man. You are no closer to figuring out why"
				print "you were brought here, but hey, at least you got your revenge."
			
				you_win()
			elif item == "Knife":
				print "\nYou pull out the knife you found."
				print "Time to start stabbing!"
				
				# makes sure you input an integer
				try:
					# user input
					stab = int(raw_input("How many times will you stab the old man? "))
				except ValueError:
					print "You frantically search for a number key, any number will do"
					print "But in your haste you press something else! Quickly try again!"
					
				print "You stab the old man %d times!" % stab
				
				# extra fun with conditionals
				if stab > 5:
					print "Damn son, that's excessive!"
	
				print "You've killed the old man. You are no closer to figuring out why"
				print "you were brought here, but hey, at least you got your revenge."
				
				you_win()
			else:
				print "\nYou punch the old man in the face."
				print "\"Oh please, you're no match for me!\" he exclaims."
				print "The blind old man then pushes you off him and does some sick karate moves."
				print "You are so in awe of his unexpected skills that you have"
				print "no time to react when he karate chops you in the neck, taking"
				print "your head clean off. Ouch."
				
				dead()
	else:
		print "\n\"Seriously, you've gotten this far and you still don't know how to"
		print "type in the right thing\" the old man taunts."
		print "\"Hey that's my job!\" I say."
		print "\"Oh shut up and narrate,\" he replies."
		print "Even though he's being a jerk about it. The old timer makes a good point."
		print "Try again."
		
		finale()

# intro function to the last room		
def blind_guy():
	print "\nYou find yourself walking down a long corridor."
	print "Eventually you see that another hall meets up with this one."
	print "\"Huh,\" you think to yourself, \"This game must have some great replay value.\""
	print "So meta!"
	print "\nFinally, you reach the end."
	print "In front of you is a huge wooden door."
	print "You knock."
	print "The door slowly creeks open."
	print "\nThe suspense is killing me!\n"
	print "Slowly, you walk inside to a pitch black room."
	print "\"H-Hello?\" you manage to choke out."
	print "\"Hello there,\" a voice echoes."
	print "\"Are you the blind man I was told about?\""
	print "\"Why yes, yes I am. Why don't you have a seat.\""
	print "\"Where? I can't see a thing in here it's so dark.\""
	print "\"Oh did the servants turn off the lights again? They're always doing that."
	print "'What if I have guests' I say, but they never listen."
	print "Sorry about that. Here.\""
	print "And with a flick of a switch you are met with a blinding light."
	print "When you regain your vision, you see an old man sitting at a table with an empty chair just for you..."
	
	finale()

# intro to path 1 room 2
def cuavhh_intro():
	print "\nYou enter yet another room."
	print "Floating in front of you is an abomination of a monster."
	print "\"What are you? Some kind of... Cyclopic Unicorned Airborne Violet Human Hunter??\" you cry out."
	print "\"You're not gonna eat me are you?\""
	print "\"Maybe,\" the monster replied, \"You don't look so tough.\""
	
	cuavhh()

# path 1 room 2 function
def cuavhh():
	print "\nWhat do you do?"
	print "1. Try to talk him out of it."
	print "2. Inquire about his past."
	print "3. Open inventory."
	print "4. Use item."
	
	# user input
	monster_choice = raw_input("> ")
	
	if monster_choice == "1":
		print "\n\"Hey man, don't eat me please,\" you say nervously."
		print "\"Why not? After all I am a purple people ea- I mean violet human hunter.\" The monster replies."
		print "\"Well, I could help you out if you ever get sued for copyright infringement.\""
		print "\"Nah, after I gave up on my dream of becoming a rock star I got a law degree"
		print "online so I'm pretty much set."
		print "Yeah I think I'm just gonna eat you. Nothing personal, brah.\""
		print "The Cyclopic Unicorned Airborne Violet Human Hunter swoops down and devours you whole."
		
		dead()
	elif monster_choice == "2":
		print "\n\"So what's your story Mr. Human Hunter?\" you ask politely."
		print "\"Well you know, just your classic alien-wants-to-be-in-a-band-then-gets-imprisoned-for-life"
		print "story. Nothing special.\""
		print "\"Tragic, man. Tragic,\" you say, \"Do you know who imprisoned you?\""
		print "\"Some blind dude. Never got his name. I think he lives in the next room over."
		print "\"Huh. Mind if I go talk to him?\""
		print "\"Well since you actually asked nicely, sure thing.\""
		print "\"Thanks, bud. Hope that band thing works out eventually.\""
		print "\"That means a lot, friend. Here have this. Maybe it will help you.\""
		print "The monster hands you one of his old horns."
		print "It's kind of gross, but you put it in your pocket anyway and go on your way."
		
		add_inventory("Horn")
		
		blind_guy()
	elif monster_choice == "3":
		show_inventory()
		cuavhh()
	elif monster_choice == "4":
		# user input
		item = raw_input("What item will you use (\"exit\" to stop)? ")
		
		# item.lower allows the user to use upper or lower case
		if item.lower() == "broken spear":
				print "\nYou take out the spear you used to kill the lion."
				print "\"Oh so you think you can take me?\" Yells the monster."
				print "He dives at you. You try to use your spear but, you know, it's broken."
				print "The Cyclopic Unicorned Airborne Violet Human Hunter swoops down and devours you whole."
			
				dead()
		elif item.lower() == "guitar":
				print "\nYou whip out your new guitar and start shredding."
				print "The monster looks on in amazement."
				print "\"Damn, son where'd you get a such a nice guitar?\" he asks."
				print "\"Genie gave it to me.\" you reply."
				print "\"You know I've always wanted to be in a rock n roll band,\" the monster says eagerly."
				print "\"Tell you what, if you give me that guitar, I wont eat you.\""
				print "\"Maaaan I just got this thing,\" you complain."
				print "\"That's the deal, take it or leave it,\" he says."
				print "\"Fine. Here.\" Defeated, but alive you move on to the next room barely escaping"
				print "the evil clutches of borderline copyright infringement."
			
				remove_inventory("Guitar")
			
				blind_guy()
		else:
			print "You don't have that."
			cuavhh()
			
		
# intro to path 2 room 1	
def stranded_guy_intro():
	print "\nOh good, you're in another room..."
	print "\"Who's there?\" a panicked voice asks."
	print "\"I'm just trying to figure out why I'm here,\" you respond."
	print "\"Well I'm not sure myself, I found a blind guy in here once"
	print "he was over that way.\" The stranger points to the door"
	print "He said that there might be a way out near here, but I never found it."
	
	stumble_init = 0
	stranded_guy(stumble_init)

# path 2 room 1 function	
# uses the stumble variable to increment movement in this room
def stranded_guy(stumble):
	print "\nWhat do you do?"
	print "1. Go through the door"
	print "2. Stumble around in the dark"
	print "3. Keep talking"
	print "4. Open inventory"
	
	# user input
	stranded_choice = raw_input("> ")
	
	if stranded_choice == "1":
		print "\n\"Well, I guess I'll go looking for that blind guy.\" You say."
		print "\"Good luck,\" says the stranger. \"Don't die and stuff.\""
		print "You go through the door in search of a blind man."
		
		blind_guy()
	elif stranded_choice == "2":
		print "%d" % stumble
		if stumble < 2:
			print "\nYou look around in the darkness, but find nothing yet."
			
			stumble += 1
			
			stranded_guy(stumble)
		elif stumble == 2:
			print "\nHey you actually found something!"
			print "Looks like a knife. You put it in your pocket."
			
			stumble += 1
			
			# puts "Knife" item into the inventory list
			add_inventory("Knife")
			stranded_guy(stumble)
		else:
			print "\nAfter quite a bit of searching, you hear a hollow thud under your foot."
			print "You grope around and find a handle. It's a trap door!"
			print "You open it to reveal a tunnel."
			print "\"Hey, I've never come across that before,\" exclaims the stranger."
			print "\"Maybe this is the way out,\" you suggest."
			print "\"Well let's find out\""
			print "You and the stranger crawl through the narrow tunnel."
			print "What's that? a light at the end!"
			print "You go to it and lo and behold it's the way out!"
			print "A voice echoes in the distance: \"That's not how you're supposed to beat the game!\""
			print "\"Stupid hackers!\""
			
			you_win()
	elif stranded_choice == "3":
		print "\n\"So how long have you been here?\" You ask the man."
		print "\"Look dude, I'm tired. I don't want to talk to you any more,\" he replies."
		print "\"Seriously?\""
		print "\"Seriously.\""
		print "\"Well that just sounds like lazy programming to me.\""
		print "\"Yeah, you're probably right,\" The stranger says and gives a knowing glance to the camera."
		print "\"Dude you can't just break the fourth wall like that,\" you say, shocked."
		print "\"Can't help it, man. That's just what I was hardcoded to do."
		print "Now go back to the selection menu.\""
		
		stranded_guy(stumble)
	elif stranded_choice == "4":
		show_inventory()
		stranded_guy(stumble)
	else:
		print "\nHow many times to we have to do this, pal? Pick a real option."
		
		stranded_guy(stumble)

# path 1 room 1 intro
def genie_intro():
	print "\nYou walk through the left door and find yourself in a small room."
	print "You look around and find a lamp."

	genie()
	
# path 1 room 1 function
def genie():
	print "\nWhat do you do?"
	print "1. Rub the lamp"
	print "2. Curl up in a ball"
	print "Type a number"
	
	# user input
	genie_choice = raw_input("> ")
	
	if genie_choice == "1":
		print "\nYou pick up the lamp and start to rub it."
		print "\"This better not turn in to some kind of 60s sitcom,\" you think to yourself"
		print "A genie pops out of the lamp."
		print "\"You have freed me kind stranger, and for that I will grant you a wish,\" he exclaimed."
		print "\"Only one? What a rip off!\" You say"
		print "\"Yeah people really took advantage of the whole three wishes thing.\""
		print "\"NOW CHOOSE\" the genie bellowed"
		print "1. I wish to know why I'm here."
		print "2. I wish for a million dollars."
		print "3. I wish to be set free."
		print "4. I wish for a guitar."
		print "5. I wish for infinite wishes."
		print "Type a number"
		
		# user input
		wish = raw_input("> ")
		
		if wish == "1":
			print "\n\"Ah it's answers you seek. I will take you to someone who can help.\""
			print "You are teleported to another small room."
			
			stranded_guy_intro()
		elif wish == "2":
			print "\n\"Greedy are we? As you wish.\""
			print "A million dollar bills start to fall out of the ceiling."
			print "But the room is too small and soon the bills start to crush you."
			print "You have died from your own wealth! Oh the irony!"
			
			dead()
		elif wish == "3":
			print "\n\"So you want to cheat the game do you?"
			print "That will be $25\""
			print "\"What!? I don't have any money!\" You yell."
			print "\"Welcome to the modern gaming industry, bud. You gotta pay to win.\""
			print "The genie goes back into his lamp to make a phone call to EA about how"
			print "to better implement microtransacions into his wishes."
			print "You wait for him to come back out."
			print "Days go by."
			print "You die of dysentery and never make it to Oregon."
		elif wish == "4":
			print "\n\"Seriously? A guitar? Seems a bit strange given the situation,\" the genie says, perplexed."
			print "\"Eh, I've always wanted one. Figured I'd never get a chance like this again,\" you say."
			print "\"Well ok, here you go\""
			print "And with a poof, the genie was gone and in his place a bitchin' Gibson Les Paul."
			print "\"Sweet\" you say, and put it in your pocket."
			print "That's right. Your pocket."
			
			add_inventory("Guitar")
			
			print "\nHey look, a door. You go through it."
			
			cuavhh_intro()
		elif wish == "5":
			print "\n\"Infinite wishes!? A paradox!?\" the genie lets out a tortured scream."
			print "\"My only weakness! Noooooo!!\""
			print "The genie disappears into a cloud of illogic."
			print "A door appears behind him and you go through it."
			
			cuavhh_intro()
		else:
			print "\n\"That wasn't an option given to you,\" said the genie."
			print "\"For not playing by the rules I must now kill you."
			print "It's part of the genie code of conduct, sorry.\""
			
			dead()
	elif genie_choice == "2":
		print "\nThe sheer thought of making a decision terrifies you."
		print "You curl up in a ball and cry like a little baby."
		print "Seriously, what is wrong with you.\n"
		
		dead()

# room 1 intro		
def lion_pit_intro():
	print "\nYou hear a low pitched growl."
	print "You see a golden mane slowly stalk its way toward you."
	print "Is that... Yup that's totally a lion."
	
	lion_pit()

# room 1 function	
def lion_pit():
	print "\nBetter act fast, he looks ready to pounce."
	print "1. Stand still in fear."
	print "2. Frantically search for a weapon."
	print "3. Pee your pants."
	print "4. Open inventory."
	print "Type a number"
	
	# user input
	lion_choice = raw_input("> ")
	
	if lion_choice == "1":
		print "\nYou are terrified. You don't dare move a muscle."
		print "The lion comes up to you and sniffs around for a while."
		print "He rolls over playfully."
		print "1. Pet the cute little kitty."
		print "2. Run for your life."
		print "Type a number"
		
		# user input
		lion_one = raw_input("> ")
		
		if lion_one == "1":
			print "\nYou rub his tummy and he starts to purr."
			print "Oh no he was just toying with you!"
			print "He bites your face of! Oh the agony!\n"
			
			dead()
		elif lion_one == "2":
			print "\nYou take this chance to run away."
			print "Somehow you escape into a dark corner."
			print "You haven't fooled him for long though."
			
			lion_pit()
		else:
			print "\nOk you little rebel, pick an actual choice."
			
			lion_pit()
	elif lion_choice == "2":
		print "\nYou look around for anything to kill the beast."
		print "You see a spear lying on the ground."
		print "You make a run for it, but the lion is right on your tail."
		print "You pick it up and stab him through his mouth just in time!"
		print "Way to go, champ!"
		add_inventory("Broken_Spear")
	elif lion_choice == "3":
		print "\nYou are so scared your bladder releases like a rushing river!"
		print "That's pretty gross dude."
		print "The lion wants nothing to do with you now and walks away."
		print "Good thinking!"
	elif lion_choice == "4":
		show_inventory()
		lion_pit()
	else:
		print "\nCome on, play the game"
		
	print "\nWith the lion dead, you now notice two doors."
	print "Better pick one."
	print "1. Left"
	print "2. Right"
	print "Type a number"
	
	# user input
	lion_door = raw_input("> ")
	
	if lion_door == "1":
		genie_intro()
	elif lion_door == "2":
		stranded_guy_intro()
	else:
		print "\nYou die of indecisiveness"
		dead()

# first decisions
def wake_up():
	print "\nYou can vaguely make out two doors."
	print "Which one do you open?"
	print "1. Left"
	print "2. Right"
	print "Type a number"

	# user input
	first_door = raw_input("> ")

	if first_door == "1" or first_door == "2":
		print "\nYou try to turn the handle, but it's locked!"
		print "A voice echoes out \"Ha! Like I'd give you a choice!\""
		print "The floor falls out from under you and you fall into a pit."
		
		lion_pit_intro()
	else:
		print "\nTry again. 1 or 2, it's not that hard."
		
		wake_up()

# game intro
def start():		
	print "\nOh no, it happened again."
	print "You find yourself alone in a dark room."
	print "\"I've got to stop drinking tequila\" You think to yourself."
	print "You have so many questions."
	print "Where am I?"
	print "How did I get here?"
	print "Did that guy's rag smell like chloroform or not?"
	
	wake_up()

# exits the game if you make the wrong choices
def dead():
	print "GAME OVER"
	exit(0)

# congratulatory banner for making the right choices	
def you_win():
	print "\n\n***************************"
	print "*                         *"
	print "* Congratulations You Win!*"
	print "*                         *"
	print "***************************\n\n"
	
	endgame()

start()