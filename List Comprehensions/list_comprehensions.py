'''
Write one line of Python that takes this list a 
and makes a new list that has only the even elements of this list in it
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

def even_elements(even_list):
	return [a for a in even_list if a % 2 == 0]

def prime_numbers(start,end):

	if start == 1:
		print("Prime numbers start from 2 enter valid start point")
	else:
		nonprimes = [j for i in range(start,end) for j in range(i*2,200,i)]
		return [x for x in range(start,end) if x not in nonprimes]

def main():
	print("even elements",even_elements([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))
	print("prime numbers",prime_numbers(2,200))

if __name__ == '__main__':
	main()