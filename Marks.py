x= int(input("Enter the number:"))
result=""

if x<30:
    result = "Fail"
elif x<75:
    result = "Passed with Distinction"
else:
   result = "Pass"

print(result)