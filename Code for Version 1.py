l=input("Enter Name which u want to display in * pattern format: ")
for i in range(1,6):
    for k in l:
        if k=='A':
            for j in range(1, 6):
                if j == 1 or j == 5 or i==1 or i == 3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='B':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or j == 5 or i==3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='C':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 :
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='D':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or j == 5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='E':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or  i==3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='F':
            for j in range(1, 6):
                if i == 1  or j == 1 or  i==3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='G':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or (j==5 and i>=3) or (i==3 and j>2):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='H':
            for j in range(1, 6):
                if i==3 or j == 1 or j == 5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='I':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='J':
            for j in range(1, 6):
                if i== 1 or (i == 5 and j<3) or j==3 :
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='K':
            for j in range(1, 6):
                if j== 1 or (i>=3 and i==j) or (i<=3 and i+j==6):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='L':
            for j in range(1, 6):
                if i == 5 or j == 1 :
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='M':
            for j in range(1, 6):
                if j == 1 or j == 5 or ((i == j or i + j == 6) and (i <= 3)):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='N':
            for j in range(1, 6):
                if j == 1 or j == 5 or i==j:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='O':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or j == 5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='P':
            for j in range(1, 6):
                if i == 1  or j == 1 or (j == 5 and i<3) or i==3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='Q':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or j == 5 or (i>=3 and i==j):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='R':
            for j in range(1, 6):
                if i == 1  or j == 1 or (j == 5 and i<3) or i==3 or (j>2 and i==j):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='S':
            for j in range(1, 6):
                if i == 1 or i == 5 or i==3 or (j==1 and i<3) or (j==5 and i>3):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='T':
            for j in range(1, 6):
                if i == 1 or  j == 3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='U':
            for j in range(1, 6):
                if i == 5 or j == 1 or j == 5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='V':
            for j in range(1, 6):
                if (j==1 and i<=3) or (j==5 and i<=3) or (i==5 and j==3) or (i==4 and j==2) or (i==4 and j==4):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='W':
            for j in range(1, 6):
                if j == 1 or j == 5 or (j==3 and 5>i>=3):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='X':
            for j in range(1, 6):
                if i==j or i+j==6:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='Y':
            for j in range(1, 6):
                if (i==j and i<3) or (i+j==6 and i<3) or (i>=3 and j==3):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")


        elif k=='Z':
            for j in range(1, 6):
                if i+j==6 or i==1 or i==5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
    print()

