gsymbol= "*" 
def print_square(indent,side):
    lsymbol= "^" 
    for j in range(0,side):
        print (indent*" " + side*lsymbol)

print_square (0,3) 
