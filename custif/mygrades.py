#!/usr/bin/env python3

################################
## Message that will display 
################################

message = "Your final grage is, "

################################
# Obtaining value
################################


grade = float(input('What is your grade percentage? '))
print('\n')

################################
# Display Grade
################################
if grade >= 90:
	message = message + 'an A.'
elif grade >= 80:
	message = message + 'a B.'
elif grade >= 70:
	message = message + 'a C.'
elif grade >= 60:
	message = message + 'a D.'
else:
	message = message + 'an F.'

#############################
# Print message
#############################

print(message)
