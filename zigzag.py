def convert(s: str, numRows: int) -> str:
    str_len = len(s)
    if 0 == str_len:
        return ''
    if 1 == numRows:
        return s

    diagonal_chars_count = numRows - 2
    chars_count_in_col_and_diagonal = numRows + diagonal_chars_count
    buff = [''] * numRows
    for i in range(str_len):
        line = i % chars_count_in_col_and_diagonal
        if line >= numRows:
            line = chars_count_in_col_and_diagonal - line

        buff[line] = buff[line] + s[i]

    print("".join(buff))


def convert_another_logic(s: str, num_rows: int) -> str:
    str_len = len(s)
    if s == '' or str_len == 0 or num_rows <= 0:
        return " "
    if num_rows == 1:
        return s

    arr = []
    size = 2 * num_rows - 2

    for i in range(num_rows):
        for j in range(i, str_len, size):
            arr.append(s[j])

            if i != 0 and i != num_rows - 1 and (j + size - 2 * i) < str_len:
                arr.append(s[j + size - 2 * i])
    print("".join(arr))


STR = "PAYPALISHIRING"
# convert(STR, 4)

convert_another_logic(STR, 3)
