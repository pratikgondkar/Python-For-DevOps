for i in range(5):
    print("Rana :", i)

furits = ["apple", "banana", "mango", "grapes"]
for fruit in furits:
    print("I like", fruit)


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print("Number:", num)


for num in numbers:
    if num == 3:
        continue
    print("Number:", num)   

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)

