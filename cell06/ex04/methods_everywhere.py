import sys

def shrink(input_string):
    print(input_string[:8])
    
def enlarge(input_string):
    print(input_string + 'Z' * (8 - len(input_string)))

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        else:
            enlarge(arg)
