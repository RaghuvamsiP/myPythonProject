# 1. break 2. continue
# break: As soon as condition is satisfied, the looping will be stopped
# Continue: In looping, it will skip the condition value

# break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
# use multiple condition using 'or' operator
for i in range(1, 10):
    if i == 5 or i == 7 or i == 9:
        continue
    print(i)



