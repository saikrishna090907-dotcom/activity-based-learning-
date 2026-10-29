Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> subjects = ["Maths", "Python", "English"]
... 
... for subject in subjects:
...     first = int(input("Enter first exam marks: "))
...     second = int(input("Enter second exam marks: "))
... 
...     change = second - first
... 
...     if change > 0:
...         print(subject, "Improved by", change)
...     elif change < 0:
...         print(subject, "Declined by", -change)
...     else:
...         print(subject, "No change")
... 
...     if second < 40:
