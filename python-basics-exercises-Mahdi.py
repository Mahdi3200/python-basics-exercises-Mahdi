# DAY 1 – Variables & Printing
# TASK 1 – VARIABLE 1
name = "Alice"
age = 25
is_student = True
print(name, age, is_student)

# TASK 2 – VARIABLE 2
country = "Netherlands"
population = 17500000
is_eu_member = True
print(f"{country} has a population of {population} and EU membership: {is_eu_member}")

# TASK 3 – VARIABLE 3
a = 12
b = 4
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)


# DAY 2 – More Variables Practice

# TASK 4 – VARIABLE 4
first_name = "Mahdi"
last_name = "Mousavi"
full_name = first_name + " " + last_name
print(full_name)

# TASK 5 – VARIABLE 5
product_price = 15.5
product_quantity = 3
total_cost = product_price * product_quantity
print("Total cost:", total_cost)

# TASK 6 – VARIABLE 6
radius = 5
pi = 3.14159
area = pi * radius**2
print("Area of circle:", area)

# TASK 7 – VARIABLE 7
birth_year = 1999
current_year = 2025
age = current_year - birth_year
print("Age:", age)

# TASK 8 – VARIABLE 8
celsius = 30
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# TASK 9 – VARIABLE 9
km = 10
meters = km * 1000
print("Meters:", meters)

# TASK 10 – VARIABLE 10
monthly_salary = 3000
yearly_salary = monthly_salary * 12
print("Yearly salary:", yearly_salary)


# DAY 3 – Methods & String Manipulation

# TASK 11 – METHODS 1
def square(num):
    return num * num

# TASK 12 – METHODS 2


def print_name_age(name, age):
    print(f"{name} is {age} years old.")

# TASK 13 – METHODS 3


def multiply(a, b):
    return a * b

# TASK 14 – METHODS 4


def even_or_odd(number):
    return "even" if number % 2 == 0 else "odd"

# TASK 15 – METHODS 5


def largest_of_three(a, b, c):
    return max(a, b, c)


# TASK 16 – STRING MANIPULATION
text = " Python programming is awesome! "
stripped = text.strip()
length = len(stripped)
uppercased = stripped.upper()
replaced = stripped.replace("awesome", "powerful")

print(stripped, length, uppercased, replaced, sep="\n")

# TASK 17 – ADVANCED STRING MANIPULATION
email = "student@example.com"
username = email.split("@")[0]
domain = email.split("@")[1]
print(f"Username: {username}, Domain: {domain}")


# DAY 4 – Math Operators

# TASK 18
x = 15
y = 4
print(x + y, x - y, x * y, x / y, x % y)

# TASK 19
counter = 0
counter += 1
counter += 1
counter += 1
counter -= 1
counter -= 1
print("Counter:", counter)

# TASK 20 – FREE EXERCISE


def greet(name):
    return f"Hello, {name}!"


user = "Alice"
msg = greet(user)

number = 7
square_result = square(number)

sentence = f"{msg} The square of {number} is {square_result}."
print(sentence)
