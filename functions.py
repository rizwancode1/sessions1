# functions in python 

def greet_user(name):

    if type(name) != str:
        print("Error:  Name must be string ")
        return

    # print(f"Hello {name}")

    # greet_response = f'hi {name}'

    return f'hi {name}'

result1 = greet_user('Riz')


# print(result1)

# def square(num):
#     if type(num) != int:
#         print("Error: Please provide a number")
#         return

#     return (num **2)



# result = square(5)

# print(result)


def add2 (num1,num2):
    result = num1 + num2
    return result


result3 = add2(10, 49)


print(result3)


add = lambda x,y : x+y 


# result2 = add(1,5)

# print(result2)


def test(*args, **kwargs):
    pass

