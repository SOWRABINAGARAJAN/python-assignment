#python program to find all occurence of substring in a given string

string = "what we think we become;we are Python programmer."
for index,value in enumerate(string):
    if string[index:index+(len("we"))] == "we":
        print(index);