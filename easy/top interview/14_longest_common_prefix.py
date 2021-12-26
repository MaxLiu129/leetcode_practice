"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        # if the strs has nothing inside, return an empty list
        if not strs:
            return ""
        
        # make the first str in the list as an example str.
        longest = strs[0]
        
        # start to compare each char in the example str to the rest of the target strs.
        for i in range(len(strs[0])):
            for str in strs:
                # In the following situation, we think we found the longest prefix.
                # 1. the target str has less chars than the example str.
                # 2. the target str's char is not the same with the example str'char at "i" position
                if len(str) <= i or strs[0][i] != str[i]:
                    # return the example str from the starting char to "i-1" position
                    return strs[0][:i]
        
        # if after the for loop above we did not get a return. That means all chars in the example str
        # can be found in all other target strs, so we can just return the example str.
        return strs[0]
                
                    
            
        