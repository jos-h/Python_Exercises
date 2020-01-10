wrd_cnt = {}


def record_word_cnt(line):

    for i in line:
        if i != '':
            if i.lower() not in wrd_cnt:
                wrd_cnt[i.lower()] = 1
            else:
                wrd_cnt[i.lower()] += 1


def sorted_words(wrd_cnt):
    words = [(word, cnt) for word, cnt in wrd_cnt.items()]
    print(sorted(words, key=lambda x: x[1]))


with open(".//dummy.txt") as fp:
    print("reading file:", fp.name)
    for line in fp:
        record_word_cnt(line.strip().split())
    sorted_words(wrd_cnt)
    print(wrd_cnt)


