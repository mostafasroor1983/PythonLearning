my_list = [1, 2, 4, 6, 3, 2] #Python maintain the same order as we declared.
print(my_list)               #Python allow the duplications

#List elements are indexed
print(my_list[0])  # First index
print(my_list[1])  # Second index

#List is Mutable: elements can be updated, removed, changed, sorted...
del my_list[2]
my_list.insert(0,-1)
print(sorted(my_list))