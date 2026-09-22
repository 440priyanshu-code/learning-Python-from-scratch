"""
   what will be the length of the following set. 
   s=set()
   s.add(20)
   s.add(20.0)
   s.add('20')
"""
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print (s)
print(len(s))

#OUTPUT WILL BE 3 NOT 2 bcz in python the comparision operator ( ==) jsut checks they are numerically equal or not and if they are it says true simillary it happend here in sets.
