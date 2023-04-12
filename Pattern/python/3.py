user_input = int(input())

for i in range(0,user_input):
    for j in range(0,user_input - i):
        print("*",end=" ")
    print()