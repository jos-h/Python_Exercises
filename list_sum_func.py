l = [[1, 25, 33, 37, 45, 89, 103, 105, 109],
      [19, 29, 30, 35, 55, 79, 94, 101],
      [2, 6, 13, 15, 32, 39, 47, 60, 64, 100, 106],
      [3, 5, 10, 40, 52, 72, 74, 81, 84, 98, 102, 107],
      [44, 48, 57, 66, 75, 86, 91, 92, 110, 112],
      [36, 42, 80, 82, 90],
      [12, 14, 18, 26, 31, 34, 38, 43, 54, 61, 71, 85, 99],
      [0, 4, 9, 16, 23, 41, 93, 104],
      [7, 8, 21, 22, 51, 68, 77, 78, 108, 111],
      [17, 20, 27, 56, 62, 65, 70, 76, 87, 95, 96, 113],
      [11, 24, 50, 59, 63, 69, 97],
      [28, 46, 49, 53, 58, 67, 73, 83, 88, 114]]

print(max(sum(l, [])))

print("******************")
print(max([max(i) for i in l]))