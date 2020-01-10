from pprint import pprint

tree_dictionary = {}

ll = [(2, 0, 100, 3), (2, 100, 101, 10), (2, 100, 102, 11), (2, 100, 103, 12), (2, 101, 110, 201), (2, 102, 104, 21),
      (2, 103, 105, 22), (2, 0, 200, 22), (2, 200, 201, 23), (2, 201, 205, 31), (2, 201, 206, 32), (2, 0, 300, 30)]


def generate_dict(ll, parent, p_visit):
    for i in range(len(ll)):
        if parent == ll[i][2] and p_visit == 0:
            p_visit = 1
            tree_dictionary['parent'] = {}
            tree_dictionary['parent'][parent] = []
            generate_dict(ll[i + 1:], parent, p_visit)
            p_visit = 0
        else:
            if parent == ll[i][1] and p_visit == 1:
                tree_dictionary['parent'][parent].append(ll[i][2])
                generate_dict(ll[i + 1:], parent, p_visit)
                p_visit = 0
            else:
                break


def main():
    generate_dict(ll, 100, 0)  # int(input()))
    pprint(tree_dictionary)


if __name__ == '__main__':
    main()
