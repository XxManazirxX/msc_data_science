symbol= "*" 
def print_square(indent,side):
    symbol= "^" 
    for j in range(0,side):
        print (indent*" " + side*symbol)

symbol= "*" 

print_square(0,3)
