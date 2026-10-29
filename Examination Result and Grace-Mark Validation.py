Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

# Examination Result and Grace Marks

subjects = ["Maths", "Physics", "Chemistry"]
max_marks = 100
pass_marks = 40
grace_limit = 5

marks = []
total = 0
grace_used = 0
all_passed = True

# Read marks
for subject in subjects:
    m = int(input("Enter marks in " + subject + ": "))

    if m < 0 or m > max_marks:
        print("Invalid marks!")
        exit()

    grace = 0

    # Apply grace marks if needed
    if m < pass_marks and pass_marks - m <= grace_limit:
...         grace = pass_marks - m
... 
...     final_marks = min(m + grace, max_marks)
...     grace_used += grace
... 
...     if final_marks < pass_marks:
...         print(subject, ": FAIL")
...         all_passed = False
...     else:
...         print(subject, ": PASS")
... 
...     print("Final marks:", final_marks)
... 
...     marks.append(final_marks)
...     total += final_marks
... 
...     # Stop if the total grace limit is exceeded
...     if grace_used > grace_limit:
...         print("Grace limit exceeded!")
...         exit()
... 
... # Calculate percentage
... percentage = total / (len(subjects) * max_marks) * 100
... 
... print("\nTotal marks:", total)
... print("Percentage:", round(percentage, 2), "%")
... print("Grace marks used:", grace_used)
... 
... # Final classification
... if not all_passed:
...     print("Result: FAIL")
... elif percentage >= 75:
...     print("Result: DISTINCTION")
... elif percentage >= 60:
...     print("Result: FIRST CLASS")
... elif percentage >= 50:
...     print("Result: SECOND CLASS")
... else:
...     print("Result: PASS")
