Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> opening = 100
... incoming = 50
... dispatched = 80
... closing = 65
... 
... expected = opening + incoming - dispatched
... 
... print("Expected stock:", expected)
... print("Actual stock:", closing)
... 
... if expected == closing:
...     print("Stock is correct")
... else:
...     print("Stock discrepancy:", expected - closing)
... 
... if closing < 50:
