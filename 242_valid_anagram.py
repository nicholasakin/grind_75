'''
VALID ANAGRAM




Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

 Example 1:

 Input: s = "anagram", t = "nagaram"
 Output: true
 Example 2:

 Input: s = "rat", t = "car"
 Output: false
  

  Constraints:

  1 <= s.length, t.length <= 5 * 104
  s and t consist of lowercase English letters.

'''


def isAnagram(s1, s2):
    freq=[0] * 26             #map to hold ascii # values of characters
   
    if len(s1) != len(s2):
        return false
    
    for i in range(len(s1)):            #calc. freq. of each character per string
        freq[ord(s1[i]) - ord('a')] += 1  #adding 1 for freq in s1
        freq[ord(s2[i]) - ord('a')] -= 1  #subtracting 1 for freq in s2

    for i in range(len(freq)):
        
        print(freq)
        if freq[i] != 0:
            return False


    return True
    

s1="anagram"
s2="nagaram"




print(isAnagram(s1, s2))
isAnagram(s1,s2)

   
    








