"""
Approach is :
    remainder = number % 26, quotient = number//26
    
    if remainder is zero append Z and number = number//26
    
    if remainder is non zero then (remainder + ord('A') -1 ) and number = number // 26
    
    take and example of 1 as column nummber which should be A
    now 1%26 = 1 and 1//26 = 0
    ord(A) =  65 and we want to get A so remainder is 1 thus 1 + 65 -1 is 65
    and chr(65) is 'A'. 
    example 2: 26th column name should be Z
    26%26 is 0
    and according to our condition 0 is 'Z'
"""

def excelColumn(n):
    column_name = ''
    while n>0:
        if n%26 == 0:
            column_name += 'Z'
            n = n//26 -1
        else:
            column_name += chr(n%26 + ord('A') -1) # n = 1 column name should be 'A'
            n //= 26
    
    return column_name[::-1]

def main():
    print(excelColumn(53))
    

if __name__ == '__main__':
    main()
    
