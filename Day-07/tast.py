import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, i will create a t2.micro instance and they charage 2 dollars.")

elif type == "t2.small":
    print("ok, i will create a t2.small instance and they charage 4 dollars.")
elif type == "t2.medium":
    print("ok, i will create a t2.medium instance and they charage 8 dollars.")
else:
    print("we do not have this type of instance.")
