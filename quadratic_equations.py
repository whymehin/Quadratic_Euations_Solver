import math

print("This program solve quadratic equations in the "
      "form of (Ax^2+Bx+C=0)\n")


a = input("Input the value of A: ")
b = input("Input the value of B: ")
c = input("Input the value of C: ")

def solver(a,b,c):
    if a.strip("-").isnumeric() and b.strip("-").isnumeric() and c.strip("-").isnumeric():
        a = float(a)
        b = float(b)
        c = float(c)
        delta = b * b - 4 * a * c

        if delta > 0:
            d = math.sqrt(delta)
            answer1 = ((-b) + d) / (2 * a)
            answer2 = ((-b) - d) / (2 * a)
            print("There are two distinct roots,\n"
                  "They are " + str(round(answer1, 2)) + " and " + str(round(answer2, 2)))
        elif delta == 0:
            answer = -b / 2 * a
            print("Two roots are equal,\n "
                  "which is " + str(round(answer, 2)))
        elif delta < 0:
            print("There is no real root.")

    else:
        print("Invalid Input")

solver(a,b,c)