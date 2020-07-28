#Making elements of inner list and tuples to outer list 

my_list = [(1, 2,3),[1,2],['a','hit','less']] 

output_list = [] 
  
# function used for removing nested lists in python

def removeNesting(my_list): 
    for i in my_list: 
        if type(i) == list: 
            removeNesting(i) 
        else: 
            output_list.append(i) 
            
print ('Original list: ', my_list) 
removeNesting(my_list) 
print ('Outer list: ', output_list) 