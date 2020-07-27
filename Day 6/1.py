#Convert to a dictionary in one line code using list comprehension (without using zip method)

List1 = [1,2,3,4,5,6,7,8]

List2 = ["a","b","c","d","e"]

new_dict = { List1[i]:List2[i] for i in range(len(List2))}

print(new_dict)