

"""
L = local
E = Enclose
G = Global
B = Built in

"""


var1 = 40 # global

def test_scope():
    x = 12 # enclose

    global var1

    var1 = 12

    def func2():
        y = 50 # local
        
        nonlocal x 
        x = 0

        print("in func2 ", x)

    func2() 

    print(x)



test_scope()




print(var1)



[[1,2], [5,4]]




