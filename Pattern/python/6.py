user_input = int(input())


def fun(num):
    for i in range(1,num+1):
        for j in range(1,num + i):
            # if user_input == j:
                print("*",end="")
            # else:
            #     print(" ",end="")
        print()

fun(user_input)
