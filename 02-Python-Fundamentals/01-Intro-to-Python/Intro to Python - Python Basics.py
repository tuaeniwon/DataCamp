#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Hello Python!
-Video

### The Python Interface
...
In the Python script on the right, you can type Python code to solve the exercises. If you hit Run Code or Submit Answer, your python script (script.py) is executed and the output is shown in the IPython Shell. Submit Answer checks whether your submission is correct and gives you feedback.

You can hit Run Code and Submit Answer as often as you want. If you're stuck, you can click Get Hint, and ultimately Get Solution.

You can also use the IPython Shell interactively by simply typing commands and hitting Enter. When you work in the shell directly, your code will not be checked for correctness so it is a great way to experiment.
...
Instructions - 100 XP
-Experiment in the IPython Shell; type 5 / 8, for example.
-Add another line of code to the Python script on the top-right (not in the Shell): print(7 + 10).
-Hit Submit Answer to execute the Python script and receive feedback.

# Example, do not modify!
print(5 / 8)

# Print the sum of 7 and 10
print(7 + 10)


###When to use Python?
...
get_ipython().set_next_input('Python is a pretty versatile language. For which applications can you use Python');get_ipython().run_line_magic('pinfo', 'Python')

## Possible Answers

# A You want to do some quick calculations.
# B For your new business, you want to develop a database-driven website.
# C Your boss asks you to clean and analyze the results of the latest satisfaction survey.
# D All of the above. < ------- Correct


### Any comments?
...
Something that Hugo didn't mention in his videos is that you can add comments to your Python scripts. Comments are important to make sure that you and others can understand what your code is about.

To add comments to your Python script, you can use the # tag. These comments are not run as Python code, so they will not influence your result. As an example, take the comment on the right, # Division; it is completely ignored during execution.
...
Instructions - 100 XP
-Above the print(7 + 10), add the comment # Addition.

# Division
print(5 / 8)

# Addition
print(7 + 10)


### Python as a calculator
...
Python is perfectly suited to do basic calculations. Apart from addition, subtraction, multiplication and division, there is also support for more advanced operations such as:

Exponentiation: **. This operator raises the number to its left to the power of the number to its right. For example 4**2 will give 16.
Modulo: %. This operator returns the remainder of the division of the number to the left by the number on its right. For example 18 % 7 equals 4.
The code in the script on the right gives some examples.
...
Instructions - 100 XP
-Suppose you have $100, which you can invest with a 10% return each year. After one year, it's 100×1.1=110 dollars, and after two years it's 100×1.1×1.1=121. Add code to calculate how much money you end up with after 7 years, and print the result.

# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100 * 1.1**7)


### Variables and Types
-Video


### Variable Assignment
...
In Python, a variable allows you to refer to a value with a name. To create a variable use =, like this example:

    x = 5

You can now use the name of this variable, x, instead of the actual value, 5.

Remember, = in Python means assignment, it doesn't test equality!
...
Instructions - 100 XP
-Create a variable savings with the value 100.
-Check out this variable by typing print(savings) in the script.

# Create a variable savings
savings = 100

# Print out savings
print(savings)


### Calculations with variables
...
Remember how you calculated the money you ended up with after 7 years of investing $100? You did something like this:

    100 * 1.1 ** 7

Instead of calculating with the actual values, you can use variables instead. The savings variable you've created in the previous exercise represents the $100 you started with. It's up to you to create a new variable to represent 1.1 and then redo the calculations!
...
Instructions -100 XP
-Create a variable growth_multiplier, equal to 1.1.
-Create a variable, result, equal to the amount of money you saved after 7 years.
-Print out the value of result.


# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = 100 * 1.1**7

# Print out result
print(result)


### Other variable types
...
In the previous exercise, you worked with two Python data types:

    -int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.

    -float, or floating point: a number that has both an integer and fractional part, separated by a point. growth_multiplier, with the value 1.1, is an example of a float.

Next to numerical data types, there are two other very common data types:

    -str, or string: a type to represent text. You can use single or double quotes to build a string.

    -bool, or boolean: a type to represent logical values. Can only be True or False (the capitalization is important!).
...
Instructions - 100 XP
-Create a new string, desc, with the value "compound interest".
-Create a new boolean, profitable, with the value True.

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True


### Guess the type
...
To find out the type of a value or a variable that refers to that value, you can use the type() function. Suppose you've defined a variable a, but you forgot the type of this variable. To determine the type of a, simply execute:

    type(a)
    
get_ipython().set_next_input('We already went ahead and created three variables: a, b and c. You can use the IPython shell on the right to discover their type. Which of the following options is correct');get_ipython().run_line_magic('pinfo', 'correct')
...
Instructions - 50 XP

## Possible Answers

# A a is of type int, b is of type str, c is of type bool
# B a is of type float, b is of type bool, c is of type str
# C a is of type float, b is of type str, c is of type bool < ------- Correct
# D a is of type int, b is of type bool, c is of type str


### Operations with other types
...
Hugo mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.
...
Instructions - 100 XP
-Calculate the product of savings and growth_multiplier. Store the result in year1.
-What do you think the resulting type will be? Find out by printing out the type of year1.
-Calculate the sum of desc and desc and store the result in a new variable doubledesc.
get_ipython().set_next_input('-Print out doubledesc. Did you expect this');get_ipython().run_line_magic('pinfo', 'this')

savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of savings and growth_multiplier to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc


### Type conversion
...
Using the + operator to paste together two strings can be very useful in building custom messages.

Suppose, for example, that you've calculated the return of your investment and want to summarize the results in a string. Assuming the integer savings and float result are defined, you can try something like this:

    print("I started with $" + savings + " and now have $" + result + ". Awesome!")
    
This will not work, though, as you cannot simply sum strings and integers/floats.

To fix the error, you'll need to explicitly convert the types of your variables. More specifically, you'll need str(), to convert a value into a string. str(savings), for example, will convert the integer savings to a string.

Similar functions such as int(), float() and bool() will help you convert Python values into any type.
...
Instructions - 100 XP
-Hit Run Code to run the code. Try to understand the error message.
-Fix the code such that the printout runs without errors; use the function str() to convert the variables to strings.
-Convert the variable pi_string to a float and store this float as a new variable, pi_float.

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)


### Can Python handle everything?
...
Now that you know something more about combining different sources of information, have a look at the four Python expressions below. Which one of these will throw an error? You can always copy and paste this code in the IPython Shell to find out!
...
Instructions - 50 XP

## Possible Answers

# A "I can add integers, like " + str(5) + " to strings."
# B "I said " + ("Hey " * 2) + "Hey!"
# C "The correct answer to this multiple choice exercise is answer number " + 2 < ------- Correct
# D True + False

