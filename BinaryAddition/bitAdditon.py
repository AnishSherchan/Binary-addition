import gateAnd as G1
import gateOr as G2
import gateXor as G3
def bitAdditon(list1,list2):
    A=[]
    B=[]
    for i in range(len(list1)-1,-1,-1):
        A.append(list1[i])
    for i in range(len(list2)-1,-1,-1):
        B.append(list2[i])
    FinalSum=[]
    output=[]
    CI=0
    for i in range(0,8):
        sum1=G3.gateXor(A[i],B[i])
        Fsum=G3.gateXor(sum1,CI)
        FinalSum.append(Fsum)
        Co1=G3.gateXor(A[i],B[i])
        Co2=G1.gateAnd(CI,Co1)
        Co3=G1.gateAnd(A[i],B[i])
        finalCout=G2.gateOr(Co2,Co3)
        CI=finalCout
    for i in range(len(FinalSum)-1,-1,-1):
        output.append(FinalSum[i])
    finaloutput=[]
    finaloutput=output
    count=-1
    for i in range(0,len(output)):
        count=count+1
        if output[i]==1:
            break
    for i in range(0,count):
        del(finaloutput[0])
    
    result=""
    for i in range(0,len(finaloutput)):
        result=result+str(finaloutput[i])
    return result
