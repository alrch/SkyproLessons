def closest_mod_5(x):
    for i in range(5):
        #print(i)
        if (x + i) % 5 == 0:
            return x + i

    return "I don't know :("


print(closest_mod_5(int(input())))
