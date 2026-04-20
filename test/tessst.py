from test import x, y, swapVal

# Directly using x, y, and swapVal without the module prefix
print("x value: ", x, "y value:", y)

# Using the swapVal function
x, y = swapVal(x, y)

print("x value: ", x, "y value:", y)