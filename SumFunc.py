def getSum(a):
    return int(a*(a+2)/2)
n = int(input("더할 정수를 입력하세요 : "))
print(getSum(n))

def getSubstract(a):
    return int(a*(a-2)/2)
m = int(input("뺄 정수를 입력하세요 : "))
print(getSubstract(n))