# ENSF 592 Spring 2023
# May 9 Lab 2
# Exercise 2


# Trace through the execution of the following program. 
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar

print(foo)
print(type(foo))
print(bar)
print(type(bar))

# POINT 1
# What is the value of foo at this point?
# foo: 100
# What is the type of foo at this point?
# foo type: int
# What is the value of bar at this point?
# bar: 100
# What is the type of bar at this point?
# bar type: int

spam = foo + bar
foo += 50
eggs = foo + bar
ham = [1, 2, 3]
baz = ham
ham.append(bar)

# POINT 2
# What is the value of foo at this point?
# foo: 150
# What is the value of bar at this point?
# bar: 100
# What is the value of spam at this point?
# spam:200
# What is the value of eggs at this point?
# eggs: 250
# What is the value of ham at this point?
# ham: [1, 2, 3, 100]
# What is the value of baz at this point?
#baz: [1, 2, 3, 100]

eggs = "Python is very flexible!"
spam = ham
ham = bar
bar += bar
foo = eggs
eggs = bar + ham
baz.append(bar)

# POINT 3
# What is the value of foo at this point?
# foo: 'Python is very flexible!'
# What is the value of bar at this point?
# bar: 200
# What is the value of spam at this point?
# spam: [1, 2, 3, 100]
# What is the value of eggs at this point?
# eggs: 300
# What is the value of ham at this point?
# ham: 100
# What is the value of baz at this point?
# baz: [1, 2, 3, 100, 200]

# Print out the types and final values of each variable.
