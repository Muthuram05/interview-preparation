user_input = int(input())

for i in range(0,user_input+1):
    for j in range(0,i):
        print("*",end= " ")
    print()
for i in range(0,user_input):
    for j in range(1,user_input - i):
        print("*",end=" ")
    print()