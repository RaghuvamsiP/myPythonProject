# Ex1:
x = 5
y = 10

x, y = y, x

print(x, y)

# Ex2:
x = 5
y = 10

temp = y
y = x
x = temp

print(x, y)


# Ex3:
x = 5
y = 10

x = x + y  # 15
y = x - y  # 5
x = x - y
print(x, y)
