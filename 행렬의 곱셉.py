'''
url : https://programmers.co.kr/learn/courses/30/lessons/12949 
''' 

import numpy as np 

def solution(arr1, arr2):
    
    #numpy에서 배열간의 내적 계산인 dot() 활용 
    A = np.array(arr1)
    B = np.array(arr2)
    
    answer = A.dot(B).tolist() #ndarray 를 list화

    return answer
  
  
