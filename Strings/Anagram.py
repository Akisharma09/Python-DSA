    """
    Approach: Add all characters of one strig in hasmap with value as count and key/index as ord(character) i.e. unicode of character.
    The using second string check if the charater is in first hashmap, if not return NO if yes then decrement count by 1
    
    if loop goes towards the end then return true.
    """
    def isAnagram(self,a,b):
        #code here
        if len(a) != len(b):
            return 'NO'
        hash_map_a = [0]*256
        for ch in a:
            hash_map_a[ord(ch)] += 1
            print(ord(ch))
            
        for ch in b:
            if hash_map_a[ord(ch)] == 0:
                return 'NO'
            if hash_map_a[ord(ch)] != 0:
                hash_map_a[ord(ch)] -=1
        
        return 'YES'
