astring = "Hello World!"

# length
print(len(astring))

# index
print(astring.index("o"))

# count
print(astring.count("l"))

# slicing
print(astring[3:7])
print(astring[:5])
print(astring[-3:])

# reversing
print(astring[::-1])

# upper/lower
print(astring.upper())
print(astring.lower())

# exercise
s = "Strings are awesome!"

# use len
print(f"Length: {len(s)}")

# use method .find
print(f"1st 'a' at index: {s.find('a')}")

# use negative slicing
print(f"Last 5 characters: {s[-5:]}")

# use method upper
print(f"Uppercase: {s.upper()}")