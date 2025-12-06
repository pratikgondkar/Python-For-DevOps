import re
text = "i am learning python programming"
pattern = r"python"

search = re.search(pattern, text)

if search:
    print("serach are found:", search.group())
else:
    print("No search found")