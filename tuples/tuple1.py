#Tuple is an ordered collection that can't be changing after creating it.
#Locked & Frozen for security reason\

#Tuple is Ordered and allow duplications
my_tuple = (30, 60, 20, 0, 30)
print(my_tuple) #Keep the same order as we created it and allow duplicates

#Indexed
print(my_tuple[0]) # Fisrt element 


#Imutable not able to do any kind of change
#my_tuple[0] = 90 # TypeError: 'tuple' object does not support item assignment
#del my_tuple[1]  # TypeError: 'tuple' object doesn't support item deletion
print(sorted(my_tuple)) # Sort the tuple and convert it to List

