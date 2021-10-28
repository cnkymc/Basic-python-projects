def fibonacci(n, output=[]):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        output.append(str(a))
    return output

number = int(input("Length of fibonacci sequence: "))

print("Result: {}".format(",".join(fibonacci(number))))