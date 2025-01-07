dimensions=(600,700,800,900,1000)
#dimensions[0]=250    It causes error  as tuple does not support value assignment
for dimension in dimensions:
    print(dimension)
my_t=(3,)    # Here use of trailing comma is necessary to make a tuple of a single element
print(my_t)    