string = "caesariseasy"

shift = 12
caeserd = ""

for i in string:
    if i != " ":
        caeserd += chr(ord(i) + shift)
    else:
        caeserd += " "


print(caeserd)
