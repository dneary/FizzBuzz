# EclipseCon Europe Che Challenge
#
# This program prints the numbers from 1 to 100, with every multiple of 3
# replaced by "Fizz", and every multiple of 5 replaced by "Buzz". Numbers
# divisible by both are replaced by "FizzBuzz". Otherwise, the program
# prints the number.
#
# Your mission, if you choose to accept it, is to change this program so that,
# in addition to the above, it prints "Fizz" for any number which includes a 3,
# and prints "Buzz" for any number including a 5. After modification, for
# example, the number 53 should be replaced by "FizzBuzz".
#
# Once you have completed the challenge, you will be entered into a draw for
# one of the ChromeBooks at the Eclipse Che booth.

for i in range(1, 101):
    str = ""

    if (i % 3 == 0):
        str += "Fizz"
    if (i % 5 == 0):
        str += "Buzz"
    if (str == ""):
        str = "%d" % i
    print("%s" % str)
