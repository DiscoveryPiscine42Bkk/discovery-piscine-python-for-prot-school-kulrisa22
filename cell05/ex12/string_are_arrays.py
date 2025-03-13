import sys

def find_and_print_z(input_string):
    """หาและแสดง 'z' ใน string ที่รับเข้ามา"""
    if 'z' in input_string:
        for char in input_string:
            if char == 'z':
                print('z')
    else:
        print('none')

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    find_and_print_z(input_string)