"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"abcde###" ==> "ab"

"""

def backspace(str):
    listy = []
    for i in str:         
        if i == '#' and listy != []:  # add the and conditional in case list is empty
            listy.pop()
        elif i != '#':       # can change else to elif so itll help with third example below ↓ and not give a '#' for the answer 
            listy.append(i)

    if listy == []:
        return '""'
    else: 
        return "".join(listy)

print(backspace("abc#d##c"))
print(backspace("abc##d######"))
print(backspace("#######"))
print(backspace(""))
print(backspace("abcde###"))

# Time: Linear
# Space: Linear

# Morgan's Answer:
def love_tuesday(string):
    backspace = []
    # need to us .pop
    # === "#"
    # .join? in else
    for i in string:
        if i == "#" and backspace != []:
            backspace.pop()
        elif i != "#":
            backspace.append(i)
    i = "".join(backspace)
    return i
print(love_tuesday("abcde###"))