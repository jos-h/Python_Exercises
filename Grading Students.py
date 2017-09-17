"""
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.

Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grades and the next multiple of 5  is less than 3, round  up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

For example, grade=84 will be rounded to 85 but grade=29 will not be rounded
because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's n  students,
write code to automate the rounding process. For each grade,
round it according to the rules above and print the result on a new line.
"""


def grade_roundoff(item, loop_cnt):
    i = 0
    while i < loop_cnt:
        item += 1
        i += 1
        if item % 5 == 0:
            break
    return item


def solve(grades):
    loop_cnt = 2
    for item in grades:
        if item % 5 == 0:
            continue
        elif not item % 5 == 0:
            new_item = grade_roundoff(item, loop_cnt)
            if new_item % 5 == 0:
                if new_item >= 40:
                    old_index = grades.index(item)
                    grades.remove(item)
                    grades.insert(old_index, new_item)
    return grades


def main():
    n = int(input().strip())
    result = []
    grades = []
    for grades_i in range(n):
        grades_t = int(input().strip())
        grades.append(grades_t)
    result = solve(grades)
    print("\n".join(map(str, result)))


if __name__ == '__main__':
    main()
