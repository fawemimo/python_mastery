# TERNARY OPERATOR
age = 12
message = "Eligible" if age >= 18 else "Not eligible"

print(message)

# LOGICAL OPERATOR
"""
AND
OR
NOT
"""
high_income = True
good_credits = True

message = "Eligible" if high_income and good_credits else "Not eligible"

print(message)

# comparison operator
age = 22
if 18 <= age < 65:
    print("OK")

# LOOP    #
for number in range(1, 10, 2):
    print(f'Number:{number} {(number + 2) * "."}')

# for else flow
succussful = True
for number in range(3):
    print("Attempt")
    if not succussful:
        print("Successfull")
        break

else:
    print("Attempted 3 times and failed")


# Nested Loop
# for x in range(5):
#     for y in range(3):
#         print(f'({x}, {y})')

# STRINGS ARE ALSO ITEREABLE
number = 100
while number > 0:
    print(number)
    number //= 2