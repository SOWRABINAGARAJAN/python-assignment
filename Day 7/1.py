#Swapping of keys and values in dictionary
port1 = {21:"FTP", 22:"SSH", 23:"telnet",80:"http"}
port2= {val:key for (key, val) in port1.items()}
print(port2) 