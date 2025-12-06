import re 

text = "i am learning python programming"
pattern = r"i"

match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")