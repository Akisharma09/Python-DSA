def TowerOfHanoi(n , s, d, h):
    if n == 1:
        print('moving plate {} from {} to {}'.format(n,s,d))
        return
    TowerOfHanoi(n-1,s,h,d)
    print('moving plate {} from {} to {}'.format(n,s,d))
    TowerOfHanoi(n-1,h,d,s)
    
    return 
    
    
         
# Driver code
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods
