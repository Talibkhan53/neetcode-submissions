
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, result: str) -> List[str]:
        i = 0 
        l = []
        while i < len(result):
            # Find the position of the delimiter '#'
            j = result.find('#', i)
            print(j)
            
            # Extract the length of the word (handles multi-digit lengths like 10#)
            length = int(result[i:j])
            print("Length",length)
            
            # Extract the actual word using the parsed length
            word = result[j + 1 : j + 1 + length]
            print("Word",word)
            print("J+1",j+1)
            l.append(word)
            
            # Move the pointer to the start of the next encoded block
            i = j + 1 + length

        return l