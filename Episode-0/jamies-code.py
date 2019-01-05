# This line is a comment, as it starts with a pound symbol/hash character

# The following line is a statement, it prints the literal string
# "hello, world!" to the console
print('hello, world!')

# This pair of statements creates a variable (called 'name') and assigns
# it the value of "GaProgMan", then the value of the 'name' variable is used
# as part of an f-string within the print statement.
name = 'GaProgMan'
print(f"hello, {name}")

# At runtime, the Python engine combines the string literal (i.e 'hello, ')
# with the value of the variable (i.e. name, which has a value of "GaProgMan")
# before sending the combined value to the print method