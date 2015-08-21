''' File Log:
    Version 0.01 05/10/2011 Kevin (Login Logic)
    Version 0.02 08/09/2011 Jonathan (Userlevel Logic)


'''

def Validate(user, passw, Accountlist):
    for i in range(len(Accountlist[0])):
        if Accountlist[0][i]==user:
            if Accountlist[1][i]==passw:
                lis=[Accountlist[2][i],Accountlist[3][i]]
                return lis
            else:
                return False
    return False
