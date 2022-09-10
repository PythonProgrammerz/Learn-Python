from random import *

num = randint(1, 30)
print("Roll NO:", num)
name = choice(["Harshit Mandal", "Ayush Raj", "Arsham Malik", "Priyam Aggarwal", "Mayank ", "Aadarsh",
               "Aman Singh", "Arihant Maurya", "Piyush Kumar Singh", "Harshit Verma"])
print("Name:", name)
print("Class: 8B ")
date = randint(1, 28)
Month = choice(["January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"])
Year = choice(["2008", "2009", "2007"])
print("DOB:", date, Month, Year)
