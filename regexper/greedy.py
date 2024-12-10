import re

# Input string with angle brackets
text = "<tag>content</tag>"

# Greedy pattern
pattern = r"<.*>"
match = re.search(pattern, text)
if match:
    print("Greedy match:", match.group())

# Lazy pattern
pattern_lazy = r"<.*?>"
match_lazy = re.search(pattern_lazy, text)
if match_lazy:
    print("Lazy match:", match_lazy.group())
