#-->File handling

#-->Writing a file
file = open("Testing.txt","w")
# w stands for writing mode and will create a file if not exist
file.write("Hello World \nHello Nepal \nHello Sir")
#writes into a new file
file.close()
    #When a file is opened in write mode, exisiting the content is deleted


#-->Reading a file
file = open("Testing.txt","r")
# r stands for reading mode
print(file.read(2))
# argument takes 1 character as 1 byte and prints it
print(file.read())
# after 2 characters are printed it prints the remaining characters


#-->Reading each line in a file
for line in file:
    print(line)
    #OR we can use file.readlines() function
file.close()


#Example:
file1 = open("Testing.txt","r")
n = int(input())
results = file1.readlines()
#reads all lines from file
print(results[n])
#prints only the line given as argument

#Example:
names = ["John", "Hari", "Osama"]
file = open("names.txt", "w+")
for i in names:
    file.write(i+"\n")
file.close()
file = open("names.txt","r")
print(file.read())
file.close()


#-->Appending in a file
file = open("names.txt", "a")
file.write("Ram")
file.close()


#-->WITH
with open("names.txt") as f:
    print(f.read())
    #automate the closing of a file
    
#Example:
file = open("Testing.txt", "r")
s = file.readlines()
    #Reads every lines and stores in s 
for line in s:  
    # Iterates throuugh every line and strip() removes the spaces
    s1 = line.strip()
    print(line[0]+str(len(s1)))
    #Line(0) prints 1st letter and len prints the length after spaces removed   
file.close()


#-->CSV 
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
    print(student)

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)
def get_name(student):
    return student["name"]      
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
    

#Same using Lambda
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
    
    
#-->CSV Library
import csv
students=[]
with open("students1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name":row[0], "house":row[2]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
   
   
#DictReader
import csv
students = []
with open("students1.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
 
  
#DictWriter
import csv
name = input("Name: ")
home = input("Home: ")
with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames= ["name","home"])
    writer.writerow({"name":name, "home":home})
    
    

#Example:
import sys
import csv
from tabulate import tabulate

pizza=[]
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                pizza.append(row)
        print(tabulate(pizza[1:], pizza[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

#Example:
import sys
import csv

before = []
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                split_name = row["name"].split(",")
                before.append({"first":split_name[1].strip(), "last":split_name[0].strip(), "house":row["house"]})
    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])

    with open(sys.argv[2], "w") as file2:
        writer = csv.DictWriter(file2,fieldnames=["first","last","house"])
        writer.writerow({"first":'first',"last":'last',"house":'house'})
        for row in before:
            writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})
            
#Example:
import sys
import os
from PIL import Image, ImageOps

extensions = [".jpg", ".jpeg", ".png"]
file1 = sys.argv[1]
file2 = sys.argv[2]

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif os.path.splitext(file1)[1:] != os.path.splitext(file2)[1:]:
    sys.exit("Input and output have different extensions")
elif not (file1.endswith(tuple(extensions))):
    sys.exit("Invalid Input")
elif not (file2.endswith(tuple(extensions))):
    sys.exit("Invalid Output")
else:
    try:
        imagefile = Image.open(file1)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    #Opens Shirt image
    shirt = Image.open("shirt.png")
    #Measures size of shirt
    size = shirt.size
    #Resize muppet image to fit shirt
    size_fit = ImageOps.fit(imagefile, size)
    #Paste shirt in muppet
    size_fit.paste(shirt,shirt)
    #Creates output image
    size_fit.save(file2)
