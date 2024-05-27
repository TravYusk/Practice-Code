# Travis Yuskevich
# SPC ID 2543201
# The user inputs the number of hours they desire.
# Calculate the number of days by dividing the total hours by 24.
# Remaining hours are incorporated by %.
# The output is then displayed in days and hours.

# Input the number of hours from the user
hours = int(input('What is the number of hours to convert to days and hours: '))

# Calculate days and remaining hours
days = hours // 24
remaining_hours = hours % 24

# Output to display the result
print(f'{hours} hours is equivalent to {days} days and {remaining_hours} hours')
