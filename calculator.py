def calculate(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")


def main():  # pragma: no cover
    print("Simple Calculator (type exit to quit)")

    while True:
        op = input("Enter operation (+ - * /): ")

        if op == "exit":
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", calculate(op, a, b))
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":  # pragma: no cover
    main()