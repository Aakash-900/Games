# def message(name):
#     print("Have a good day , "+name)

# message("Niraj dai")

# def multi(num1, num2):
#     a = num1 * num2
#     return a
    

# result = multi(5, 5)

# print(result)


# def factorial_recursive(n):
#     if n==0 or n ==1:
#         return 1
#     return n * factorial_recursive(n - 1)

# print(factorial_recursive(4))


#write a program using function to find the greatest of three number 


# def maximum(num1 , num2 , num3 ):
#     if (num1>num2):
#         if (num1>num3):
#             return num1
#         else:
#             return num3

#     else:
#         if (num2>num3):
#             return num2
#         else:
#             return num3

# print(maximum(40,90,30))

# print("hello, ", end=" ")
# print("niraj dai", end=" ")
# print("k gardai ", end=" ")
# print("hununcha", end=" ") 


# def sum(n):
#     if n == 1 or n == 0:
#         return n 
#     else:
#         a = sum(n-1)+n
#         return a

# print(sum(16))




# n = int(input('Enter the number for multiplication: '))

# def table(num):
#     for i in range(1,11):
#         print(num, 'X', i ,"=", num*i)

# print(table(n))

n = int(input('Enter the number '))

def multi(n):
    for i in range(1,11):
        print(n,'X',i,'=', n*i)

print(multi(n))

        

    