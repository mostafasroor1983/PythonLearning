# Define sets
set1 = {1, 2, 3, 4, 5, 6, 5}  # duplictes removed
set2 = set(["a", "b", "c", "d"])  # ordered
print(set1)
print(set2)
# print(set2[1]) # not indexed
print("#"*50)

# Sets are mutable
set1.add(11)
print(set1)
print("#"*50)

# Deduplicating ietms in a list
duplicated_elements_list = ["c", "v", "e", "v", "a", "A", "b", "c"]
deduplicated_set = set(duplicated_elements_list)
print(deduplicated_set)
print("#"*50)

#Removing an element
deduplicated_set.remove("c")
print(deduplicated_set)
print("#"*50)