import json
from tabulate import tabulate
 

#loading json file
with open('students.json','r') as file:
    students = json.load(file)


#Saving the changes in json file
def save_file():
    with open('students.json','w') as file:
        json.dump(students,file,indent=4)


#Addition of new Student
def add_students():
    while True:
        roll = input("Enter Rollno No : ")
        duplicate=False
        for student in students:
            if student["Rollno"]==roll:
                duplicate=True
        if duplicate==True:
            print("Rollno number already exists")
        elif roll.strip() == "":
            print("Rollno number cannot be empty")
        elif roll.isdigit() == False:
            print("Rollno no. must be a number")
        else:
            break

    # Name validation
    while True:
        name = input("Enter Name : ")
        if name.strip() == "":
            print("Name cannot be empty")
        elif name.replace(" ", "").isalpha() == False:
            print("Name should contain only letters")
        else:
            break

    # Age validation
    while True:
        age = input("Enter Age : ")
        if age.isdigit() == False:
            print("Age must be a number")
        else:
            age = int(age)
            if age <= 0 or age > 100:
                print("Enter valid age")
            else:
                break
    students.append({"Rollno":roll,"Name":name,"Age":age})
    print("Student successfully Added !!")
    save_file()


#Displaying All the Students
def view_students():
    print(tabulate(students,headers="keys",tablefmt="grid"))


#Updation of a Existing Student
def update_students():
    rollno=input("Enter a Rollno to update :")
    found = False
    for student in students:
        if student["Rollno"]==rollno:
            #Name Validation
            while True:
                student["Name"]= input("Enter New Name :")
                if student["Name"].strip()=="":
                    print("Name cannot be Empty")
                elif student["Name"].replace(" ","").isalpha()==False:
                    print("Name should contain only letters")
                else:
                    break
            #Age Validation
            while True:
                student["Age"]= input("Enter New Age :")
                if student["Age"].isdigit() == False:
                    print("Age must be a number")
                else:
                    break
            print("Student successfully Updated !!")
            found = True
            save_file()
            break
    if found==False:
            print("No Record Found!!!")


#Deletion of a New student
def delete_students():
    found = False
    rollno=input("Enter a Rollnono of student you want to delete :")
    for student in students:
        if student["Rollno"]==rollno:
            students.remove(student)
            print("Student successfully Deleted!!")
            found = True
            save_file()
            break       
    if found==False:
            print("No Record Found!!!")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice :"))
    if choice==1:
        add_students()
    elif choice==2:
        view_students()
    elif choice==3:
        update_students()
    elif choice==4:
        delete_students()
    elif choice==5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")

