import re
txt="The rain in spain"
x=re.search("^The.*Spain$", txt)
if x:
    print("YES! We have a match!")
else:
    print("No match")