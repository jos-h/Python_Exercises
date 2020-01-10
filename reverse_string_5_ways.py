def reverse_string_I(input_str):
    print(f'Reversed string is =======> {input_str[::-1]}')

def reverse_string_II(input_str):

    print("reversed string is =======>", end='')
    for index in range(len(input_str) - 1, -1, -1):
        print(f'{input_str[index]}', end='')

def reverse_string_III(input_str):
    
    print(f"Reversed string is =======> {''.join(list(reversed(input_str)))}")

def reverse_string_IV(input_str):
    if len(input_str) == 0:
        return input_str
    else:
        return reverse_string_IV(input_str[1:]) + input_str[0]

def reverse_string_V(input_str):

    temp_str = ''
    for each in input_str:
        temp_str = each + temp_str
    print(f"Reversed string is ======> {temp_str}")

def main():
    s = "kunal"

    print("Using slice to reverse the string")
    reverse_string_I(s)

    print("\n\nUsing the negative indexing way")
    reverse_string_II(s)

    print("\n\nUsing the reversed function")
    reverse_string_III(s)

    print("\n\nUsing recursion to reverse string")
    print(f"Reversed string is =======> {reverse_string_IV(s)}")

    print("\n\nUsing concatenation in different way")
    reverse_string_V(s)
    
if __name__ == '__main__':
    main()
