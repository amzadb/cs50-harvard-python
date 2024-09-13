# Read the mass in kgs and calculate the energy in joules
# using the formula E = mc^2

# Read the mass in kgs
mass = int(input("Enter the mass in kgs: "))

# Calculate the energy in joules
energy = mass * 300000000**2

# Display the energy in joules
print("m:", mass, "kg")
print("E:", energy, "J")