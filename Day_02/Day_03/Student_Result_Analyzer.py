m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))

total = m1 + m2 + m3

percentage = (total/300) * 100

if (percentage >= 90):
    print("A")
elif (percentage >= 75):
    print("B")
elif (percentage >= 60):
    print("C")
elif (percentage >= 40):
    print("D")
else:
    print("Fail")