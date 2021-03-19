
def findNthOccur(string , ch, N) : 
    occur = 0;  
  
    # Loop to find the Nth  
    # occurence of the character  
    for i in range(len(string)) : 
        if (string[i] == ch) : 
            occur += 1;  
       
        if (occur == N) : 
            return i;  
      
    return -1;  
  
string = 'johnny'
ch = '4'
N = 3

print(findNthOccur(string,ch,N))