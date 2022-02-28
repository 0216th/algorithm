'''
문제링크 : https://programmers.co.kr/learn/courses/30/lessons/81301 [2021 카카오 채용연계형 인턴십] 
'''

def solution(s):
    
    #문자열 리스트화 
    s_list = list(s) 
    
    #숫자와 영단어 매칭을 위한 딕셔너리 
    alpha_dict = {
                   'zero'  :   '0'  
                 , 'one'   :   '1'
                 , 'two'   :   '2'
                 , 'three' :   '3'
                 , 'four'  :   '4'
                 , 'five'  :   '5'
                 , 'six'   :   '6'
                 , 'seven' :   '7'
                 , 'eight' :   '8'
                 , 'nine'  :   '9'
                 }

    tmp_str = "" 
    answer = []  
    

    for idx , string  in enumerate(s_list) : 
    
        if string.isdigit() : #숫자일경우 바로 append
            answer.append(string)  
        
        else :  #문자일 경우 변화처리가 필요 
            
            tmp_str += string
            
            if len(tmp_str) >= 3 :  #추가된 문자가 3개 이상일 경우 부터 변환 
                
                if tmp_str in alpha_dict.keys() :
                    answer.append(str(alpha_dict[tmp_str]))
                    tmp_str = "" 
                    
    
    answer = int("".join(answer))
    
    
    return answer
