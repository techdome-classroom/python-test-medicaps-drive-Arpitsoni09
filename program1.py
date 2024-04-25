class Solution(object):
    def isValid_(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass

def is_valid(s):
  """
  Checks if a string containing parentheses is valid.

  Args:
      s: A string containing characters '(', ')', '{', '}', '[' and ']'.

  Returns:
      True if the parentheses are balanced, False otherwise.
  """
  stack = []
  mapping = {")": "(", "}": "{", "]": "["}
  for char in s:
    if char in mapping:
      top = stack.pop() if stack else None
      if top != mapping[char]:
        return False
    else:
      stack.append(char)
  return not stack

# Examples
print(is_valid("()"))  # Output: True
print(is_valid("()[]{}"))  # Output: True
print(is_valid("(]"))  # Output: False
print(is_valid("([)]"))  # Output: False
print(is_valid("{[]"))  # Output: False (missing closing ")")
 



  

