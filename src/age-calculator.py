msg = "What is your age? "

# Everything from input is a 'string'
age = input(msg)
decades = int(age) // 10
yrsReamining = int(age) % 10
respones1 = f"You are {age} years old!"
response2 = f"You are {decades} decades and {yrsReamining} old"
print(respones1)
print(response2)
