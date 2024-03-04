# E: Y2 = X3 + 497 X + 1768, p: 9739

a = 497
b = 1768
p = 9739

x  = 8045
y  = 6936


x_neg = x % p
y_neg = -y % p

print(f"({x}, {y}) + ({x_neg}, {y_neg}) = O")