Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> hours = int(input("Enter parking hours: "))
... vehicle = input("Enter vehicle (car/bike): ")
... 
... if hours <= 0:
...     print("Invalid time")
... elif vehicle == "car":
...     fee = hours * 30
...     if fee > 200:
...         fee = 200
...     print("Parking fee:", fee)
... elif vehicle == "bike":
...     fee = hours * 10
...     if fee > 100:
...         fee = 100
...     print("Parking fee:", fee)
... else:
