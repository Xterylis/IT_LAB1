def f(x):
    return 2 + 5 * x - 10 * x ** 2 - 5 * x ** 3 - x ** 5


def half_method(a, b, epsilon):
    iterations = 0

    while (b - a) >= epsilon:
        c = (a + b) / 2
        fc = f(c)
        print(f"Ітерація {iterations}: a={a}, b={b}, c={c}, f(c)={fc}")

        if fc == 0.0:
            break
        elif fc * f(a) < 0:
            b = c
        else:
            a = c

        iterations += 1

    return (a + b) / 2, iterations

a = -3
b = 2
epsilon = 0.001

x, num_iterations = half_method(a, b, epsilon)
f_x = f(x)

print(f"\nМаксимум функції: f(x) = {f_x}  при x = {x}")
print(f"Кількість ітерацій: {num_iterations}")
