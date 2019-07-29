'''
import turtle as t

t=t.Pen() #t.으로 사용해야 함!


i = 0
while i < 5:
    r_l = input("left또는 right를 입력하세요: ")

    if r_l == 'left':
        t.left(45)
        t.forward(50)
        
    elif r_l == 'right':
        t.right(45)
        t.forward(50)
        
    i += 1
'''


    
