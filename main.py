

for i in range(1, 101):
    str = ""

    if (i % 3 == 0):
        str += "Fizz"
    if (i % 5 == 0):
        str += "Buzz"
    if (str == ""):
        str = "%d" % i
    print("%s" % str)
