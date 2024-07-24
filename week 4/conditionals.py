x = 75

print(x == 60)

if x == 60:
    x += 5

    print(x)
elif x == 75:
    x -= 5
    print(x)

elif x == 80:
    x /= 5
    print(x)

else:
    print("x is neither of those values")