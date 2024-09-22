print("Python has NO block scope.")

print("variables created within a block (such as an if statement), are accessible outside of the block")
a = "apple"

if "a" in a:
    p = "pears"

print(p)

#pycharm shows error above, but code is functional and correct