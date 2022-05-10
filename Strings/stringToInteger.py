  """
  sign = + 
  if first character = - then sign = -
  for character in string:
    if ord(character) - ord('0') not between 0 and 9 then the character is not a number hence return -1
    number = number*10 + ord(character) - ord('0') // ord('0') = 47 
  
  if sign is + then return 1*number
  else return -1* number

  """
  
  def atoi(self,string):
        # Code here
        number = 0
        sign = 0
        for ch in string:
            if ch == '-':
                sign += 1
                continue
            if ord(ch)-ord('0') < 0 or ord(ch)-ord('0') > 9:
                return -1
            number = number*10 + ord(ch)-ord('0')
        
        if sign == 0:
            return number
        elif sign == 1:
            return -1*number
        else:
            return -1
