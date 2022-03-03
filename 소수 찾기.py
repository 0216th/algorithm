'''
참고 블로그 : https://seongonion.tistory.com/43 

초반 2중 for 문을 사용할 당시 시간초과 발생

꼭 소수를 2중 for문으로 나눠 나머지가 0인 것들을 찾는것이 아니라 
다음처럼 역발상을 할 수 있다는 것이 신기했다. 
'''

def find_sosu(n) : 
    
    list_ = [True] * (n + 1)
    list_[0] = False 
    list_[1] = False 
    
    for i in range(2  , n//2 + 1 ) : 
        
        if list_[i] == True :
            j = 2 
            
            while (i * j) <= n :   # 핵심 2 일때 4,6,8,10...에 해당하는 데이터를 모두 False 처리 (소수가 아님) 
                                   #      3 일때는 위에서 True 값을 가지고 있으므로 이 로직이 실행되고, 3,6,9,12,15 ... 등이 False 처리 
                                   #      4 일때 위에서 False 처리 되었으므로 실행하지 않음
                                   # (n // 2 + 1 단계에서는 j = 2 이고 , 위에서 False 처리 되었다면 추가적인 실행을 하지 않음 
                list_[i*j] = False
                j+=1 
    return list_
    

def solution(n):
    cnt = 0 
    for list_ in find_sosu(n) : 
        if list_ :
            cnt += 1 
    
    return cnt
