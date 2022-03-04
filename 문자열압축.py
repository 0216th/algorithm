def solution(s):
    
    answer = 9999 #하나의 문자열 단위로 자를때 길이 
    
    tmp = '' 
    cnt = 0 
    packing = '' 
    
    for i in range(1 , len(s) + 1) : 

        tmp = s[0 : i]
        cnt = 1 
        
        for j in range(i , 1001 , i) :  
            
            if tmp == s[j : j + i] : 
                cnt += 1
            else : 
                if cnt >= 2 : 
                    packing += str(cnt) + tmp
                else : 
                    packing += tmp 
                
                tmp = s[j : j + i]
                cnt = 1 
        packing += tmp
        answer = min(answer , len(packing))
        packing = '' 
       
    return answer
