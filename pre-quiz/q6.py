a = [1,2,3] 
b = a
print(a == b) # True
print(a is b) # True

b = a[:]
print(a == b) # True
print(a is b) # False

# Why is the last line False?
# A. a and b are different objects that have identical content
# B. a and b are different objects that have different content
# C. a and b are the same object
# D. This code contains an error
# E. b is empty list

# Answer: A. a and b are different objects that have identical content