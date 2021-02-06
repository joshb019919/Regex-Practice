import re

s = input("Do you agree? ")

# if re.search("yes|y", s) works, but below is even more succinct.
if re.search("y(es)?", s, re.IGNORECASE):
    print("Agreed.")
elif re.search("n(o)?", s, re.IGNORECASE):
    print("Not Agreed.")

# Regex also allows for ^ and $ to require certain user input:
# if re.search("^y(es)?$", s, re.IGNORECASE):
#     print("Agreed.")
# but this would require yes to be first in input, and I don't like it
# this particular way for this particular program.