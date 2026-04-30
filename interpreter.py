# This is a simple interpreter that can evaluate basic arithmetic expressions.
def main():
    i = input("enter the expression: ")
    cal(i)

def cal(value):
    x, y, z = value.split(" ")
    x = float (x)
    z = float (z)
    if y == "+":
        print(x+z)
    elif y == "-":
        print(x-z)
    elif y == "*":
        print(x*z)
    elif y == "/":
        print(x/z)
    else:
        print ("invalid choice")
    return
main()
