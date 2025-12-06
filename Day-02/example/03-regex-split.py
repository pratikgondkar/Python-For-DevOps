import re 

text = "apple,banana,orange,grape,mango"
pattern = r","

result = re.split(pattern, text)
print("Split Result:", result)