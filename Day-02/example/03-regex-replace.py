import re 

text = "Rana is learning python programming"
pattern = r"Rana"

replacment = "Ranaji"

new_text = re.sub(pattern, replacment, text)

print("Original Text:", text)
print("Modified Text:", new_text)