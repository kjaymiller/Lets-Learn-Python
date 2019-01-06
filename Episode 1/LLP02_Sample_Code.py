"""
ItemTypes, Functions, Classes
"""

# Basic Item Types
# Strings
print("This a String")
print('this is also a string')

print('this string \
goes to another line OR DOES IT???')

print('''this string 
goes to another line''')

print("""this is a 
multiline string, but you shouldn't do this unless you absolutely need to! Code Confusion""")

# Integers
print('Integer', 1)

# Floats
print('Float', 1.01)

# Booleans
print('Boolean -', True)

# Comments don't return anything
# single line comments
"""Multiline
Comments*"""
    
# Iterators
# tuples
print((1,2,'strings', ('other', 'tuples'), ['even', 'lists']))

# lists
this_list = ['just', 'like', 'tuples', 'but', 'mutable']

print(this_list)

this_list.pop(2)
print(this_list)

# dictionaries

print(
    {
    'key': 'value',
    'other_key': 'value2',
    }
    )

# Sets
print({'only', 'unique', 'items', 'items'})


# functions are a series of steps that can be called throughout your program

a = True
print('a=', a) # --> True
def side_effects():
    # **Functions can manipulate things outside of the function within scope**
    a = False

side_effects()
print('After running side_effects')
print('a=', a) # --> 



a = True
print("We've set 'a' back to", a)

def no_side_effects():
    """Functions can also return values"""
    return False

no_side_effects() # Returns False

print("If we run 'no_side_effects' a is now", a)
print("""Wait Wut??!!!???
That is because this function is changing anything.
If we want it to modify 'a', we must make a equal to the result of the funtion.""")

a = no_side_effects()

a # --> False

## Classes
"""Classes allow you to create objects
and build rules around that object."""
class Brit:
    likes_crumpets = True
    talks_with_british_accent = True
    likes_silly_hats = True

Jamie = Brit()
print('Does Jamie like crumpets - ', Jamie.likes_crumpets)
print('Does Jamie talk with a British Accent - ', Jamie.talks_with_british_accent)
print('Does Jamie like silly hats - ', Jamie.likes_silly_hats)


print('Jamie also likes anime, but not all Brits')
Jamie.likes_anime = True


Mark = Brit()
Mark.likes_anime
