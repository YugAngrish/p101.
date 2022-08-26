
import random 


def dice(response):
  
    if(response == 'y'):
      no = random.randint(1,6)
      print(no)
   
   
    elif(response == 'n'):
        print("Project ended")
    
       
response = input("choose y or n") 
while(response=='y'):
  dice(response); 
  print(response)
  print("Press y to continue and n to exit")
  response=input("choose your new input")