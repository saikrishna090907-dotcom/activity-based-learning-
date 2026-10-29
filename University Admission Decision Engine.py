Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> students = [
...     ("Ravi", 85),
...     ("Sita", 92),
...     ("Ram", 70),
...     ("Anu", 88)
... ]
... 
... eligible = []
... 
... for name, marks in students:
...     if marks >= 75:
...         eligible.append((name, marks))
... 
... eligible.sort(key=lambda x: x[1], reverse=True)
... 
... print("Eligible students:")
... for name, marks in eligible:
