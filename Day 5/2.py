#Merge two sorted lists & produce one sorted list(use only one loop)

list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45,60]
for x in list2 : 
    list1.append(x)  
print(sorted(list1))