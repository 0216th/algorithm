'''
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/82612 [위클리 챌린지] 
'''

def solution(price, money, count):
    answer = -1
    
    #놀이기구를 타는데 필요한 액수 
    sum = 0 
    for i in range(1,  count + 1 ) : 
        sum += price * i 

    #현재 가진 액수에서 차감     
    answer = money - sum
    
    #결과가 음수이면 부족한 금액이므로 , 부호 변환하여 제공 
    if answer <= 0 : 
        answer *= -1 
    #결과가 양수면 부족하지 않으므로 , 0 리턴
    else : 
        answer = 0 
    
    return answer
