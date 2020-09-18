l=input("Enter Name which u want to display in * pattern format: ")
for i in range(1,6):
    for k in l:
        if k=='A' or k=='a' :
            for j in range(1, 6):
                if j == 1 or j == 5 or i==1 or i == 3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='B' or k=='b':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or j == 5 or i==3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='C'or k=='c':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 :
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='D'or k=='d':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or j == 5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='E' or k=='e':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or  i==3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='F'or k=='f':
            for j in range(1, 6):
                if i == 1  or j == 1 or  i==3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='G'or k=='g':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or (j==5 and i>=3) or (i==3 and j>2):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='H'or k=='h':
            for j in range(1, 6):
                if i==3 or j == 1 or j == 5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='I'or k=='i':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='J'or k=='j':
            for j in range(1, 6):
                if i== 1 or (i == 5 and j<3) or j==3 :
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='K'or k=='k':
            for j in range(1, 6):
                if j== 1 or (i>=3 and i==j) or (i<=3 and i+j==6):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='L'or k=='l':
            for j in range(1, 6):
                if i == 5 or j == 1 :
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='M'or k=='m':
            for j in range(1, 6):
                if j == 1 or j == 5 or ((i == j or i + j == 6) and (i <= 3)):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='N'or k=='n':
            for j in range(1, 6):
                if j == 1 or j == 5 or i==j:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='O'or k=='o':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or j == 5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='P'or k=='p':
            for j in range(1, 6):
                if i == 1  or j == 1 or (j == 5 and i<3) or i==3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='Q'or k=='q':
            for j in range(1, 6):
                if i == 1 or i == 5 or j == 1 or j == 5 or (i>=3 and i==j):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='R'or k=='r':
            for j in range(1, 6):
                if i == 1  or j == 1 or (j == 5 and i<3) or i==3 or (j>2 and i==j):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='S'or k=='s':
            for j in range(1, 6):
                if i == 1 or i == 5 or i==3 or (j==1 and i<3) or (j==5 and i>3):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='T'or k=='t':
            for j in range(1, 6):
                if i == 1 or  j == 3:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='U'or k=='u':
            for j in range(1, 6):
                if i == 5 or j == 1 or j == 5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='V'or k=='v':
            for j in range(1, 6):
                if (j==1 and i<=3) or (j==5 and i<=3) or (i==5 and j==3) or (i==4 and j==2) or (i==4 and j==4):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='W'or k=='w':
            for j in range(1, 6):
                if j == 1 or j == 5 or (j==3 and 5>i>=3):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='X'or k=='x':
            for j in range(1, 6):
                if i==j or i+j==6:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        elif k=='Y'or k=='y':
            for j in range(1, 6):
                if (i==j and i<3) or (i+j==6 and i<3) or (i>=3 and j==3):
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")


        elif k=='Z'or k=='z':
            for j in range(1, 6):
                if i+j==6 or i==1 or i==5:
                    print('*', end="")
                else:
                    print(" ", end="")
            print(" ", end="")
    print()

