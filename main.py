#Functions
    #Functions can take in parameters, which we can then pass arguments when invoking the function --> NOTE: We can also provide a Default Parameter, which will use that default value if we DO NOT pass an arguement for that parameter at function invokation - IMPORTANT: Once we set a parameter to have a default value, all subsequent parameters MUST have a default value
def greet(years ,name="Chris", city="Chicago"):
    print(F"Hello, {name}, the city of {city} is a beautiful place. I can't believe you've been living here for {years} years.")

greet(20, "Wendy", "California")

#Keyword Arguments: Setting the parameter equal to the argument WILL NOT matter how we list the arguents at funciton invocation time
def amazing(person, occupation):
    print(F"{person} is a {occupation} and is an amazing person!")

amazing(occupation="Software Engineer", person="Christopher Jimenez")

#Prime Number Checker: Prime numbers can only be divided cleanly by 1 and itself - Write a function that checks if input number is a prime number ( 1 - 100)
def prime_checker(number):
  dividends = []
  for num in range(1, 101):
    if number % num == 0:
      dividends.append(num)
  if len(dividends) >= 3:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")

prime_checker(10)