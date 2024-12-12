'''
정수를 계산하는 모듈입니다.

Author: Jeon Hyeran
Created: 2024.12.12
'''

name = 'calculator'

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# my_main이 직접 실행될 때만 출력값이 나오도록 하는 방법
# 테스트 코드들이 import 시 뜨지 않도록 하는
if __name__ == '__main__':
    print('시작점')
    print(__name__)