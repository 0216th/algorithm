'''
문제 url : https://programmers.co.kr/learn/courses/30/lessons/42839 

핵심 : 
전체 경우의 수가 7x6x5x4x3x2x1 의 경우이므로 삼중 반복을 통해 완전 탐색을 실행함 
전체 케이스를 위해 permutations 함수를 이용해 나올수 있는 모든 경우의 수를 가져옴 
'''
from itertools import permutations 

# 소수 판별 함수 
def check_sosu(num) :     
    if num <= 1 : 
        return 0 
    for number in range(2 , num + 1) : 

        if num % number == 0 : 
            if num == number : 
                return 1 
            else : 
                return 0
    return 0 


def solution(numbers):
    purm = [] 
    cnt = 0 
    exists = set()
    
    for i in range(1 , len(numbers) + 1) : 
        purm = list(permutations(numbers, i)) #numbers 리스트에 대해 permute를 1부터 len(numbers) 까지 실행 
        
        for num in purm : 
            int_num = int(''.join(num))  #숫자로 변환 

            if int_num not in exists :   #이미 처리한 대상은 skip 할 수 있도록 처리 
                exists.add(int_num)
                cnt += check_sosu(int_num) 

    return cnt
