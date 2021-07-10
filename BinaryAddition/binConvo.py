def binConvo(Deci):            #Function for changing Decimal to binary 
    DuplicateBin=[]
    ActualBin=[]
    flag = True
    while flag == True:     #While loop for chaing Decimal to Binary
        for i in range(0,8):
            Remi = Deci % 2
            DuplicateBin.append(Remi)
            Ques = Deci // 2
            Deci = Ques
            if Deci == 0:
                flag = False
            else:
                flag = True 
    for i in range (len(DuplicateBin)-1,-1,-1):   #Loop for Reversing the list given as output from BinConvo For making ActualBinary Number
        ActualBin.append(DuplicateBin[i])
    return ActualBin