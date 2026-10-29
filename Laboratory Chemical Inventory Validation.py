Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> chemicals = {
...     "Acid": 20,
...     "Base": 15,
...     "Water": 30
... }
... 
... maximum = 25
... 
... for name, quantity in chemicals.items():
...     if quantity > maximum:
...         print(name, "Quantity exceeds limit")
...     else:
