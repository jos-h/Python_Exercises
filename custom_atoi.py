import re


class Solution:

    def myAtoi(self, istr: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        string_length = len(istr)
        istr = istr.strip()
        istr = re.findall("(^[\+\-0]*\d+)\D*", istr)
        try:
            result = int("".join(istr))
            if result > INT_MAX > 0:
                return INT_MAX
            elif result < INT_MIN < 0:
                return INT_MIN
            else:
                return result
        except:
            return 0

        # if string_length == 0:
        #     return ' '
        # number = 0
        # sign = ''
        # visit = 0
        # for i in istr:
        #     if '0' <= i <= '9':
        #         number = number * 10 + (int(i) - 0)
        #     elif i == ' ' and visit == 0:
        #         pass
        #     elif i == '-' and visit == 0 or i == '+' and visit == 0:
        #         sign = i
        #         visit = 1
        #     elif ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        #         break
        #         # return number
        #     else:
        #         break
        # # number = int(sign + str(number))
        #
        # if sign == '-':
        #     number = int(sign + str(number))
        #     # print(number)
        #     if number <= INT_MIN:
        #         return INT_MIN
        #     elif number >= INT_MAX:
        #         return INT_MAX
        #     return number
        # else:  # sign == '+':
        #     return number


def main():
    obj = Solution()
    print(obj.myAtoi('42'))
    print(obj.myAtoi("   -42"))
    print(obj.myAtoi("4193 with words"))
    print(obj.myAtoi("words and 987"))
    print("-91283472332", obj.myAtoi("-91283472332"))
    print(obj.myAtoi("3.14159"))
    print(obj.myAtoi("-+2"))
    print(obj.myAtoi("  -0012a42"))
    print(obj.myAtoi("   +0 123"))


if __name__ == '__main__':
    main()
