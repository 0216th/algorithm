def solution(n, m):
    
    div = 1   #최대공약수 
    mult = 1  #최소공배수 
    
    #n을 가장 크게 처리 
    if m >= n : 
        n , m = m , n 

    i = 2 
    
    while i <= m : 
        
        if m % i == 0 and n % i == 0 : #둘다 나뉘는 수이면 
            div *= i 
            m //= i 
            n //= i 
            i = 2 
        else : 
            i += 1 
    
    mult = div * n * m 
    print(div , mult)
        
    return [div , mult] 
