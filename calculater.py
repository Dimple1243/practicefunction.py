def calculater(num1,operator,num2):
    if operator=="+":
        return num1+num2  
    elif operator=="-":
        return num1-num2
    elif operator=="/":
        return num1/num2
    elif operator=="*":
        return num1*num2
    elif operator=="**":
        return num1**num2
    elif operator=="//":
        return num1//num2
    elif operator=="%":
        return num1%num2
def solve(question_list):
    if len(question_list)==1:
        return int(question_list[0])
    elif len(question_list)==3:
        return operator(int(question_list[0]), question_list[1], int(question_list[2]))
    else:
        return operator(solve(question_list[:-2]), question_list[-2], int(question_list[-1])) 

solve(['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9', '/', '3'])

calculater()
solve()



# multiple_list =[5, 10, 50, 20] 
# b=[2, 20, 3, 5]
# i=0
# m=1
# while i<len(multiple_list):
#     print(multiple_list[i]*b[i])
#     i=i+1

    

