def print_square(indent,side,symbol):
   """Prints indented square of characters:

      indent = leading spaces (int)
      side   = side length (int)
      symbol = character (str). """
   for j in range(0,side):
      print (indent*" " + side*symbol)

print (print_square.__doc__)

