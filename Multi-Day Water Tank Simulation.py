Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> level = 50
... capacity = 100
... 
... for day in range(1, 4):
...     inflow = int(input("Enter water inflow: "))
...     outflow = int(input("Enter water outflow: "))
... 
...     level = level + inflow - outflow
... 
...     if level > capacity:
...         level = capacity
...         print("Overflow on day", day)
... 
...     if level < 0:
...         level = 0
...         print("Water shortage on day", day)
... 
...     print("Day", day, "Water level:", level)
... 
...     if level >= 80:
...         print("Threshold reached on day", day)
