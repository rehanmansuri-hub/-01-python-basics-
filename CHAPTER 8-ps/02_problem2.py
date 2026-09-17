#  celsius to fahrenheit formula

# formula c/5 = f-32/9


def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter tempreature in F: "))
c = f_to_c(f)

print(F"{round(c, 2)}degree c")