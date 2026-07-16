from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        for i in s:
            match i:
                case "(" | "{" | "[":
                    stack.append(i)
                case ")":
                    if len(stack) > 0 and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                case "]":
                    if len(stack) > 0 and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                case "}":
                    if len(stack) > 0 and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

        return True if len(stack) == 0 else False

       # stack_1 = deque()
       # stack_2 = deque()
       # stack_3 = deque()
       # bracket_track = ""

       # for i in s:
       #     match i:
       #         case "(":
       #             stack_1.append(i)
       #             bracket_track = i
       #         case ")":
       #             if len(stack_1) > 0 and bracket_track == "(": stack_1.pop()
       #         case "[":
       #             stack_2.append(i)
       #             bracket_track = i
       #         case "]":
       #             if len(stack_2) > 0 and bracket_track == "[": stack_2.pop()
       #         case "{":
       #             stack_3.append(i)
       #             bracket_track = i
       #         case "}":
       #             if len(stack_3) > 0 and bracket_track == "{": stack_3.pop()
       #         
       # return True if (len(stack_1) == 0 and len(stack_2) == 0 and len(stack_3) == 0) else False
