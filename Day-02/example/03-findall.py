import re

text = "Rana is learing Python"

pattern = r"Python"

search = re.search(pattern, text)
if search:
    print("pattern is found:", search.group())
else:
    print("pattern is not found")


