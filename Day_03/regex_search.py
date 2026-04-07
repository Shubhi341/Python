import re 

text="the quich brown fox"
pattern=r"brown"

search= re.search(pattern,text)
if search:
    print("pattern found: ", search.group())
else:
    print("pattern not found")
