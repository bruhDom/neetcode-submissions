class Solution:

    def encode(self, strs: List[str]) -> str: # if we have ["hi", "pumps"], we encode to "2#hi5#pumps"

        encoded_str = ""

        for s in strs:
            n = len(s)
            encoded_str += str(n) + "#" + s

        return encoded_str

    def decode(self, s: str) -> List[str]: # if we have 2#hi5#pumps, we decode to ["hi", "pumps"]
        
        decoded_str, i  = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
        
            decoded_str.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length
    
        return decoded_str
        



