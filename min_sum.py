def min_sum(num, k):
    for ele in num:
        for i in range(1, len(num)):
            if ele > num[i]:
                num[i] = int(num[i] / k)
        pass
    print(num)
    print(min(num))

num = [10, 20, 30, 23]
min_sum(num, 4)
