from math import factorial, pi, sin, cos
from symbolic import remove_parens, is_x, is_registered_function, cleanup, is_number, has_x, to_number, has_no_ops
from parsing import get_next_split
import matplotlib.pyplot as plt


def registered_function_ddx(fun):
    if fun == 'sin':
        return 'cos'
    elif fun == 'cos':
        return '-1*sin'
    else:
        raise Exception("Unsupported function, not registered...")


def ddx(f):
    f = remove_parens(f)
    if is_x(f):
        return "1"
    elif has_no_ops(f) and is_registered_function(f):
        i = f.index('(')
        ddfun = registered_function_ddx(f[0:i])
        return ddfun + '(' + cleanup(f[i:]) + ') * ' + ddx(f[i:])
    elif is_number(f) or not has_x(f):
        return "0"
    else:
        s = get_next_split(f)
        left = f[0:s].strip()
        op = f[s]
        right = f[s+1:].strip()

        if op == "+":
            result = ddx(left) + " + " + ddx(right)
        elif op == "-":
            result = ddx(left) + "-" + ddx(right)
        elif op == "*":
            result = right+" * "+ddx(left) + " + " + ddx(right)+" * "+left
        elif op == "/":
            result = ddx(left) + " * " + right+" - " + \
                left+ddx(right)+"/"+left**2
        elif op == "^":
            if has_x(left) and is_number(right):
                result = right + " ^ " + left+" ^ "+right-1+" ^ " + ddx(left)
            else:
                raise Exception(str(f) + " is not covered")
        else:
            raise Exception(str(op) + " is not covered")
    return cleanup(result)


def taylor(f, N, A):
    taylor_series = " "
    for n in range(N+1):
        dd = f
        for i in range(n):
            dd = ddx(dd)
        taylor_series += "+ (" + str(dd.replace("x", str(A))) + " * "+"( "+"x" + \
            "-" + str(A) + ")" + "^" + str(n) + \
            ")"+"/"+str(factorial(n))
    return taylor_series


def try_function(name, f, x, A):
    approx = taylor(f, 11, "-" + A)
    print(f, "≈", approx)
    print(f.replace("x", x + " - " + A), "≈",
          eval(approx.replace("^", "**").replace("x", x)))

    plt.clf()
    R = [x * 0.1 for x in range(100)]
    plt.plot(R, [eval(approx.replace("^", "**").replace("x", str(x)))
             for x in R], color='C0')
    plt.plot(R, [eval(f.replace("^", "**").replace("x", str(x)))
             for x in R], color='C1')
    plt.savefig(name + ".png")


try_function("two-plus-x", "2 + x", "pi", "0")
try_function("cos-x", "cos(x)", "pi", "0")


print(cleanup(ddx("cos(x)")))
print(cleanup(ddx("x + x")))
