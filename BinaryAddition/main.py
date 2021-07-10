import binConvo as B1
import bitAdditon as add1


ContinueLoop = True
Try = True
while ContinueLoop == True:
    while Try == True:
        try:
            Num = int(input("Enter First Decimal Number : "))
            flag1 = True
            while flag1 == True:
                if Num < 255 and Num >= 0:
                    flag1 = False
                    Try = False
                    A = B1.binConvo(Num)
                else:
                    print("Error Try again !!")
                    Num = int(input(
                        "Please Enter Decimal Number between 0-254 and the first number cannot be 255 as it last number of 8 bit : "))
                    flag1 = True
        except:
            print("Error!! \nPlease Enter Integer from 0-255")
    while Try == False:
        try:
            Num2 = int(input("Enter Second Decimal NUmber : "))
            flag1 = True
            if Num+Num2 > 255:
                print(
                    "Error!! Addition of 8 bit can only be performed please enter number whose sum is less than 255!!")
            else:
                flag1 = False
            while flag1 == False:
                if Num2 < 256 and Num2 >= 0:
                    flag1 = True
                    Try = True
                    B = B1.binConvo(Num2)
                else:
                    print("Error Try again !!")
                    Num2 = int(
                        input("Please Enter Decimal Number between 0-255 : "))
                    flag1 = False
        except:
            print("Error!! \n Please Enter Integer from 0-255")
    first = ""
    second = ""
    for i in range(0, len(A)):
        first = first+str(A[i])
    for i in range(0, len(B)):
        second = second+str(B[i])
    output = add1.bitAdditon(A, B)
    print("The binary Conversion of", Num, "is", first)
    print("The binary Conversion of", Num2, "is", second)
    print("-----------------------------------------------------------------------------")
    print("\n The Addtion of following Binary Numbers are given below!!\n")
    print("\t ", first)
    print("\t+", second)
    print("\t ---------")
    print("\t ", output)
    print("---------------------------------------------------------------------------------")
    Continue = input("Do you want to continue (Y/N) : ").lower()
    if Continue == "y":
        ContinueLoop = True
    else:
        ContinueLoop = False
