kilometres = float(input("Enter the KMS you run: "))
minutes = int(input("Enter the minutes you run: "))
seconds = int(input("Enter the seconds you run: "))

time = minutes * 60 + seconds
kms_run = kilometres / time * 3600
miles = kms_run / 1.609


print("the speed (in miles per hour): ", miles)