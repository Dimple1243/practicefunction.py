# def add(a,b):
#     c=a+b
#     print("ADDITION" ,c)
# a=int(input("enter 1 num "))
# b=int(input("enter 2 num "))
# add(a,b)


# def name(name):
#     print(name+"divya")

# name("email")
# name("contact")
# name("address")


   

# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")




# def my_function(**kid):
#   print("Her last name is " + kid["lname"])

# my_function(fname = "divya", lname = "khurana")


# def my_function(country="Delhi"):
#     print("I Am From " + country)
# my_function("Punjab")
# my_function("Haryana")
# my_function()
# my_function("Bihar")    


# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def my_function(x):
#     print(6*x)   

# my_function(3)
# my_function(5)
# my_function(9)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)