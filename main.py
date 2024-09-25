#Activity1
# def printno(n):
#     iteration=0
#     print("The total number entered by user: ",n)
#     iteration=iteration+1
#     print("The total number of iterations done by computer are: ",iteration)
# printno(10)
# printno(1500)
#Activity2
# def Ontime(n):
#     iterations=0
#     for i in range (1,n+1):
#         iterations=iterations+1
#     print("When n is ",n,"the number of iterations are ",iterations)
# Ontime(15)
#Activity3
def test(n):
    iteration=0
    for i in range(0,n):
        for j in range (0,n):
            print("*",end="")
            iteration+=1
        print("")
    print("When n is ",n,"number of iterations are ",iteration)
test(15)