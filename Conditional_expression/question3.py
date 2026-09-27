# #a spam comment is defiend as a text containing following keywords:-
# "make s lot of money" , "buy now" , "subscribe this " , "click this " ,  "write a program to detect these spams "
#wap to detect these spams.

spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"
spam5 = "write a program to detect these spams"

message  = input ( "enter any paragraph :- ")

if ((spam1 in message) or (spam2 in message ) or ( spam3 in message ) or ( spam4 in message )): 
  print( " this comment is a spam ")

else :
  print ( "this comment is not a spam")


# #OUTPUT:-
# enter any paragraph :- buy the car 
# this comment is not a spam

# enter any paragraph :- buy now  this car 
#  this comment is a spam 

# enter any paragraph :- buy this car now 
# this comment is not a spam

