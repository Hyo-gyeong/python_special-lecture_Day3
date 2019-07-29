

start = int(input("시작값을 입력하세요."))
end = int(input("끝값을 입력하세요."))
add = int(input("증가값을 입력하세요."))

addsum = -start

for i in range(start, end + 1, add):
    addsum += i
    

print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" % (start, end, add, addsum))




'''
num = int(input("단을 입력하세요."))

for i in range(1,10,1):
    print("%d x %d = %d\n" % (num, i, num * i))
'''



'''
print("구구단 출력\n")

for i in range(2, 10, 1):
    for k in range(1, 10, 1):
        print("%d x %d = %d"% (i, k , i*k))
    print("\n")
'''




'''
for j in range(2, 10, 1):
    print("##  %d단 ##"% j, end='\t')
 
for k in range(1, 10, 1):
    for i in range(2, 10, 1):
        print("%d x %d = %d" % (i, k, i*k), end='\t')#새로운 내용!
    print(" ")
'''



#이렇게 구구단 가로로 출력할 수도 있음.
'''    
num = ''
for i in range(2,10):
    for k in range(1,10):
        num = num + str("%d x %d = %d\t" % (i, k,i*k))
    print("\t\t\t\t")
print(num)
'''




"""
number = int(input("정수를 입력하시오."))
'''
numSum = 0

while num > 0:
    each = num % 10
    numSum += each
    num = (num - each) // 10
print(f"각 자리수의 합: {numSum}")
'''
#이런 방법도 있음. 복습해서 내꺼로 만들기!!!!
sum = 0
while number != 0:
    sum = sum + number % 10
    number = number // 10
print(sum)

"""
























