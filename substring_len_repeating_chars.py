def substring_len_repeating_chars(s):
    l = []
    news = ''
    if len(s) == 0:
        print(len(s))
    else:
        for i in s:
            if i not in news:
                news += i
                l.append(news)
            else:
                # if news not in l:
                l.append(news)
                news = ''
        print(len(max(l, key=len)))
        print(l)


def new_substring_len_repeating_chars(s):
    dct = {}
    max_so_far = curr_max = start = 0
    for index, i in enumerate(s):
        if i in dct and dct[i] >= start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dct[i]
            start = dct[i] + 1
        else:
            curr_max += 1
        dct[i] = index
    print(max(max_so_far, curr_max))
    print(dct)

'''
s = 'abba'
    # s = 'pwwkew'
    # s = 'geeksforgeeks'
    s = "aab"
'''

# substring_len_repeating_chars("aab")
print("**************************************************")
new_substring_len_repeating_chars("aab")
