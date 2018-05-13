print ("Mike is awesome!")
print ("And so is George!")
print("The answer is", 2*2)
print ("The answer is ", 2*3)

message = "Hello Python world!"
print (message)

message = 'I told my friend, "Python is my favorite language!"'
print (message)

message = "The language 'Python' is named after Monty Python, not the snake."
print (message)

message = "One of Python's strengths is its diverse and supportive community."
print(message)

name = "aDa lovElace"
print (name.title())
print (name.upper())
print (name.lower())

first_name = "aDa"
last_name = "loveLace"
full_name = first_name + " " + last_name
print ("full_name = ", full_name.title())

message = "Hello, " + full_name.title() + "!"
print (message)

print("\tPython")
print("Languages:\nPython\nJavaScript\nScala")

favorite_language = " Python "
print (favorite_language + " rocks!")
print (favorite_language.rstrip() + " rocks!")
print (favorite_language.lstrip() + " rocks!")
print (favorite_language.strip() + " rocks!")
print (favorite_language + " rocks!")
favorite_language = favorite_language.rstrip()
print (favorite_language + " rocks!")

print (2 * 3)
print (2 ** 3)
print ((2 * 3) ** 4)
print (6*6*6*6)

x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x > y and x > z:
    maximum = x
elif y > x and y > z:
    maximum = y
else:
    maximum = z

print("The maximal value is: " + str(maximum))
print('The maximum value is:', maximum)
