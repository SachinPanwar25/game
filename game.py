import random

a=random.randint(1,10)
i=1
while i<=5:
   user_value =int(input("Enter the value :"))
   if a==user_value:
         print(f"You won the game \nYou taken {i} chances")
        
         break

   elif user_value< a:
       print ("please enter the greater value" )
   elif user_value> a:
       print ("please enter the smaller value" )

   i=i+1
if i>5:
    print ("game over")
