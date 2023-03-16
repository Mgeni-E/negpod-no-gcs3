

month =input("Enter the month: ")
if month in ["January", "March", "May", "July", "August", "October", "December"]:
    print("Month has 31 days")
elif month in ["April", "June", "September", "November"]:
    print("Month has 30 days")
elif month == "February":
    print("month has 28 or 29 days")
else:
    print("Month input us invalid")
    



