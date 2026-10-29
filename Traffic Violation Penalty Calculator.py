Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> fine = 0
... 
... for i in range(2):
...     offence = input("Enter offence (helmet/signal): ")
...     repeat = input("Repeat offence? (yes/no): ")
... 
...     if offence == "helmet":
...         fine += 500
...     elif offence == "signal":
...         fine += 1000
...     else:
...         print("Invalid offence")
...         continue
... 
...     if repeat == "yes":
...         fine += 500
... 
... print("Total fine:", fine)
... 
... if fine >= 2000:
