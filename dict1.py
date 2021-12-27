#Dictionary is unodered, doesn't allow duplicates but is changeable.
#info is stored in key:value form.
student={
    "roll no":677,
    "name":"Rustam"
}
print(student)

#Values are individually accessible.
print(student["roll no"])
print(student.get("roll no")) #Alternate method to access.

print(student.keys())
print(student.values())

#Changing value
student["roll no"]=674
print(student)

#adding another key:value.
student["Attendance"]=100
print(student)

#check if key exists
if "Attendance" in student:
    print(student["Attendance"])

#we can remove using 'pop'.


