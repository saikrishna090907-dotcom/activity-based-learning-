Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> budget = 500
... total = 0
... 
... prices = [200, 150, 100]
... quantities = [2, 1, 2]
... 
... for i in range(3):
...     total += prices[i] * quantities[i]
... 
... print("Total cost:", total)
... 
... if total > budget:
...     print("Budget exceeded:", total - budget)
...     print("Reduce the quantity of products")
... else:
