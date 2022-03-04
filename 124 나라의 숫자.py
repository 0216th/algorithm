from collections import deque #stack구현을 위한 deque 임포트 

def solution(n):
    
    deque_ = deque() 
    
    while n != 0 : 
        
        if n % 3 == 0 : 
            deque_.appendleft(4)
            n = n // 3 - 1 
        else : 
            deque_.appendleft(n%3) 
            n = n // 3 
    
    answer = ''.join(list(map(str , deque_)))
    return answer
  
  '''
  공식 예시 36 = 424(124기준) 
  
  36 % 3 = 0 이므로 4를 리스트 앞에 대입  
  36 // 3 = 12 로 처리 후 -1 를 한다. (n = 11) 
 
  11 % 3 = 2 이므로 2를 리스트 앞에 대입 (현재 리스트 [2 , 4]) 
  11 // 3 = 3 로 처리 (n = 3 ) 
  
  3 % 3 == 0 이므로 4를 리스트 앞에 대입 (현재 리스트 [ 4 , 2 , 4 ] )
  3 // 3 = 1 로 처리 후 -1을 한다 (n = 0) 
  
  n = 0 이므로 반복문 종료 , 위 리스트를 join 처리해 합쳐 출력. 
  '''
