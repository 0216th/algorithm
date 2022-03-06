'''
url : https://programmers.co.kr/learn/courses/30/lessons/42577
'''

def solution(phone_book):
    answer = True

    # 길이가 하나라서 접두어 비교가 불가능 한 경우 
    if len(phone_book) == 1 : 
        return True 

    phone_book.sort()
    check = phone_book[0]   

    for i in range(1 , len(phone_book)) : 
        if check == phone_book[i][0: len(check)] : 
            return False         
        else : 
            check = phone_book[i]

    return answer
