print ("Every Horror Movie Ever")
start = '''
        Chapter 1- The Invitation
        It's a typical Friday night. Some of the popular people from school invited you to a party.
        The sun is quickly setting and you believe you are at the place where the party is supposed to be.
        "Huh?" you think to yourself. Before you lies a decrepit manor on a hill. It must have been a beautiful mansion years ago,
        but years of abandonment and neglect has warped it into the state it's in now...
        '''
print (start)

choice1 = '''
          Do you choose to walk away from the manor or approach the gate?
          Type "Walk away" to walk away or "Approach" to approach the gate.
          '''
print (choice1)
user_input = input()
# major choice 
if user_input == "Walk away":
    print ('''
            You think to yourself "Is this even the right place?
            You check the invitation...
            "OH NO!! I'm at the wrong address!! Should I check this house out just in case or go to the right address?"
            Type "Check house" to go to the house or "Leave" to go to the right address.
            ''')
    user_input = input()
    if user_input == "Check house":
           print ('''
                   You, being the curious little idiot you are, decide to go to the house despite knowing it's not the right place. *rolls eyes*
                   ''')
    if user_input == "Leave":
           print ('''
                    Congratulations! You avoided potential death! Now go and be social!
                    ''')
           print ('''
                   Thanks for playing!
                   ''') #This is an ending

#major choice
elif user_input == "Approach":
    print ('''
           You decide to approach the gate. Taking a good look at it, you realize that it has a lock on it.
           Do you try to unlock the gate or find another way in?
           Type "Unlock" to try to unlock the gate or "Find another way" to find another way in.
           ''')
    user_input = input()
#this is the unlock choices
    if user_input == "Unlock":
        print ('''
                Do you try to pick the lock or pull on the lock?
                Type "Pick" to pick the lock or "Pull" to pull on the lock.
                ''')
        user_input = input()
    #this is still the gate part
        if user_input == "Pick":
            print ('''
                   You got the lock open! You push the gate open and walk up to the front door.
                   You knock on the door, but nobody answers. Hold on, is that an open window?
                   "I got the gate open with my novice lockpicking skills, but that window looks a little promising," you think to yourself.
                   Type "Unlock door" to pick the door lock or "go through window" to enter the house through the window.
                   ''')
            
        elif user_input == "Pull":
            print ('''
                    Nope. Nothing happened.
                    You choose to either "Pick" the lock or "Find another way" in.
                    ''')
            user_input2 = input()
            if user_input2 == "Pick":
                print ('''
                   You got the lock open! You push the gate open and walk up to the front door.
                   You knock on the door, but nobody answers. Hold on, is that an open window?
                   "I got the gate open with my novice lockpicking skills, but that window looks a little promising," you think to yourself.
                   Type "Unlock door" to pick the door lock or "go through window" to enter the house through the window.
                   ''')
            elif user_input2 == "Find another way":
                print ('''
               You climb up the gate because why not? Who doesn't want to be a little fearless?
               You land on the other side of the gate and walk up to the front door of the house.
               You knock on the door, but nobody answers. Hold on, is that an open window?
               "I have a lockpick here in my bag, but that window seems a little promising," you think to yourself.
               Type "Unlock door" to pick the door lock or "Go through window" to enter the house through the window.
               ''')
                
##this is the other way in
    elif user_input == "Find another way":
        print ('''
               You climb up the gate because why not? Who doesn't want to be a little fearless?
               You land on the other side of the gate and walk up to the front door of the house.
               You knock on the door, but nobody answers. Hold on, is that an open window?
               "I have a bobbypin here in my bag that I can use as a lockpick, but that window seems a little promising," you think to yourself.
               Type "Unlock door" to pick the door lock or "Go through window" to enter the house through the window.
               ''')
        user_input = input()
        if user_input == "Unlock door":
            print ('''
                   You unlock the door despite not knowing much about picking locks. You walk through the door and enter the large foyer of the manor. You turn on your phone light.
                   Old paintings line the wall. You feel a chill go down your spine because you feel as if the people in the paintings are watching your every move.
                   Is there even anyone here?
                   Type "Hello" to ask if anyone is home or "Keep going" to continue walking through the foyer.
                   ''')
            user_input2 = input()
            if user_input2 == "Hello":
                print ('''
                       You call out "Hello! Is anyone home?" Silence...
                       Out of the corner of your eye, you see some shadow dart by. You turn, but it's gone.
                       You feel your body breaking out in a cold sweat. Your heart just beats faster and faster. Through your panic and fear, you think you start hearing
                       footsteps approaching. You're not alone in the manor...
                       Then you feel a hand clasp your shoulder.
                       END OF CHAPTER 1
                       ''')
        # 1 Ch 1 ending
            elif user_input2 == "Keep going":
                print ('''
                        You walk down the foyer. You can't help but admire the paintings. You start feeling uneasy. Each painting got weirder and weirder as you walked.
                        One painting in particular caught your eye...
                        Type "Woman" to look at the painting of the tall elegant pale woman or "Creature" to look at the painting of the strange creature with yellow eyes.
                        ''')
                user_input3 = input()
                if user_input3 == "Woman":
                    print ('''
                           This particular painting captures a tall woman wearing a white Victorian dress. The woman is as pale as her dress and her dark hair, put up in a bun,
                           makes her look even more pale. There seemed to be something off about the woman's blue eyes. They looked very realistic. You've never seen eyes so detailed
                           in a painting. Is that even possible. You step to the side just to make sure she's just a painted woman. Suddenly her blue eyes looked into your eyes. You
                           start feeling your heart speed up. You see quick glimpse of red in her eyes. You can't shake this feeling. You think you're just becoming paranoid.
                           Is this even real? The muse for this painting is probably dead already. It's not like she's going to come up behind you and tap you on the shoulder...
                           Right?...............................
                           Then you feel a cold hand cover your mouth.
                           END OF CHAPTER 1
                           ''')
      # 2 Ch 1 ending
                elif user_input3 == "Creature":
                    print ('''
                           This particular painting captures a seemingly large creature. It appears to be hidden in the shadow of some large building. The only thing visible are two yellow eyes
                           drawn with such detail that they appear to be glowing. The creature is also standing near what looks like a large picture window. There's a light coming from the inside of the building.
                           You can barely make out the shape of a person standing in the middle of the room that is shown in the painting. Your phone light flickers a little then turns back on.
                           You point the light at the painting again and... GASP! the creature's eyes have disappeared!! Your phone light flickers again and the window in the painting is now dark.
                           "What is going on?" you whisper to yourself and then your phone light goes completely dark. Your phone is now dead. You should've brought a portable charger.
                           You try to feel your way through the darkness but no matter how far to what seems to be the right, you don't even get to the wall. You try to walk a different direction, and again, no wall.
                           The little hairs on your neck stand up on end as you feel a hot breath on your neck. You freeze up. Your knees buckle up under you and you collapse to the floor...
                           For some odd reason, your phone light turns on despite your phone being dead a few minutes ago. You check your phone, but the battery says it's at 75%. You point your phone
                           in several different directions but there's nothing there....
                           Or is there?
                           END OF CHAPTER 1
                           ''')
    # 3 Ch 1 ending
        elif user_input == "Go through window":
            print ('''
                   You make your way to the open window, which is on the left side of the front on the house. You 
       


    
