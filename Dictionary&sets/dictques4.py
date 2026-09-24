#what will happen when two names are same in previous question ?
 


d ={}
name = input( "enter friends name:")
lang = input( "enter faourite language :")
d.update({name : lang})

name = input( "enter friends name:")
lang = input( "enter faourite language :")
d.update({name : lang})

name = input( "enter friends name:")
lang = input("enter faourite language :")
d.update({name : lang})

name = input( "enter friends name:")
lang = input( "enter faourite language :")
d.update({name : lang})

print(d)

#it will show PS D:\internship\pyhton\Dictionary&sets> python dictques4.py
# enter friends name:shubham
# enter faourite language :python
# enter friends name:harry
# enter faourite language :python
# enter friends name:rohan 
# enter faourite language :C
# enter friends name:rohan 
# enter faourite language :Js
# {'shubham': 'python', 'harry': 'python', 'rohan ': 'Js'}


#bcz d.upadate will show the last entered input show it shows the last one
