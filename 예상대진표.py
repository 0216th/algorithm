def solution(n,a,b):
    answer = 0
    cnt = 0 # 토너먼트 라운드 
    
    while a != b : 
        cnt += 1 #라운드 추가 
        
        a , b = (a+1)//2 , (b+1)//2
        '''
        예시 
        a = 5 , b= 11 일경우 
        cnt = 1 , a = (5+1) // 2 = 3 , b = (11+1) // 2 = 6 
        cnt = 2 , a = (3+1) // 2 = 2 , b = (6 + 1) // 2 = 3
        cnt = 3 , a = (2+1) // 2 = 1 , b = (3 + 1) // 2 = 2 
        cnt = 4 , a = (1+1) // 2 = 1 , b = (2 + 1) // 2 = 1 
        '''
      
    return cnt
  
'''
  다른 사람의 풀이 
  
  def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

^ : 배타적논리합연산자(XOR)
bit_length() 는 0b 뒤에 숫자의 개수를 표현함 
ex) (3).bit_length() 의 경우 0b11 이므로 2개 
ex) (4).bit_length() 의 경우 0b100 이므로 3개  
자바와 달리 0000 0000 ... 0011 이 아니라 1이 있는 시점부터 작성해서 리턴을 한다. 

... 
