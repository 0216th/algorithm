'''
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/77484
'''

def solution(lottos, win_nums):
    
    lottos.sort(reverse=True)
    match_count = 0 
    zero_cnt = 0 
    
    #지워지지 않는 숫자 중에서 맞춘 횟수 카운트
    for num in lottos : 
        if num == 0 : 
            zero_cnt += 1
            continue 
            
        if num in win_nums : 
            match_count += 1
    
    
    min_correct = match_count            #최소로 맞춘경우 
    max_correct = match_count + zero_cnt #최대로 맞춘 경우 
    
    if min_correct == 0 : 
        min_correct = 1 
    
    if max_correct == 0 : 
        max_correct = 1 
        
    answer = [7 - max_correct , 7 - min_correct]
    
    return answer
