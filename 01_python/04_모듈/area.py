print(f'area 모듈 이름: {__name__}') # __main__

PI = 3.14 # 상수는 대문자로 변수 지정 

def circle(radius):
    return radius * radius * PI

def square(length):
    return length * length


print(circle(2) == 12.56)
print(circle(5) == 78.5)
print(square(2) == 4)
print(square(5) == 35)