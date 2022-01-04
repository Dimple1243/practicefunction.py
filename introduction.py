# def ask_question ():
#     print("Who is the founder of Facebook?")
#     print("- Mark Zuckerberg")
#     print("- Bill Gates")
#     print("- Steve Jobs")
#     print("- Larry Page")


# ask_question ()
# ask_question ()
# ask_question ()
# ask_question ()    


# print((lambda x,y:x+y)(2,3))

# sum=lambda x,y=3: x+y

# print(sum(3))


# mylist = [5, 7, 8, 10, 14, 15, 20]

# def even(num):
#     if num%2==0:
#         return True
#     else:
#         return False


# new_list=list(filter(even,mylist))
# print("filtered list:",new_list)        

# new_list=list(filter(lambda num:num%2==0,mylist))
# print("filtered list:",new_list)

# my_range=range(1,11)
# new_list=list(filter(lambda num:num%2==0,my_range))
# print("filtered:" ,new_list)

# def multiply(num):
#     return num*2

# new_list=list(map(multiply,mylist))
# print("modified:- ",new_list)    


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# def add(num1,num2):
#     return num1+num2

# new_list=list(map(add,list1,list2))
# print("modified:- ",new_list)

# def find_power(num):
#     def power(n):
#         return num**n
#     return power(2)
# print(find_power(10))

# def print_even(lst):
#     def find_even(num):
#         if num%2==0:
#             return True
#         else:
#             return False
#     new_list=[]
#     for num in lst:
#         if find_even(num)==True:
#             new_list.append(num)
#     print("final list",new_list)
# new_list=[1,2,3,4,5,6,7,8,9,10,11]    
# print_even(new_list)

str="hello"
print(str[:3])
