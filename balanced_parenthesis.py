s = ')()()){([])}()(((((())))'
increment_count = decrement_count = 0
stack = []
# brackets = ['(', ')', '{', '}', '[', ']']
for i in s:
    if i == '(' or i == '{' or i == '[':
        increment_count += 1
        # stack.append(i)
    if i == ')' or i == '}' or i == ']':
        increment_count -= 1
        # decrement_count -= 1
        # stack.remove('(')

# if len(stack) == 0:
#     print("balanced")
# else:
#     print("Un-balanced")
print(increment_count)
if increment_count == 0:
    print("YES")
else:
    print("NO")
