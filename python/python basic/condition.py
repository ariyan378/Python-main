# # A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

p1 = "Make a lot of many"
p2 = "buy Now "
p3 = "subscribe now"
p4 = "click this"

text = input("Enter Your comment : ")


if((p1 in text) or (p2 in text) or (p3 in text) or (p4 in text)) :
    print("This is a spam ")
else : 
    print("you are safe")

print("Process complete")

