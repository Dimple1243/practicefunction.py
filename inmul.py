# def multiply_function(a):
#     i=0
#     while i<a:
#         if a%3==0:
#             print("divisible by 3")
#             if a%5==0:
#                 print("divi by 5")
#             else:
#                 print("")
#         else:
#             print(":l,")
#         i=i+1
# multiply_function(10)            

# def driver_speed(speed):
#     if speed<=70:
#         print("ok")
#         if speed>70:
#             print("for every 5km ",speed)

# def greet(*names):
#     for name in names:
#                print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

def sumofdigits(number):
    sum = 0
    modulus = 0
    while number!=0 :
        modulus = number%10
        sum+=modulus
        number/=10
    return sum

print(sumofdigits(123))