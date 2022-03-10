def solution(n):
    k = 0 
    
    #N을 나누면서 홀수이면 1칸씩 이동해서 N이 0이될때 종료 
    
    while n != 0 : 
        if n % 2 != 0 : 
            k += 1 
        n //= 2 
    
    return k
